from pydantic import BaseModel


class UploadPhotoModel(BaseModel):
    href: str
    method: str
    templated: bool