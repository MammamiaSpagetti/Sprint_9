import allure


@allure.feature('Аккаунт')
@allure.story('Создание аккаунта')
class TestRegistration:
    @allure.title('После регистрации открывается страница с формой авторизации')
    def test_registration_redirects_to_login(
        self, registration_user, main_page, registration_page, login_page,
    ):
        main_page.open_registration()
        registration_page.register(registration_user)

        assert login_page.is_opened(), 'После регистрации не открылась страница авторизации'
        assert login_page.is_form_visible(), 'Форма авторизации не отображается'
