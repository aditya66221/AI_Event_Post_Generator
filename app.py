from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ai_events"
)

cursor = db.cursor(dictionary=True)


# -------------------------------
# Home Route
# -------------------------------

@app.route("/")
def home():
    return jsonify({"message": "AI Event Social Media Generator API"})


# -------------------------------
# Add Event
# -------------------------------

@app.route("/events", methods=["POST"])
def add_event():

    data = request.json

    query = """
    INSERT INTO events (title, date, location, type, description)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (
        data["title"],
        data["date"],
        data["location"],
        data["type"],
        data["description"]
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "Event added successfully"})


# -------------------------------
# Get Events
# -------------------------------

@app.route("/events", methods=["GET"])
def get_events():

    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()

    return jsonify(events)


# -------------------------------
# Generate AI Social Media Posts
# -------------------------------

@app.route("/generate/<int:event_id>", methods=["GET","POST"])
def generate_posts(event_id):

    cursor.execute("SELECT * FROM events WHERE id=%s", (event_id,))
    event = cursor.fetchone()

    if not event:
        return jsonify({"error": "Event not found"})


    title = event["title"]
    date = event["date"]
    location = event["location"]
    description = event["description"]


    # Platform posts
    posts = {
        "linkedin": f"""
🚀 Join us at {title}!

📅 Date: {date}
📍 Location: {location}

{description}

Looking forward to connecting with industry professionals and exploring new opportunities.

#AI #Innovation #Networking
""",

        "instagram": f"""
✨ {title}

📅 {date}
📍 {location}

{description}

🔥 Don't miss this amazing event!

#AI #TechEvent #Innovation
""",

        "facebook": f"""
We are excited to announce {title}!

📅 Date: {date}
📍 Location: {location}

{description}

Join us and be part of an inspiring event.
""",

        "twitter": f"""
🚀 {title}

📅 {date}
📍 {location}

{description}

#AI #Tech
"""
    }

    return jsonify(posts)


# -------------------------------
# Run Server
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5003)

@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):

    query = "DELETE FROM events WHERE id=%s"
    cursor.execute(query, (event_id,))
    db.commit()

    return jsonify({"message": "Event deleted successfully"})