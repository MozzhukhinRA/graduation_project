from dataclasses import dataclass


@dataclass
class MiddlePage:
    selector_switcher_for_all_and_business: str = '._3RMGOJ'
    selector_choice_card: str = '._27xvq3'
    selector_field_phone: str = '#card-prilib-personalDataMobilePhone'
    selector_button_submit: str = '[type="submit"]'
    selector_button_info: str = '._1HcN_l'


selector_found_middel = MiddlePage
