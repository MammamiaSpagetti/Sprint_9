import allure


@allure.feature('Аккаунт')
@allure.story('Авторизация')
class TestLogin:
    @allure.title('После входа открывается главная страница и отображается «Выход»')
    def test_login_opens_main_page(self, registered_user, main_page, login_page):
        main_page.open_login()
        login_page.login(registered_user)

        assert main_page.is_opened(), 'После входа не открылась главная страница'
        assert main_page.is_logout_visible(), 'Кнопка «Выход» не отображается'
