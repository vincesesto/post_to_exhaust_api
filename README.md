# Easy Exhaust Applications
  
## Connect Users In Strava To Automatically Post to Exhaust

## Work In Progress

### Currently Using CSV, but will deploy database at a later date
 
### Files/DB's

#### users1
- name: Strava athlete profile firstname and lastname
- strava_id: Strava athlete id number
- steemit_user: Steemit username
- strava_users_key: Once off access key for user, needs to be obtained with user originally accepts access to app
- latest_bearer: Latest access token for posting and extracting data, needs to be updated every 6 hours

#### posts1
- user: User identified by Steemit username
- strava_activity_id: Activity Id assigned by Strava able to reference back to verify if posts have been added
- type: Activity type to be added to exhaust; run, hike, bike, strength, yoga
- photo: Downloaded image from strava, for now...yes or no
- description: Description added from Strava description, or created if no description provided
- date: Date of the activity in local time 
- title: Title of the activity from Strava
- distance: Distance of the activity in metres
- duration: Duration of the activity
- sent_to_exhaust: Y|N set to exhaust

##### scripts/users_from_database.py

- run the script: 
```
  python3 scripts/users_from_database.py "strava_client_id" "strava_client_secret"

```
Sample output

```
  Search For New Activities
  athlete id: 1778778
  activity name: Lunch Run
  activity type: Run
  distance: 6062.0
  moving time: 1909
  elapsed time: 1917
  activity id: 2410588125  
```

## To Do
- Script to place things into a database
-- Verify they have not been added to the database previously
- Script to add them to exhaust from the database
-- Verify they have not been added to exhaust previously
- Welcome page for uses to access the Strava app
