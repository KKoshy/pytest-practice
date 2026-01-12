"""
This file holds the practice on using yield for teardown
"""

import pytest
import logging
from lib.email_client import User, Mail, EmailUtilityAdmin

log = logging.getLogger(__name__)

@pytest.fixture
def sender():
    user = EmailUtilityAdmin().create_user("sender_01")
    yield user
    EmailUtilityAdmin().delete_user(user)

@pytest.fixture
def msg():
    return Mail("Welcome", "Hi, how are you?")

@pytest.fixture
def receiver():
    user = EmailUtilityAdmin().create_user("receiver_01")
    yield user
    EmailUtilityAdmin().delete_user(user)

@pytest.fixture
def send_email(sender: User, receiver: User, msg:Mail):
    sender.send_mail(msg, receiver)
    yield sender, receiver
    sender.clear_sent_items()
    receiver.clear_inbox()

def test_yield_values(send_email, msg):
    sender, receiver = send_email
    log.info("Validating yield statements")
    assert msg in sender.sent_items
    assert msg in receiver.inbox
