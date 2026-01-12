"""
This file holds the practice on using request.addfinalizer() for teardown
"""

import pytest
import logging
from lib.email_client import EmailUtilityAdmin, User, Mail


log = logging.getLogger(__name__)


@pytest.fixture
def sender(request):
    admin = EmailUtilityAdmin()
    user = admin.create_user("sender_01")

    def delete_user():
        admin.delete_user(user)

    request.addfinalizer(delete_user)
    return user
    

@pytest.fixture
def receiver(request):
    admin = EmailUtilityAdmin()
    user = admin.create_user("receiver_01")

    def delete_user():
        admin.delete_user(user)

    request.addfinalizer(delete_user)
    return user

@pytest.fixture
def msg():
    return Mail("Welcome", "Hi, how are you?")

@pytest.fixture
def send_mail(request, sender, receiver, msg):
    sender.send_mail(msg, receiver)

    def clear_up():
        sender.clear_sent_items()
        receiver.clear_inbox()

    request.addfinalizer(clear_up)
    return sender, receiver


def test_add_finalizer(send_mail, msg):
    log.info("Validating add finalizer")
    sender, receiver = send_mail
    assert msg in sender.sent_items
    assert msg in receiver.inbox


