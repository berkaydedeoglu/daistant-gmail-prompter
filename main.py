import argparse
from gmail_extension.config import Config
from gmail_extension.gmail_client import GmailClient
from gmail_extension.core_client import CoreClient
from gmail_extension.prompt_generator import PromptGenerator

class CLI:
    def __init__(self):
        self.args = self.parse_arguments()
        config_file_path = f'{self.args.root_path}/config.yaml'

        self.config = Config(config_file_path)
        self.gmail_client = GmailClient(self.config)
        self.core_client = CoreClient(self.config, self.args.core_url, self.args.user_id)
        self.prompt_generator = PromptGenerator(self.config)

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Gmail Prompter")
        parser.add_argument("--core_url", help="Core Api URL")
        parser.add_argument("--root_path", help="Root path of extension from running path")
        parser.add_argument("--user_id", help="Daistant user id" )

        return parser.parse_args()

    def run(self):
        gmail_access_token = self.core_client.get_access_token()
        print("gmail_access_token: ", gmail_access_token)
        unread_emails = self.gmail_client.get_unread_emails(gmail_access_token)
        print(unread_emails)
        prompt = self.prompt_generator.generate_prompt(unread_emails)

        self.core_client.send_prompt(prompt)

if __name__ == "__main__":
    cli = CLI()
    cli.run()