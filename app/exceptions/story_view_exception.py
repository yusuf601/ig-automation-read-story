# app/exceptions/story_view_exception.py

class StoryViewException(Exception):
    """Exception raised for errors in the story viewing process."""

    def __init__(self, message, status_code=None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        if self.status_code:
            return f"StoryViewException (Status Code: {self.status_code}): {self.message}"
        return f"StoryViewException: {self.message}"