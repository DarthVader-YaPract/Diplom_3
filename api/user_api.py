import allure
import requests

from urls import Urls


class UserApi:
    TIMEOUT = 50

    @staticmethod
    @allure.step("Создать пользователя через API")
    def register(user_data):
        return requests.post(
            Urls.REGISTER,
            json=user_data,
            timeout=UserApi.TIMEOUT,
        )

    @staticmethod
    @allure.step("Удалить пользователя через API")
    def delete(access_token):
        return requests.delete(
            Urls.USER,
            headers={"Authorization": access_token},
            timeout=UserApi.TIMEOUT,
        )
