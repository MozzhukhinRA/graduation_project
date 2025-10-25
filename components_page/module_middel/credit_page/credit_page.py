from dataclasses import dataclass


@dataclass
class CardPage:
    selector_header_card_page: str = '._2wSX0Z'
    selector_field_phone: str = '#cash-credit-personalDataMobilePhone'
    selector_information: str = '.YMbfwp-B'
    selector_button_statement: str = '.eMFvbP'


selector_found_credit = CardPage
