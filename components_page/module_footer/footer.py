from dataclasses import dataclass


@dataclass
class FooterPage:
    selector_header_footer: str = '._3VI9Tl'
    selector_payments_and_transfers: str = '._3W6qqE'
    selector_info_banner: str = '._3uq7CK'
    selector_payment: str = '._3lVduv'


selector_found_footer = FooterPage
