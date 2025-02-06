import requests
from gmail_extension import utils

class GmailClient():
    LIST_MESSAGES_URI = 'users/{}/messages'
    def __init__(self, config) -> None:
        self.__base_url = config.get('google', 'base_url')
        self.__base_user = config.get('google', 'base_user')
        self.__max_list_result = config.get('google', 'max_list_result')

    def get_unread_emails(self, gmail_access_token: str) -> str:
        print('getting unread emails')
        return ''
    
    def __sendRequest(self, page_token: int = 0):
        url = self.__generate_url()
        payload = {
            'q': 'is: unread',
            'pageToken': page_token,
            'maxResults': self.__max_list_result,
            'includeSpamTrash': False,
        }

        res = requests.get(url, params=payload)



    def __generate_url(self):
        uri = self.LIST_MESSAGES_URI.format(self.__base_user)
        return f'{self.__base_url}/{uri}'
    
    def __create_label(self):
        pass

    def __markEmailsAsReadByDaistant(self, message_ids):
        pass


    @utils.successfull_response
    def __defMakeApiRequest(self):
        pass

