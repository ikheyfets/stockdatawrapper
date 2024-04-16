import requests
import json

class EndpointsManager:
    def __init__(self) -> None:
        pass


class Endpoint:
    def __init__(self, type, **kwargs):
        self.type = type
        self.url = None
        self.is_valid = False
        self.parameters = kwargs['kwargs']


    def call(self) -> json:
        if self.is_valid:
            response = requests.get(url=self.url)
            return json.loads(response.content)
        else:
            raise Exception(f'Your call validation has failed.')