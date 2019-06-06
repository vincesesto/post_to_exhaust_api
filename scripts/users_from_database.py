#!/usr/bin/evn python3
import csv
import requests
import json
import sys
import stravalib

# Extracting users from CSV for time being
userdb="/Users/vincesesto/NewStrava/users1.csv"
#userdb="scripts/users1.csv"
postdb="scripts/posts1.csv"
client_id=sys.argv[1]
api_token=sys.argv[2]
api_url_base='https://www.strava.com/api/v3/athlete/activities'

#################TO DO########################
# 1. Verify the api_token is added as a command line arguement
# 2. Try catch for all statements
# 3. Logging
# 4. Security
# 5. Set time frame of one week for check_for_new_activities function


# Go through the users in the database
# Get a user from the database
	# Get the users strava_users_key latest_bearer
# Update their latest_bearer for the user so you can check more activity
	# Update this in the database
# Search through users activity
	# Find activity that is tagged correctly
	# Verify it has not been posted to steemit already 

def add_activity_to_database(post_db_list):
	# Add following details to the database as function arguements
	# user,strava_activity_id,type,photo,description,date,title,distance,duration,sent_to_exhaust
	print("Adding the activity to the database")
	with open(postdb, 'a') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerow(post_db_list)
		writeFile.close()

def check_activity_db(activity_id):
	# Check to see if the activity has been added to the database
	with open(postdb, 'r') as readFile:
		reader = csv.reader(readFile)
		lines = list(reader)

	found = False
	for line in lines:
		if activity_id in line:
			found = True
			break
	return found

def change_activity_bearer_in_db(old_activity_bearer, new_activity_bearer):
	# Update this in the database
	with open(userdb, 'r') as readFile:
		reader = csv.reader(readFile)
		lines = list(reader)
		readFile.close()

	for i, h in enumerate(lines):
		for j, k in enumerate(h):
			if k == str(old_activity_bearer):
				# print("bearer found")
				lines[i][j] = new_activity_bearer

	with open('scripts/users1.csv', 'w') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(lines)
		writeFile.close()

def update_activity_bearer(user_key,activity_bearer):
        # Update their latest_bearer for the user so you can check more activity
        # Update this in the database

	# print("Obtaining New Activity Bearer")
	client = stravalib.client.Client()
	access_token = client.exchange_code_for_token(client_id=31940,client_secret=api_token,code=user_key)
	client.access_token = access_token
	#print("Updating token in db from: " + activity_bearer + " " + access_token['access_token'])
	change_activity_bearer_in_db(activity_bearer, access_token['access_token'])
	return access_token['access_token']

def check_for_new_activities(activity_bearer):
	# Search through users activity
	# Find activity that is tagged correctly
		# Verify it has not been posted to steemit already
	print("Search For New Activities")
	bearer_header = "Bearer " + activity_bearer
	headers = {'Content-Type': 'application/json', 'Authorization': bearer_header}
	parameters = {"after": 1558231822}
	response = requests.get( api_url_base, headers=headers, params=parameters )
	data = response.json()
	activity_id = data[-1]['id']
	activity_logged = check_activity_db(str(activity_id))

	if activity_logged == True:
		print("No new activities to post")
	else:
		print("athlete id: " + str(data[-1]['athlete']['id']))
		print("activity name: " + data[-1]['name'])
		print("activity type: " + data[-1]['type'])
		print("distance: " + str(data[-1]['distance']))
		print("moving time: " + str(data[-1]['moving_time']))
		print("elapsed time: " + str(data[-1]['elapsed_time']))
		print("activity id: " + str(data[-1]['id']))
	
		# Extract extra details using activity id
		activity_parameters = {"id": activity_id}
		activity_url = "https://www.strava.com/api/v3/activities/" + str(activity_id)
		print(activity_url)
		activity_response = requests.get( activity_url, headers=headers, params=activity_parameters )
		activity_data = activity_response.json()
		print("activity date: " + str(activity_data['start_date_local']))
		print("description: " + str(activity_data['description']))
		print("photos: " + str(activity_data['photos']))

		# Create new list with details
		# user,strava_activity_id,type,photo,description,date,title,distance,duration,sent_to_exhaust
		fields_to_database = [str(data[-1]['athlete']['id']),
					str(data[-1]['id']),
					str(data[-1]['type']),
					"none",
					str(activity_data['description']),
					str(activity_data['start_date_local']),
					str(data[-1]['name']),
					str(data[-1]['distance']),
					str(data[-1]['moving_time']),
					"n"]

		add_activity_to_database(fields_to_database)

def get_userdata_from_db(user_database):
	# Go through the users in the database
	# Return user details

	with open(user_database) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			name=row['name']
			strava_id=row['strava_id']
			user_key=row['strava_users_key']
			activity_bearer=row['latest_bearer']

			#print("Obtaining new activity bearer for user: " + name)
			update_activity_bearer(user_key,activity_bearer)
			check_for_new_activities(activity_bearer)

get_userdata_from_db(userdb)

sys.exit()

