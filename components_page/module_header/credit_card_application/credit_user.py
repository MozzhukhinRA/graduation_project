from faker.proxy import Faker


def user_test_reg():
    fake = Faker('ru_RU')
    birth = fake.date_of_birth(minimum_age=18, maximum_age=74)
    user_data = {
        'last_name': fake.last_name(),
        'first_name': fake.first_name(),
        'middel_name': fake.middle_name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'birth': birth.strftime("%d.%m.%Y")
    }
    return user_data
