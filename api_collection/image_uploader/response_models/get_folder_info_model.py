from pydantic import BaseModel, field_validator


class ItemsOfFolderModel(BaseModel):
    sort: str
    items: list
    limit: int
    offset: int
    path: str
    total: int


class GetFolderInfoModel(BaseModel):
    _embedded: ItemsOfFolderModel
    name: str
    exif: dict
    resource_id: str
    created: str
    modified: str
    path: str
    comment_ids: dict
    type: str
    revision: int


@field_validator('type')
def check_that_type_is_dir(cls, value):
    if value != 'dir':
        raise ValueError('type of folder must be "dir"')
    return value
