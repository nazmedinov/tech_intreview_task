from pydantic import BaseModel, model_validator


class CreateFolderModel(BaseModel):
    href: str
    method: str
    templated: bool


@model_validator(mode='after')
def check_field_not_empty(cls, values):
    for value in values:
        if value is None or value == '':
            raise ValueError('Field cannot be empty')
    return values
