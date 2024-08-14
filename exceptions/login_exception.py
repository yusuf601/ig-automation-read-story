# app/exceptions/login_exception.py

class LoginException(Exception):
    """Exception raised for errors in the login process."""

    def __init__(self, message, status_code=None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        if self.status_code:
            return f"LoginException (Status Code: {self.status_code}): {self.message}"
        return f"LoginException: {self.message}"