import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teambranch.settings")
django.setup()

from django.db import trasaction

from users.models import User
from keywords.models import Keyword
from branch_tags.models import PostingTag, UserTag
from postings.models import Posting

from faker import Faker
fake = Faker()

for _ in range(300):
    try:
        User.objects.create(
            name          = fake.name(),
            nickname      = fake.first_name(),
            email         = fake.email(),
            password      = fake.password(),
            phone_number  = fake.phone_number(),
            position      = fake.color_name()
            )
    except Exception:
        continue        

    #     Posting.objects.create(
    #         title = fake.address(),
    #         sub_title = fake.company(),
    #         content = fake.paragraph(),
    #         thumbnail = fake.image_url(),
    #         created_at = fake.date(),
    #         updated_at = fake.date(),
    #         user_id = fake.pyint(min_value=1, max_value=100000),
    #         keyword_id = fake.pyint(min_value=1, max_value=30)

    #     )

    #     Keyword.objects.create(
    #         name = fake.language_name()
    #     )

    #     PostingTag.objects.create(
    #         name = fake.job(),
    #         keyword_id = fake.pyint(min_value=1, max_value=30),
    #         created_at = fake.date_time(),
    #         updated_at = fake.date_time()
    #     )

    #     UserTag.objects.create(
    #         name  = fake.job(),
    #         users = fake.pying(min_value=1, max_value=100000)
    #     )
