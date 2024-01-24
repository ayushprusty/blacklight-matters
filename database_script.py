import random
from faker import Faker
import mysql.connector
from datetime import datetime, timedelta
import secrets
import time

# Now, 'unique_ids' contains 10,000 unique IDs

fake = Faker()

# username = doadmin
# password = AVNS_QVNp7BpOOlvp88mf2S-
# host = blacklight-prusty-db-do-user-13417177-0.c.db.ondigitalocean.com
# port = 25060
# database = defaultdb
# sslmode = REQUIRED

# Establish a connection to your MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="defaultdb",
    # sslmode = "REQUIRED"
)

cursor = connection.cursor()



# Create the table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS asgn (
        UID VARCHAR(36) PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Score INT NOT NULL,
        Country VARCHAR(2) NOT NULL,
        TimeStamp TIMESTAMP NOT NULL
    )
""")

# Commit the changes
connection.commit()


def generate_unique_id():
    timestamp = int(time.time() * 1000)  # Convert current time to milliseconds
    random_part = secrets.token_hex(2)[:3]  # Random 5-character hexadecimal string
    unique_id = f"{random_part}{timestamp}"
    return unique_id

# Example usage to generate 10,000 unique IDs
unique_ids = set()
for _ in range(10000):
    while True:
        new_id = generate_unique_id()
        if new_id not in unique_ids:
            unique_ids.add(new_id)
            break

unique_idd = list(unique_ids)

# Insert 10,000 random entries into the table
for i in range(10000):
    print(i)
    uid = unique_idd[i]
    name = fake.name()
    score = random.randint(1, 1000)
    country = fake.country_code()
    timestamp = fake.date_time_between(start_date="-30d", end_date="now")
    
    # Format the timestamp as a string
    timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    # Execute the INSERT INTO statement
    cursor.execute("""
        INSERT INTO asgn (UID, Name, Score, Country, TimeStamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (uid, name, score, country, timestamp_str))

    print("""
        INSERT INTO asgn (UID, Name, Score, Country, TimeStamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (uid, name, score, country, timestamp_str))

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
