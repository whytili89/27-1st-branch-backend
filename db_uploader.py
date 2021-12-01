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

        

