class PromptGenerator():
    def __init__(self, config) -> None:
        self.__config = config

    def generate_prompt(self, unread_emails) -> str:
        print('generating prompt')