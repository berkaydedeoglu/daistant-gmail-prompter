import requests
import time
from gmail_extension import utils
from gmail_extension.model.mail import Mail

class GmailClient():
    LIST_MESSAGES_URI = 'users/{}/messages'
    MESSAGE_DETAIL_URI = 'users/{}/messages/{}'

    def __init__(self, config) -> None:
        self.__base_url = config.get('google', 'base_url')
        self.__base_user = config.get('google', 'base_user')
        self.__max_list_result = config.get('google', 'max_list_result')

    def get_unread_emails(self, gmail_access_token: str) -> str:
        messages = []
        messageIds = self.__get_all_message_list(gmail_access_token)
        for message_bundle in messageIds:
            for message_id in message_bundle:
                message_detail = self.__getMessageDetail(message_id, gmail_access_token)
                mail = Mail()
                mail.parse_from_dict(message_detail)
                print(mail.printable_summary)
                messages.append(mail)
                time.sleep(2)

        return messages
    
    def __get_all_message_list(self, token):
        url = self.__generate_message_list_url()
        
        page_token = None
        while page_token != '' :
            res = self.__send_message_list_request(url, token, page_token)
            res = res.json()

            if res['messages'] and len(res['messages']) > 0:
                yield [message['id'] for message in res['messages']]

            page_token = res['nextPageToken'] if res.get('nextPageToken') else ''
    
    def __getMessageDetail(self, id, token):
        url = self.__generate_message_detail_url(id)
        res = self.__send_message_detail_request(url, token)
        return res.json()
    
    def __create_label(self):
        pass

    def __markEmailsAsReadByDaistant(self, message_ids):
        pass

    @utils.successfull_response
    def __send_message_list_request(self, url: str, access_token: str, page_token: str) -> requests.Response:
        header = { 'Authorization': f"Bearer {access_token}" }
        payload = {
            'q': 'is: unread',
            'pageToken': page_token,
            'maxResults': self.__max_list_result,
            'includeSpamTrash': False,
        }

        return requests.get(url, params=payload, headers=header)

    @utils.successfull_response
    def __send_message_detail_request(self, url: str, access_token: str) -> requests.Response:
        header = self.__get_auth_header(access_token)
        return requests.get(url, headers=header)

    def __get_auth_header(self, access_token: str) -> dict:
        return { 'Authorization': f"Bearer {access_token}" }
    
    def __generate_message_list_url(self) -> str:
        uri = self.LIST_MESSAGES_URI.format(self.__base_user)
        return f'{self.__base_url}/{uri}'
    
    def __generate_message_detail_url(self, id: str) -> str:
        uri = self.MESSAGE_DETAIL_URI.format(self.__base_user, id)
        return f'{self.__base_url}/{uri}'
