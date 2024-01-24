from flask import Flask, jsonify, request
import mysql.connector
from datetime import datetime, timedelta

app = Flask(__name__)

# Database connection
connection = mysql.connector.connect(
    host="LAPTOP-K1QSVETP",
    user="root",
    password="root",
    database="world"
)
cursor = connection.cursor()

# API to display current week leaderboard (Top 200)
@app.route('/current-week-leaderboard', methods=['GET'])
def current_week_leaderboard():
    current_date = datetime.now()
    first_day_of_week = current_date - timedelta(days=current_date.weekday())
    last_day_of_week = first_day_of_week + timedelta(days=6)

    query = """
    SELECT UID, Name, Score, Country, TimeStamp
    FROM asgn
    WHERE TimeStamp BETWEEN %s AND %s
    ORDER BY Score DESC
    LIMIT 200;
    """
    cursor.execute(query, (first_day_of_week, last_day_of_week))
    results = cursor.fetchall()

    leaderboard = []
    for result in results:
        leaderboard.append({
            'UID': result[0],
            'Name': result[1],
            'Score': result[2],
            'Country': result[3],
            'TimeStamp': result[4].isoformat()
        })

    return jsonify(leaderboard)

# API to display last week leaderboard given a country by the user (Top 200)
@app.route('/last-week-leaderboard/<country_code>', methods=['GET'])
def last_week_leaderboard(country_code):
    current_date = datetime.now()
    last_week_start_date = current_date - timedelta(days=current_date.weekday() + 7)
    last_week_end_date = last_week_start_date + timedelta(days=6)

    query = """
    SELECT UID, Name, Score, Country, TimeStamp
    FROM asgn
    WHERE TimeStamp BETWEEN %s AND %s AND Country = %s
    ORDER BY Score DESC
    LIMIT 200;
    """
    cursor.execute(query, (last_week_start_date, last_week_end_date, country_code))
    results = cursor.fetchall()

    leaderboard = []
    for result in results:
        leaderboard.append({
            'UID': result[0],
            'Name': result[1],
            'Score': result[2],
            'Country': result[3],
            'TimeStamp': result[4].isoformat()
        })

    return jsonify(leaderboard)

# API to fetch user rank, given the userId
@app.route('/user-rank/<user_id>', methods=['GET'])
def fetch_user_rank(user_id):
    query = """
        SELECT UID, Name, DENSE_RANK() OVER (ORDER BY Score DESC) AS `Rank`
        FROM asgn;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # Find the user in the result set
    user_data = next((result for result in results if result[0] == user_id), None)

    if user_data:
        user_rank = user_data[2]  # Index 2 corresponds to the 'Rank' column
        return jsonify({'user_rank': user_rank})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
