'''Задание 2
Написать тест с использованием pytest и requests, в котором:
● Адрес сайта, имя пользователя и пароль хранятся в config.yaml
● conftest.py содержит фикстуру авторизации по адресу
https://test-stand.gb.ru/gateway/login с передачей параметров
“username" и "password" и возвращающей токен авторизации
● Тест с использованием DDT проверяет наличие поста
с определенным заголовком в списке постов другого
пользователя, для этого выполняется get запрос по адресу
https://test-stand.gb.ru/api/posts c хедером, содержащим токен
авторизации в параметре "X-Auth-Token". Для отображения
постов другого пользователя передается "owner": "notMe".'''
import yaml
import requests

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_login():
    path = data['path']
    post = requests.post(url=path, data={'username': data['username'], 'password': data['password']})
    if post.status_code == 200:
        return post.json()['token']


def get_post(token):
    path = data['path_post']
    get = requests.get(url=path, params={"owner": "notMe"}, headers={"X-Auth-Token": token})
    if get.status_code == 200:
        return get.json()


def get_my_post(token):
    path = data['path_post']
    get = requests.get(url=path, params={"owner": "Me"}, headers={"X-Auth-Token": token})
    if get.status_code == 200:
        return get.json()


def create_post(token, post_param: dict[str, str]):
    path = data['path_post']
    response = requests.post(
        url=path,
        params=post_param,
        headers={"X-Auth-Token": token}
    )
    if response.status_code == 200:
        return response.json()


if __name__ == '__main__':
    token = get_login()
    print(get_post(token))
    print(get_my_post(token))
    print(create_post(token, {'title': 'have', 'description': 'good', 'content': 'day'}))