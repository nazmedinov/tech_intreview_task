import pytest

from api_collection.dogs.api_dogs import ApiDogs
from api_collection.image_uploader.api_uploader import APIUploader


@pytest.fixture
def breed_path(request):
    api_uploader = APIUploader()
    try:
        api_uploader.delete_folder(request.param)
    except AssertionError:
        assert api_uploader.delete_folder(request.param) == '404 Folder not found'
    yield request.param
    api_uploader.delete_folder(request.param)
