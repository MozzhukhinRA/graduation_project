from dataclasses import dataclass


@dataclass
class HeaderPage:
    selector_left_upper_button: str = '._1z8ijz'
    selector_main_banner: str = '._1IXIUV'
    selector_login_button: str = '._10dgoN'
    selector_left_arrow: str = '._2anr5z'
    selector_right_arrow: str = '._3X3voY'
    selector_middel_button: str = '._3Lc2Gk .Ru_cnP'


selector_found_header = HeaderPage
