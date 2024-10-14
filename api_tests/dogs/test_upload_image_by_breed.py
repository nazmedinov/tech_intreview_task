import pytest

from api_collection.dogs.api_dogs import ApiDogs
from api_collection.image_uploader.api_uploader import APIUploader


class TestUploadImageByBreed:

    @pytest.mark.parametrize('breed_path',
                             [pytest.param('appenzeller', id='appenzeller breed'),
                              pytest.param('poodle', id='poodle breed')],
                             indirect=True)
    def test_upload_image_by_breed(self, breed_path):
        uploader_api = APIUploader()
        dogs_api = ApiDogs()
        uploader_api.create_folder(breed_path)
        list_of_sub_breeds_images = dogs_api.get_list_of_sub_breeds_images(breed_path)
        for image in list_of_sub_breeds_images:
            upload_photo = uploader_api.upload_photo_to_folder(breed_path, image, '123')
            print(upload_photo.href)
