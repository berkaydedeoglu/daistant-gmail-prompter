from gmail_extension.config import Config
import requests

class CoreClient():
    ACCESS_TOKEN_URI = '{}/third-party/google/access-token'

    def __init__(self, config: Config, core_client_uri: str, user_id: int) -> None:
        self.__config = config
        self.__base_url = core_client_uri
        self.__user_id = user_id

    def send_prompt(self, prompt: str) -> None:
        print('sending prompt')

    def get_access_token(self) -> str:
        url = self.ACCESS_TOKEN_URI.format(self.__base_url)

        res = requests.get(url)
        if res.status_code != 200:
            raise Exception('Cannot get access token')
        
        json_res = res.json()
        token = json_res.get('access_token')
        if not token:
            raise Exception('Malformat core output on fetching access token')
        
        return token