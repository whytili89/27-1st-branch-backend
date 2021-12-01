import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teambranch.settings")
django.setup()

from users.models import User

CSV_PATH_USERS = 'csv/users.csv'

with open(CSV_PATH_USERS) as in_file:
	data_reader = csv.reader(in_file)
	next(data_reader, None)
	for row in data_reader:
		if row[0]:
			user_name         = row[0]
			user_nickname     = row[1]
			user_email        = row[2]
			user_password     = row[3]
			user_phone_number = row[4]
			print(row[0])
			User.objects.create(
				name         = user_name,
				nickname     = user_nickname,
				email        = user_email,
				password     = user_password,			
				phone_number = user_phone_number
			)
