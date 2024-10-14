from pydantic import BaseModel, field_validator


class GetSubBreedsListModel(BaseModel):
    message: list
    status: str


@field_validator('status')
def check_success_response_status(cls, value):
    if value != 'success':
        raise ValueError('status must be success')
    else:
        return value