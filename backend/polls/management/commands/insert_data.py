from faker import Faker
import random
from datetime import datetime
from django.core.management import BaseCommand
from blog_module.models import Post,Category
from account_module.models import User,Profile


category_list=[
    "IT","Design","Fun"
]

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

        for name in category_list:
            Category.objects.get_or_create(name=name)
        
        for _ in range(5):
            Post.objects.create(
                author=profile,
                title=self.fake.paragraph(nb_sentences=1),
                content=self.fake.paragraph(nb_sentences=10),
                status=random.choice([True,False]),
                category=Category.objects.get(name=random.choice(category_list)),
                published_date=datetime.now(),
                # image="images/blank.jpg",
            )

# now just rund this file in terminal ==> python manage.py insert_data
