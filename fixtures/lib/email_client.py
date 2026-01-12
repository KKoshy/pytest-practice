"""
Provides a minimal Email Client for testing
"""

import logging

log = logging.getLogger(__name__)

class EmailUtilityAdmin:
    users = []

    @classmethod
    def create_user(cls, user_name):
        cls.list_users()
        log.info(f"Creating user {user_name}")
        user = User(user_name)
        cls.users.append(user)
        cls.list_users()
        return user
    
    @classmethod
    def list_users(cls):
        log.info(f"Users include: {cls.users}")

    @classmethod
    def delete_user(cls, user: User):
        cls.list_users()
        log.info(f"Deleting user {user.user_name}")
        cls.users.remove(user)
        cls.list_users()


class User:
    def __init__(self, user_name) -> None:
        self.user_name = user_name
        self.inbox = []
        self.sent_items = []

    def send_mail(self, msg:Mail, other: User):
        log.info(f"Sending email to {other.user_name}")
        other.inbox.append(msg)
        self.sent_items.append(msg)

    def clear_inbox(self):
        log.info("Clearing inbox")
        self.inbox.clear()

    def clear_sent_items(self):
        log.info("Clearing sent items")
        self.sent_items.clear()


class Mail:
    def __init__(self, subject, body) -> None:
        self.subject = subject
        self.body = body
