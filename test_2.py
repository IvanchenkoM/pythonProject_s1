import pytest
from func import get_post

id_check = 93220


def test_1(login):
    output = get_post(login)['data']
    res = []
    for item in output:
        res.append(item['id'])
    assert id_check in res