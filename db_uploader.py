import os
import django
import csv
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teambranch.settings")
django.setup()

from users.models       import User
from keywords.models    import Keyword
from branch_tags.models import UserTag, UsersUserTags, PostingTag, PostingsPostingTags
from postings.models    import Posting

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

from faker           import Faker
from users.models    import User

fake = Faker()

for _ in range(100000):

    email         = fake.unique.email()
    profile_photo = 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/8dd4f6a781571f85eac240b0f31ecfa3.jpeg'
    position_list = ['Backend', 'Frontend', 'Fullstack']

    if not User.objects.filter(email=email).exists():
    
        User.objects.create(
            name          = fake.name(),
            nickname      = fake.first_name(),
            email         = email,
            password      = fake.password(),
            phone_number  = fake.unique.phone_number(),
            github        = fake.email(),
            profile_photo = profile_photo,
            description   = fake.text(),
            position      = random.choice(position_list),
            created_at    = fake.date_time(),
            updated_at    = fake.date_time()
        )

    else:
        print(email)

    usertag_name = fake.first_name()

    if not UserTag.objects.filter(name=usertag_name).exists():
        
        UserTag.objects.create(
            name       = usertag_name,
            created_at = fake.date_time(),
            updated_at = fake.date_time()
        )
    
    else:
        print(usertag_name)
    
for _ in range(20000):
    UsersUserTags.objects.create(
        user_id     = fake.pyint(min_value=7,max_value=100000),
        user_tag_id = fake.pyint(min_value=1,max_value=720)
    )

for _ in range(100000):

    thumbnail = 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg'
    
    Posting.objects.create(
        title        = fake.name(),
        sub_title    = fake.name(),
        content      = fake.text(),
        thumbnail    = thumbnail,
        created_at   = fake.date_time(),
        updated_at   = fake.date_time(),
        keyword_id   = fake.pyint(min_value=1,max_value=19),
        user_id      = fake.pyint(min_value=7,max_value=100000)
    )

    postingtag_name = fake.first_name()

    if not PostingTag.objects.filter(name=postingtag_name).exists():

        PostingTag.objects.create(
            name         = postingtag_name,
            created_at   = fake.date_time(),
            updated_at   = fake.date_time(),
            keyword_id   = fake.pyint(min_value=1,max_value=19)
        )

    else:
        print(postingtag_name)

for _ in range(20000):
    PostingsPostingTags.objects.create(
        posting_id     = fake.pyint(min_value=50,max_value=100000),
        posting_tag_id = fake.pyint(min_value=1,max_value=720)
    )
