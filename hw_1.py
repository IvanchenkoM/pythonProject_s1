'''Условие: Добавить в задание с REST API ещё один тест,
в котором создаётся новый пост, а потом проверяется его наличие
на сервере по полю «описание».

Подсказка: создание поста выполняется запросом к https:
//test-stand.gb.ru/api/posts с передачей параметров title,
description, content.'''
import pytest
from func import get_my_post, create_post

post_check = {'title': 'have', 'description': 'good', 'content': 'day'}


def test_creation_post(login):
    new_post = create_post(login, post_check)['description']
    assert new_post in [item['description'] for item in get_my_post(login)['data']]