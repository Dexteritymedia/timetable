from django.core.management.base import BaseCommand
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from app.models import Item
from faker import Faker
import random
from django.utils import timezone
from datetime import timedelta


User = get_user_model()

class Command(BaseCommand):
    help = 'Load 100000 entries into the Item model with at least 50 different users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Check if we already have at least 50 users, otherwise create new ones
        if User.objects.count() < 50:
            self.stdout.write(self.style.NOTICE('Generating 50 users...'))
            for i in range(50):
                User.objects.create_user(
                    username=fake.unique.user_name(),
                    email=fake.email(),
                    password='password123'
                )
        
        # Get a list of all users (ensuring at least 50 are present)
        users = list(User.objects.all()[:50])
        
        self.stdout.write(self.style.NOTICE('Generating 100,000 items...'))
        
        items_to_create = []
        for _ in range(100000):
            user = random.choice(users)
            date = fake.date_between(start_date='-1y', end_date='+1y')
            time = fake.time()
            description = fake.sentence(nb_words=6)

            item = Item(
                user=user,
                date=date,
                time=time,
                description=description
            )
            items_to_create.append(item)

            # Bulk insert every 10,000 items to avoid memory overload
            if len(items_to_create) >= 10000:
                Item.objects.bulk_create(items_to_create)
                items_to_create = []
                self.stdout.write(self.style.SUCCESS(f'{_} items loaded...'))

        # Insert the remaining items
        if items_to_create:
            Item.objects.bulk_create(items_to_create)

        self.stdout.write(self.style.SUCCESS('Successfully loaded 100,000 items!'))
