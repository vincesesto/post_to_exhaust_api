#!/usr/bin/evn python3
import csv

# Extracting users from CSV for time being
userdb="/Users/vincesesto/NewStrava/users1.csv"

with open(userdb) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['name'], row['strava_id'])

