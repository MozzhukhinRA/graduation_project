import allure

from api_resource.api_methods import method_post_statement_card, method_get_search_organizations, method_get_rate, \
    method_get_subscription, method_get_download_logo


class TestMethodStatementCreditCard:
    @allure.epic("Кредитные продукты")
    @allure.feature("Отправка заявления на кредитную карту")
    @allure.story("POST")
    @allure.tag('api', 'credit_card', 'positive', 'regress')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_statement_card(self, api_url):
        with allure.step('Отправка заявления методом POST, Код = 201'):
            method_post_statement_card(api_url)


class TestMethodSearchOrganizations:
    @allure.epic("Организации")
    @allure.feature("Поиск организации по инн")
    @allure.story("GET")
    @allure.tag('api', 'inn_organization', 'positive', 'regress')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_search_organizations(self, api_url):
        with allure.step('Отправляем ИНН организации на проверку, организация найдена. Код = 200'):
            method_get_search_organizations(api_url)


class TestMethodExchangeRate:
    @allure.epic("Валюта")
    @allure.feature("Получение курса валют")
    @allure.story("GET")
    @allure.tag('api', 'rate', 'positive', 'regress')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_exchange_rate(self, api_url):
        with allure.step('Отправляем запрос на получениек курса валют. Код = 200'):
            method_get_rate(api_url)


class TestMethodSubscriptionService:
    @allure.epic("Подписки")
    @allure.feature("Подписки на предоставляемые сервисы")
    @allure.story("GET")
    @allure.tag('api', 'subscriptions', 'positive', 'regress')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subscription_service(self, api_url):
        with allure.step('Отправляем запрос на получение списка доступных подписок. Код = 200'):
            method_get_subscription(api_url)


class TestMethodConfirmationPhone:
    @allure.epic("УралСиб логотип")
    @allure.feature("Скачиваем zip файл с логотипом банка")
    @allure.story("GET")
    @allure.tag('api', 'logo', 'positive', 'regress')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_download_logo(self, api_url):
        with allure.step('Отправляем запрос на загрузку zip архива. Код = 200'):
            method_get_download_logo(api_url)
