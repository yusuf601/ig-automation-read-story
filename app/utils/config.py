# app/utils/config.py

import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv('INSTAGRAM_BASE_URL', 'https://www.instagram.com')
        self.api_url = os.getenv('INSTAGRAM_API_URL', 'https://i.instagram.com/api/v1/')
        self.user_agent = os.getenv('USER_AGENT', 'Instagram 10.3.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+')
        self.cookie_path = os.getenv('COOKIE_PATH', 'cookies')

    def get_base_url(self):
        return self.base_url

    def get_api_url(self):
        return self.api_url

    def get_user_agent(self):
        return self.user_agent

    def get_cookie_path(self, username):
        return os.path.join(self.cookie_path, f"{username}.json")

    def get_login_url(self):
        return f"{self.api_url}accounts/login/"

    def get_story_url(self):
        return f"{self.api_url}feed/user/"

    # Tambahkan metode lain sesuai kebutuhan