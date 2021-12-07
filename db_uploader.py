# import os
# import django
# import csv
# import sys

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teambranch.settings")
# django.setup()

# from django.db import trasaction

# from users.models import User
# from keywords.models import Keyword
# from branch_tags.models import PostingTag, UserTag
# from postings.models import Posting

# from faker import Faker
# fake = Faker()

# for _ in range(300):
#     try:
#         User.objects.create(
#             name          = fake.name(),
#             nickname      = fake.first_name(),
#             email         = fake.email(),
#             password      = fake.password(),
#             phone_number  = fake.phone_number(),
#             position      = fake.color_name()
#             )
#     except Exception:
#         continue        

#     #     Posting.objects.create(
#     #         title = fake.address(),
#     #         sub_title = fake.company(),
#     #         content = fake.paragraph(),
#     #         thumbnail = fake.image_url(),
#     #         created_at = fake.date(),
#     #         updated_at = fake.date(),
#     #         user_id = fake.pyint(min_value=1, max_value=100000),
#     #         keyword_id = fake.pyint(min_value=1, max_value=30)

#     #     )

#     #     Keyword.objects.create(
#     #         name = fake.language_name()
#     #     )

#     #     PostingTag.objects.create(
#     #         name = fake.job(),
#     #         keyword_id = fake.pyint(min_value=1, max_value=30),
#     #         created_at = fake.date_time(),
#     #         updated_at = fake.date_time()
#     #     )

#     #     UserTag.objects.create(
#     #         name  = fake.job(),
#     #         users = fake.pying(min_value=1, max_value=100000)
#     #     )

    
import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teambranch.settings")
django.setup()

from users.models import User
from keywords.models import Keyword
from branch_tags.models import PostingTag, UserTag
from postings.models import Posting

CSV_PATH_USERS         = "csv/users.csv"
CSV_PATH_KEYWORDS      = "csv/keyword_fake_data.csv"
CSV_PATH_POSTINGS      = "csv/posting_fake.csv"
CSV_PATH_PORSTING_TAGS = "csv/posting_tag_fake_data.csv"
CSV_PATH_USER_TAGS     = "csv/user_tag_fake_data.csv"

if not User.objects.all() :
    with open(CSV_PATH_USERS) as (in_file) : 
        data_reader = csv.reader(in_file)

        next(data_reader, None)
        for row in data_reader :
            User.objects.create(
                name         = row[0],
                nickname     = row[1],
                email        = row[2],
                password     = row[3],
                phone_number = row[4]
            )

if not Keyword.objects.all() :
    with open(CSV_PATH_KEYWORDS) as (in_file) : 
        data_reader = csv.reader(in_file)
        
        next(data_reader, None)
        for row in data_reader :
            Keyword.objects.create(
                name = row[0]
            )

if not PostingTag.objects.all():
    with open(CSV_PATH_PORSTING_TAGS) as (in_file) : 
        data_reader = csv.reader(in_file)

        next(data_reader, None)
        for row in data_reader :
            PostingTag.objects.create(
                name       = row[0],
                keyword_id = row[1]
            )

if not UserTag.objects.all() :
    with open(CSV_PATH_USER_TAGS) as (in_file) : 
        data_reader = csv.reader(in_file)

        next(data_reader, None)
        for row in data_reader :
            UserTag.objects.create(
                name = row[0]
            )

if not Posting.objects.all() :
    with open(CSV_PATH_POSTINGS) as (in_file) : 
        data_reader = csv.reader(in_file)

        next(data_reader, None)
        for row in data_reader :
            Posting.objects.create(
                title      = row[0],
                sub_title  = row[1],
                content    = row[2],
                thumbnail  = row[3],
                user_id    = row[4],
                keyword_id = row[5]
            )
