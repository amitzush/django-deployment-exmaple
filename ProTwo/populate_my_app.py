import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

# import random
from appTwo.models import User
from faker import Faker

fakegen = Faker()

# topics = ['Search','Social','Marketplace','News','Games']
#
# def add_topic():
#     t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):
    for entry in range(N):
        # top = add_topic()
        fake_name = fakegen.name().split()

        fake_first_name = fake_name[0]
        fake_second_name = fake_name[1]
        fake_email = fakegen.email()

        usr = User.objects.get_or_create(first_name=fake_first_name,second_name=fake_second_name,email=fake_email)[0]

        # acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
