import allure


@allure.feature('Рецепты')
@allure.story('Создание рецепта')
class TestCreateRecipe:
    @allure.title('Созданный рецепт отображается с указанным названием')
    def test_create_recipe_shows_card_and_name(
        self, authenticated_main_page, create_recipe_page, recipe_page, recipe_data,
    ):
        authenticated_main_page.open_recipe_creation()
        create_recipe_page.create_recipe(recipe_data)

        assert recipe_page.is_card_visible(), 'Карточка созданного рецепта не отображается'
        assert recipe_page.get_name() == recipe_data['name'], 'Название рецепта не совпадает'
