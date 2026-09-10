import allure


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Изменение общего счётчика")
    def test_completed_order_changes_total_count(
        self, signed_in_constructor, feed
    ):
        feed.open()
        before = feed.total_count()
        feed.go_to_constructor().create_order()
        feed.open()
        after = feed.wait_total_increase(before)
        assert after > before

    @allure.title("Изменение сегодняшнего счётчика")
    def test_completed_order_changes_today_count(
        self, signed_in_constructor, feed
    ):
        feed.open()
        before = feed.today_count()
        feed.go_to_constructor().create_order()
        feed.open()
        after = feed.wait_today_increase(before)
        assert after > before

    @allure.title("Заказ появляется в работе")
    def test_completed_order_appears_in_progress(
        self, signed_in_constructor, feed
    ):
        order_number = signed_in_constructor.create_order()
        feed.open()
        assert feed.order_appears_in_progress(order_number)
