from django.core.management.base import BaseCommand
from app.models import *
from django.db.models import F
from random import choice, shuffle, seed
from faker import Faker
from faker.providers.lorem import Provider



fake = Faker()


class Command(BaseCommand):

    test_avatars = ['ava_test1.jpg', 'ava_test2.jpg', 'ava_test3.jpg', 'ava_test4.jpg', 'ava_test5.jpg']

    def add_arguments(self, parser):
        parser.add_argument('--db_size', default='small', type=str, help='The size of database data to create.')

    def fill_profiles(self, cnt):
        usernames = set()
        profiles = []
        for i in range(cnt):
            username = fake.simple_profile().get('username')
            while username in usernames:
                username = fake.simple_profile().get('username')
            user = User.objects.create(
                username=username,
                password=fake.password(length=10, special_chars=True)
            )
            profiles.append(Profile(
                user_id=user.id,
                avatar=choice(self.test_avatars)
            ))
            usernames.add(username)

        


    def handle(self, *args, **options):
        sizes = [100, 100, 100, 100, 100, 100]
        # sizes = [10000, 10000, 100000, 1000000, 1000000, 1000000]

        self.fill_profiles(sizes[0])
        self.stdout.write("Профили заполнены")