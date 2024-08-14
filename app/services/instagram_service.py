# app/services/instagram_service.py

import time
from app.utils.config import Config
from app.services.auth_service import AuthService
from app.exceptions.story_view_exception import StoryViewException

class InstagramService:
    def __init__(self, config: Config, auth_service: AuthService):
        self.config = config
        self.auth_service = auth_service

    def show_banner(self):
        # Implement banner display logic
        return "Instagram Story Viewer"

    def get_target_usernames(self):
        input_str = input("[?] Enter Username Target(s) (Multiple use | without @ symbol): ").strip()
        return input_str.split('|')

    def get_sleep_seconds(self):
        return int(input("[?] Enter Sleep second(s): ").strip())

    def find_profile(self, username, login_data):
        # Implement profile search logic
        # Return profile data
        pass

    def view_stories_for_user(self, user_id, login_data, sleep_seconds):
        story_views = 0
        end_cursor = None

        while True:
            stories = self.get_stories(user_id, login_data, end_cursor)
            for story in stories['data']:
                story_views += self.view_story(story, login_data)
                time.sleep(sleep_seconds)
            end_cursor = stories['end_cursor']
            if not end_cursor:
                break

        return story_views

    def get_stories(self, user_id, login_data, end_cursor=None):
        # Implement story fetching logic
        # Return stories data and end_cursor
        pass

    def view_story(self, story, login_data):
        # Implement story viewing logic
        # Return 1 if successful, 0 otherwise
        pass