from faker import Faker
fake = Faker()
class SBurgersTestData:
    REGISTRATION_NAME = "Alex"
    REGISTRATION_EMAIL = fake.email()
    AUTHARIZATION_EMAIL = "AlexanderDneprov7016@yandex.ru"
    REGISTRATION_PASSWORD_6_NUMBERS = "123456"
    REGISTRATION_PASSWORD_5_NUMBERS = "12345"