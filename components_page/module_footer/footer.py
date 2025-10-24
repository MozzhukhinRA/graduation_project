from dataclasses import dataclass


@dataclass
class FooterPage:
    selector_need_panel: str = '._3YCDpD'
    selector_currency_button: str = '._1IfTSS'
    selector_choice_button_in_footer: str = '._1V_ZYn'
    selector_currency: str = '._1AHtbn'


selector_found_footer = FooterPage
