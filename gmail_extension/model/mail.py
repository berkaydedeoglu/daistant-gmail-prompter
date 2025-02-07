import base64

class Mail():
    def __init__(self) -> None:
        self.__snippet = None
        self.__to = None
        self.__from = None
        self.__subject = None
        self.__data = None
        self.__date = None

    def parse_from_dict(self, payload: dict) -> None:
        header_keys = ('To', 'From', 'Subject', 'Date')
        header_values = self.__find_in_headers(header_keys, payload['payload']['headers'])

        self.__to = header_values.get('To')
        self.__from = header_values.get('From')
        self.__subject = header_values.get('Subject')
        self.__date = header_values.get('Date')

        self.__snippet = payload['snippet']

        message_payload = payload.get('payload') 
        if message_payload and message_payload.get('body') and message_payload.get('body').get('data'):
            message_body = message_payload.get('body')
            if message_body.get('data'):
                raw_data = message_payload['body']['data']
                try:
                    self.__data = base64.urlsafe_b64decode(raw_data)
                except:
                    print(f'error occured: {raw_data}')
            else:
                print(f'no data available body: {message_body}')

    @property
    def printable_summary(self):
        return f"-----\nFrom: {self.__from}\n{self.__date} | {self.__subject}\n-\n{self.__snippet}\n----"

        
    def __find_in_headers(self, keys: tuple,  headers: list) -> dict:
        values = {}
        for header in headers:
            key = header['name']
            if key in keys: values[key] = header['value']

        return values


