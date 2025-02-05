import argparse
from .config import Config
from .gmail_client import GmailClient
from .core_client import CoreClient
from .prompt_generator import PromptGenerator

class CLI:
    def __init__(self):
        self.config = Config()
        self.gmail_client = GmailClient(self.config)
        self.core_client = CoreClient(self.config)
        self.prompt_generator = PromptGenerator(self.config)

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Gmail Prompter")
        parser.add_argument("--core_url", help="Core Api URL")

        return parser.parse_args()

    def run(self):
        args = self.parse_arguments()
        self.core_client.set_core_url(args.core_url)

        gmailAccessToken = self.core_client.get_access_token()
        unreadEmails = self.gmail_client.get_unread_emails(gmailAccessToken)
        prompt = self.prompt_generator.generate_prompt(unreadEmails)
        self.core_client.send_prompt(prompt)

if __name__ == "__main__":
    cli = CLI()
    cli.run()