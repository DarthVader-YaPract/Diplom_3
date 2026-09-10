import allure


@allure.feature("Навигация")
class TestNavigation:
    @allure.title("Переход в конструктор")
    def test_constructor_link_opens_main_page(self, feed_page):
        page = feed_page.go_to_constructor()
        assert page.is_open()

    @allure.title("Переход в ленту заказов")
    def test_order_feed_link_opens_feed(self, constructor_page):
        page = constructor_page.go_to_feed()
        assert page.is_open()
