# main.py

import os
from dotenv import load_dotenv
from app.services.instagram_service import InstagramService
from app.services.auth_service import AuthService
from app.utils.config import Config
from app.exceptions.login_exception import LoginException
from app.exceptions.story_view_exception import StoryViewException

def main():
    try:
        load_dotenv()
        config = Config()
        auth_service = AuthService(config)
        instagram_service = InstagramService(config, auth_service)

        print(instagram_service.show_banner())
        print()

        username = auth_service.get_username()
        login_data = auth_service.login(username)

        if login_data['status'] != 'success':
            raise LoginException("Failed to login")

        print(f"[*] Login as {login_data['username']} successful!")
        print()

        target_usernames = instagram_service.get_target_usernames()
        sleep_seconds = instagram_service.get_sleep_seconds()

        for target_username in target_usernames:
            try:
                target_info = instagram_service.find_profile(target_username, login_data)
                if target_info['status'] != 'success':
                    raise Exception("Failed to find profile or profile is private")

                print(f"[*] Target: @{target_info['username']} | Name: {target_info['fullname']} | "
                      f"Followers: {target_info['followers']} | Following: {target_info['following']} | "
                      f"Posts: {target_info['post']}")
                print()

                story_views = instagram_service.view_stories_for_user(target_info['id'], login_data, sleep_seconds)
                print(f"[+] Successfully viewed {story_views} stories for @{target_username}")
            except StoryViewException as e:
                print(f"[!] Error viewing stories for @{target_username}: {str(e)}")
            except Exception as e:
                print(f"[*] Error processing @{target_username}: {str(e)}")

    except LoginException as e:
        print(f"[*] Login failed: {str(e)}")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
