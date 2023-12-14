from typing import Any

from django.contrib.auth.models import User

from profiles.exceptions import PasswordsDontMatchError

class UserService:
    @staticmethod
    def update_user(user: User, data: dict[str, Any]) -> None:

            if tmp := data.get("first_name", None):
                user.first_name = tmp
            if tmp := data.get("last_name", None):
                user.last_name = tmp
            if tmp := data.get("email", None):
                user.email = tmp
            if tmp := data.get("username", None):
                user.username = tmp
            
            if old_pw := data.get("old_password", None):
                if user.check_password(old_pw):
                    new_pw = data.get("new_password", None)
                    user.set_password(new_pw)
                raise PasswordsDontMatchError()

            user.save()
    