from dataclasses import dataclass


@dataclass
class CreditForm:
    field_fio : 'str' = '#card-enerjeans-name'


selector_credit_form = CreditForm