import requests

from api_collection.dogs.endpoints_dogs import EndpointsDogs
from api_collection.headers import Headers
from api_collection.dogs.response_models.get_sub_breeds_list_model import GetSubBreedsListModel
from api_collection.dogs.response_models.get_sub_breed_image_url_model import GetSubBreedImageUrlModel
from api_collection.dogs.response_models.get_breed_image_url_model import GetBreedImageUrlModel


class ApiDogs:
    def __init__(self):
        self.endpoints = EndpointsDogs()
        self.headers = Headers()

    def get_sub_breeds_list(self, breed):
        response = requests.get(url=self.endpoints.SUB_BREEDS_LIST_URL(breed), headers=self.headers.BASIC_HEADERS)
        assert response.status_code == 200, response.json()
        model = GetSubBreedsListModel(**response.json())
        return model

    def get_sub_breed_image_url(self, breed, sub_breed):
        response = requests.get(url=self.endpoints.SUB_BREED_IMAGE_LINK_URL(breed, sub_breed))
        assert response.status_code == 200, response.json()
        model = GetSubBreedImageUrlModel(**response.json())
        return model

    def get_breed_image_url(self, breed):
        response = requests.get(url=self.endpoints.BREED_IMAGE_LINK_URL(breed))
        assert response.status_code == 200, response.json()
        model = GetBreedImageUrlModel(**response.json())
        return model

    def get_list_of_sub_breeds_images(self, breed):
        url_images = []
        sub_breeds_list = self.get_sub_breeds_list(breed)
        if not sub_breeds_list.message:
            single_image_url = self.get_breed_image_url(breed)
            url_images.append(single_image_url.message)
        else:
            for sub_breed in sub_breeds_list.message:
                single_image_url = self.get_sub_breed_image_url(breed, sub_breed)
                url_images.append(single_image_url.message)
        return url_images
