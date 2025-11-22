import os
import zipfile

import requests
from jsonschema import validate
from selene import browser

from api_resource.Schemas.schemas_for_api_response import statement_card_schema, search_organizations_schema, \
    exchange_rate_schema, subscription_service_schema
from api_resource.Schemas.schema_for_api_requests import statement_card_schema_request, \
    search_organizations_schema_request, exchange_rate_schema_request, subscription_service_schema_request
from test_bank.utils import attach


class StatementCard:
    def statement_card(self, api_url):
        url = f"{api_url}api/form-core/sessions/2cf31012-524c-4a9f-a56d-794189f429aa/events"
        data = {"action": "next_button"}
        validate(data, statement_card_schema_request)
        response = requests.post(url, data=data)
        assert response.status_code == 201
        validate(response.json(), statement_card_schema)
        attach.add_logs(browser)
        return response


class SearchOrganizations:
    def search_organizations(self, api_url):
        url = f"{api_url}api/dadata/suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/party?"
        params = {'query': '1207700465455'}
        validate(params, search_organizations_schema_request)
        response = requests.get(url, params=params)
        assert response.status_code == 200
        validate(response.json(), search_organizations_schema)
        attach.add_logs(browser)
        return response


class ExchangeRate:
    def exchange_rate(self, api_url):
        url = f"{api_url}api/exchange-rates/ranges?"
        params = {
            'from': 'RUR',
            'to': 'USD',
            'filter[type]': 'online',
            'filter[region]': 78}
        validate(params, exchange_rate_schema_request)
        response = requests.get(url, params=params)
        assert response.status_code == 200
        validate(response.json(), exchange_rate_schema)
        attach.add_logs(browser)
        return response


class SubscriptionService:
    def subscription_service(self, api_url):
        url = f"{api_url}api/faq/list/faq/personal/podpiski?"
        params = {
            'depth': 2,
            'sort': 'sort',
            'filter[content.fields.multiselect]': 'tags,populyarnyi',
            'filter[content.template.name]': 'question'
        }
        validate(params, subscription_service_schema_request)
        response = requests.get(url, params=params)
        assert response.status_code == 200
        validate(response.json(), subscription_service_schema)
        attach.add_logs(browser)
        return response


class DownloadLogo:
    def download_logo(self, url_api):
        url = f"{url_api}api/directory-engine/files/public/retail/uralsib_logo_a6poy414.zip"
        response = requests.get(url)
        zip_path = "downloaded_logo.zip"
        with open(zip_path, 'wb') as f:
            f.write(response.content)

        extract_to = "logos/"
        os.makedirs(extract_to, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        os.remove(zip_path)

        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/zip'
        attach.add_logs(browser)
        return extract_to


method_get_download_logo = DownloadLogo().download_logo
method_get_subscription = SubscriptionService().subscription_service
method_get_rate = ExchangeRate().exchange_rate
method_post_statement_card = StatementCard().statement_card
method_get_search_organizations = SearchOrganizations().search_organizations
