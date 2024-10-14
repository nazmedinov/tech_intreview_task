class Headers:
    BASIC_HEADERS = {'Content-Type': 'application/json'}

    @staticmethod
    def get_uploader_headers(token):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        return headers
