#!/usr/bin/evn python3
import csv
import requests
import json
import sys

# Extracting users from CSV for time being
#userdb="/Users/vincesesto/NewStrava/users1.csv"
userdb="scripts/users1.csv"
api_token=sys.argv[1]
api_url_base='https://www.strava.com'

def get_userdata_from_db():
	with open(userdb) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			name=row['name']
			id=row['strava_id']
			user_key=row['strava_users_key']
			activity_bearer=row['latest_bearer']
			print(name, id, user_key, activity_bearer)


def update_activity_bearer(user_id):
	# Function accepts the strava id
	print("Obtaining New Activity Bearer")
	import stravalib
	client = stravalib.client.Client()
	access_token = client.exchange_code_for_token(client_id=31940,client_secret='6769ae72996e05a36ac38d546871dd63982b2651',code='f53de2ed2a5d40b3814f4927c315b8dd19e12df5')
	print(access_token)
	client.access_token = access_token
	athlete = client.get_athlete()
	client.access_token = access_token['access_token']
	athlete = client.get_athlete()
	athlete


def change_activity_bearer_in_db(user_id, old_activity_bearer, new_activity_bearer):
	# Function accepts strava id, old bearer and new bearer
	# Needs to be changed to a database when we start using a database
	print("Updating bearer token in database")
	with open(userdb, 'r') as readFile:
		reader = csv.reader(readFile)
		lines = list(reader)
	readFile.close()
	
	for i, h in enumerate(lines):
		for j, k in enumerate(h):
			if k == str(old_activity_bearer):
				print("bearer found")
				lines[i][j] = new_activity_bearer

	with open('scripts/users1.csv', 'w') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(lines)
		writeFile.close()

def check_for_new_posts():
	print("Search For New Posts")



get_userdata_from_db()

response = requests.get(api_url_base)
print(response.status_code)
print(api_token)

#change_activity_bearer_in_db(1111111, 222222222222222, 333333333333333)
#change_activity_bearer_in_db(1111111, 333333333333333, 222222222222222)

