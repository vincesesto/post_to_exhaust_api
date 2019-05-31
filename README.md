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

##### scripts/users_from_database.py

- run the script: 
  python3 scripts/users_from_database.py "31940" "6769ae72996e05a36ac38d546871dd63982b2651"

- Sample output
  Search For New Activities
  athlete id: 1778778
  activity name: Lunch Run
  activity type: Run
  distance: 6062.0
  moving time: 1909
  elapsed time: 1917
  activity id: 2410588125  
