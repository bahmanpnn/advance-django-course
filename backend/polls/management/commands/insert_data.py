from django.core.management import BaseCommand
from faker import Faker
from account_module.models import User,Profile



# remember that we must dont change class name(Command) because django cant find command class!!
class Command(BaseCommand):
    help="inserting dummy data to tables"

    def __init__(self,*args, **kwargs):
        super(Command,self).__init__(*args, **kwargs)
        self.fake=Faker() # we do this because just need one object from Faker not many but this Object can every time give us random data for everything!!

    def handle(self, *args, **options):
        user=User.objects.create_user(email=self.fake.email(),password="Test12345!@")
        profile=Profile.objects.get(user=user)
        profile.first_name=self.fake.first_name()
        profile.last_name=self.fake.last_name()
        profile.description=self.fake.paragraph(nb_sentences=5)
        profile.save()

# now just rund this file in terminal ==> python manage.py insert_data
