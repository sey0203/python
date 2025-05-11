from faker import Faker
from faker.providers import BaseProvider
import random

fake = Faker('ko_KR')

print(fake.name())
print(fake.address())
print(fake.currency_code())
print(fake.currency_name())
print(fake.bank())

class BankProvider(BaseProvider):
    BANKS = [
        "KB국민은행", "신한은행", "우리은행", "하나은행", "기업은행", "농협은행"
    ]

    def bank(self):
        return random.choice(self.BANKS)
    
if hasattr(fake, "add_provider"):
    fake.add_provider(BankProvider)
    print(fake.bank())