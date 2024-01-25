**HOSTED URL HAS BEEN IN THE API ENDPOINTS SECTION (AS DEMANDED IN THE DELIVERABLES)**

**For running on local:**
1. download the code on your local system.
2. run the requirements.txt file in order to install all the dependencies.( this includes installation of mysql and flask)
3. run the database_script.py file to create and populate the specific table in the database.
4. run the f2api.py file to access the api functionalties.

**STRUCTURE AND PROCESS OF DATABASE CREATION**
The database_script.py file contains the python script which is designed to generate and insert 10,000 random entries into a MySQL database table named 'asgn'. 
The generated entries include a unique identifier (UID), a random name, a score, a country code, and a timestamp.
--Notes
  1. The script uses the Faker library to generate random names and country codes.
  2. The generated entries have random scores between 1 and 1000.
  3. The timestamp for each entry is generated within the last 30 days.

**API ENDPOINTS AND UTILITY**
The file f2api.py contains the flask api endpoints.
This Flask application provides an API for accessing leaderboard data from a MySQL database. It includes three endpoints:

Accessing the Endpoints
for accessing the endpoints, the flask app has been hosted on : http://139.59.89.244:8080/
1.http://139.59.89.244:8080/current-week-leaderboard
2.http://139.59.89.244:8080/last-week-leaderboard/<country_code>
3.http://139.59.89.244:8080/last-week-leaderboard/<user_id>

--country codes and uids can be picked from the database--

1. Current Week Leaderboard
  Endpoint: /current-week-leaderboard
  Method: GET
  Response: JSON array containing the top 200 users for the current week.
2. Last Week Leaderboard by Country
  Endpoint: /last-week-leaderboard/<country_code>
  Method: GET
  Parameter: country_code - The country code for which to fetch the leaderboard.
  Response: JSON array containing the top 200 users from the specified country for the last week.
3. User Rank Lookup
  Endpoint: /user-rank/<user_id>
  Method: GET
  Parameter: user_id - The unique ID of the user.
  Response: JSON object containing the user's rank based on their score.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
