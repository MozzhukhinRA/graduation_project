from dataclasses import dataclass


@dataclass
class CreditForm:
    header_name_form: str = '._3dCFth'
    field_fio: str = '#card-enerjeans-name'
    field_phone: str = '#card-enerjeans-personalDataMobilePhone'
    field_email: str = '#card-enerjeans-personalDataEmail'
    field_birthday: str = '#card-enerjeans-DOB'
    checkbox_1: str = '#card-enerjeans-agreement'
    checkbox_2: str = '#bloomtech'
    button_continue: str = '.eMFvbP'


selector_credit_form = CreditForm
