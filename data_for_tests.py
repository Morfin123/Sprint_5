import random


class TestAccount:
    user_email = f"test123@test.test"
    user_password = f"test123456"


class TestRandomAccount:
    user_name = f"Пользователь{random.randint(1000, 9999)}"
    user_email = f"brykov_maksim_3_{random.randint(100, 999)}@yandex.ru"
    password = f"test{random.randint(1000, 9999)}"
    bad_password = f"test{random.randint(1, 9)}"
