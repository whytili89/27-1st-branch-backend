import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teambranch.settings")
django.setup()

from users.models import User
from keywords.models import Keyword
from branch_tags.models import PostingTag, UserTag
from postings.models import Posting

CSV_PATH_USERS         = "csv/users.csv"
CSV_PATH_KEYWORDS      = "csv/keywords.csv"
CSV_PATH_POSTINGS      = "csv/postings.csv"
CSV_PATH_PORSTING_TAGS = "csv/posting_tags.csv"
CSV_PATH_USER_TAGS     = "csv/user_tags.csv"

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

# from faker           import Faker
# from users.models    import User
# from django.db       import transaction, DatabaseError

# fake = Faker()

# for _ in range(100000):
#     try:
#         User.objects.create(
#             name         = fake.name(),
#             nickname     = fake.first_name(),
#             email        = fake.unique.email(),
#             password     = fake.password(),
#             phone_number = fake.unique.phone_number()
#         )

#     except Exception:
#         continue


# for _ in range(100000):
#     try:
#         Posting.objects.create(
#             title         = fake.name(),
#             sub_title     = fake.address(),
#             content       = fake.text(),
#             thumbnail     = fake.image_url(),
#             user_id       = fake.pyint(min_value=1,max_value=100000),
#             keyword_id    = fake.pyint(min_value=1,max_value=19),
#             created_at    = fake.date_time(),
#             updated_at    = fake.date_time()
#         )

#     except Exception:
#         continue


# for _ in range(10):
#     try:
#         PostingTag.objects.create(
#             name         = fake.unique.first_name(),
#             created_at   = fake.date_time(),
#             updated_at   = fake.date_time(),
#             keyword_id   = fake.pyint(min_value=1,max_value=19)
#         )
    
#     except Exception:
#         continue


# count = 0
# for _ in range(10):
    

#     name = fake.name()
#     if not UserTag.objects.filter(name=name).exists():
    
#         UserTag.objects.create(
#             name         = name,
#             created_at   = fake.date_time(),
#             updated_at   = fake.date_time()
#         )
#         count = count +1

#     else:
#         print(name)
    

# print(count)