from faker import Faker
fake=Faker('IN')
for i in range(200):
    print(fake.first_name_female())