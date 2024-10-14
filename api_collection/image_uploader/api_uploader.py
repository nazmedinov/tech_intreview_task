import os
import requests

from dotenv import load_dotenv
from api_collection.image_uploader.endpoints_uploader import EndpointsUpLoader
from api_collection.headers import Headers
from api_collection.image_uploader.response_models.create_folder_model import CreateFolderModel
from api_collection.image_uploader.response_models.upload_photo_model import UploadPhotoModel


class APIUploader:
    def __init__(self):
        load_dotenv()
        self.endpoints = EndpointsUpLoader()
        self.headers = Headers()
        self.uploader_token = os.environ.get('UPLOADER_TOKEN')

    def create_folder(self, path='test_folder'):
        response = requests.put(
            url=f'{self.endpoints.CREATE_FOLDER_URL}?path={path}',
            headers=self.headers.get_uploader_headers(self.uploader_token)
        )
        assert response.status_code == 201, response.json()
        model = CreateFolderModel(**response.json())
        return model

    def delete_folder(self, path='test_folder'):
        response = requests.delete(
            url=f'{self.endpoints.DELETE_FOLDER_URL}?path={path}',
            headers=self.headers.get_uploader_headers(self.uploader_token)
        )

        if response.status_code == 404:
            return "404 Folder not found"

        assert response.status_code == 204 or response.status_code == 202, response.status_code
        return response

    def upload_photo_to_folder(self, path, url_file, name):
        params = {"path": f'/{path}/{name}', 'url': url_file, "overwrite": "true"}
        response = requests.post(
            url=self.endpoints.UPLOAD_PHOTO_TO_FOLDER,
            headers=self.headers.get_uploader_headers(self.uploader_token),
            params=params,
        )
        model = UploadPhotoModel(**response.json())
        return model
