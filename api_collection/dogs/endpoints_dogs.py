class EndpointsDogs:
    SUB_BREEDS_LIST_URL = lambda self, breed: f'https://dog.ceo/api/breed/{breed}/list'
    SUB_BREED_IMAGE_LINK_URL = lambda self, breed, sub_breed: f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random"
    BREED_IMAGE_LINK_URL = lambda self, breed: f"https://dog.ceo/api/breed/{breed}/images/random"
