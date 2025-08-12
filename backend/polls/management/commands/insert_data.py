from django.core.management import BaseCommand
from faker import Faker



# remember that we must dont change class name(Command) because django cant find command class!!
class Command(BaseCommand):
    help="inserting dummy data to tables"

    def handle(self, *args, **options):
        fake=Faker()
        print(fake.name())
        print(fake.job())
        print(fake.email())

# now just rund this file in terminal ==> python manage.py insert_data
