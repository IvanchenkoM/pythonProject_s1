import pytest
from func import get_login


@pytest.fixture()
def login():
    return get_login()
