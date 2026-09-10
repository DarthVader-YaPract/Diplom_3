from uuid import uuid4

import allure
import pytest

from api.user_api import UserApi


def new_account_payload():
    marker = uuid4().hex
    return {
        "email": f"qa_ui_{marker}@example.com",
        "password": f"QAtest_{marker}",
        "name": f"User_{marker[:8]}",
    }


@allure.step("Подготовить тестового пользователя")
def provision_account():
    account = new_account_payload()
    registration = UserApi.register(account)
    if registration.status_code != 200:
        pytest.fail(
            f"Не удалось создать UI-пользователя: "
            f"{registration.status_code} {registration.text}"
        )
    return {**account, **registration.json()}


@allure.step("Удалить тестового пользователя")
def remove_account(account):
    token = account.get("accessToken")
    if token:
        UserApi.delete(token)
