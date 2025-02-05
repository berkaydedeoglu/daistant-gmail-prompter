import argparse
from .config import Config
from .gmail_client import GmailClient
from .core_client import CoreClient
from .prompt_generator import PromptGenerator

class CLI:
    def __init__(self):
        args = self.parse_arguments()
        config_file_path = f'{args.root_path}/config.yaml'

        self.config = Config(config_file_path)
        self.config.load_from_yaml()
        self.gmail_client = GmailClient(self.config)
        self.core_client = CoreClient(self.config)
        self.prompt_generator = PromptGenerator(self.config)

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Gmail Prompter")
        parser.add_argument("--core_url", help="Core Api URL")
        parser.add_argument("--root_path", help="Root path of extension from running path")

        return parser.parse_args()

    def run(self):
        gmail_access_token = self.core_client.get_access_token()
        unread_emails = self.gmail_client.get_unread_emails(gmail_access_token)
        prompt = self.prompt_generator.generate_prompt(unread_emails)

        self.core_client.send_prompt(prompt)

if __name__ == "__main__":
    cli = CLI()
    cli.run()