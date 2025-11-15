import os
import zipfile

import requests


class StatementCard:
    def statement_card(self, api_url):
        url = f"{api_url}api/form-core/sessions/2cf31012-524c-4a9f-a56d-794189f429aa/events"
        response = requests.post(url, data={
            "action": "next_button"
        })
        assert response.status_code == 201
        return response


class SearchOrganizations:
    def search_organizations(self, api_url):
        url = f"{api_url}api/dadata/suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/party?"
        response = requests.get(url, params={
            'query': '1207700465455'
        })
        assert response.status_code == 200
        return response


class ExchangeRate:
    def exchange_rate(self, api_url):
        url = f"{api_url}api/exchange-rates/ranges?"
        response = requests.get(url, params={
            'from': 'RUR',
            'to': 'USD',
            'filter[type]': 'online',
            'filter[region]': 78})
        assert response.status_code == 200
        return response


class SubscriptionService:
    def subscription_service(self, api_url):
        url = f"{api_url}api/faq/list/faq/personal/podpiski?"
        response = requests.get(url, params={
            'depth': 2,
            'sort': 'sort',
            'filter[content.fields.multiselect]': 'tags,populyarnyi',
            'filter[content.template.name]': 'question'
        })
        assert response.status_code == 200
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

        return extract_to


method_get_download_logo = DownloadLogo().download_logo
method_get_subscription = SubscriptionService().subscription_service
method_get_rate = ExchangeRate().exchange_rate
method_post_statement_card = StatementCard().statement_card
method_get_search_organizations = SearchOrganizations().search_organizations
