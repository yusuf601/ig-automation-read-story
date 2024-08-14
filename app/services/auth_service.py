import json
import os
from app.utils.config import Config
from app.exceptions.login_exception import LoginException

class AuthService:
    def __init__(self, config: Config):
        self.config = config

    def get_username(self):
        return input("[?] Enter Username: ").strip()

    def login(self, username):
        cookie_path = self.config.get_cookie_path(username)

        if os.path.exists(cookie_path):
            print("[!] Saved cookie found! Using cookie mode.")
            return self.login_with_cookie(cookie_path)
        else:
            print("[!] No cookie saved! Using normal mode.")
            return self.login_with_credentials(username, password=self.get_password())  # Include password argument

    def login_with_cookie(self, cookie_path):
        try:
            with open(cookie_path, 'r') as file:
                cookie_data = json.load(file)
            # Implement cookie login logic here
            return {"status": "success", "username": cookie_data.get("username"), "sessionid": cookie_data.get("sessionid")}
        except Exception as e:
            return {"status": "fail", "message": str(e)}

    def login_with_credentials(self, username, password):
        try:
            # Implement credential login logic here
            # For now, let's return a mock successful login
            return {"status": "success", "username": username, "sessionid": "mock_session_id"}
        except Exception as e:
            return {"status": "fail", "message": str(e)}
