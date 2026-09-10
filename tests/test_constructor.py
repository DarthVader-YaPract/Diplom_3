import allure


@allure.feature("Конструктор")
class TestConstructor:
    @allure.title("Открытие деталей ингредиента")
    def test_ingredient_card_opens_details(self, constructor_page):
        constructor_page.open_ingredient()
        assert constructor_page.ingredient_details_are_open()

    @allure.title("Закрытие деталей по крестику")
    def test_cross_closes_ingredient_details(self, constructor_page):
        constructor_page.open_ingredient()
        constructor_page.close_ingredient()
        assert constructor_page.ingredient_details_are_closed()

    @allure.title("Увеличение счётчика ингредиента")
    def test_added_sauce_increases_counter(self, constructor_page):
        before = constructor_page.sauce_count()
        after = constructor_page.add_sauce()
        assert after > before
