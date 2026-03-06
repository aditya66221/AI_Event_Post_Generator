def generate_posts(event):

    title = event["title"]
    date = event["date"]
    location = event["location"]
    description = event["description"]

    linkedin = f"""
🚀 Join us for {title}

📅 Date: {date}
📍 Location: {location}

{description}

#AI #Technology #Innovation
"""
    instagram = f"""
🔥 {title} is coming!

📅 {date}
📍 {location}

{description}

#AI #TechEvent #Innovation
"""

    facebook = f"""
We are excited to announce {title}!

📅 {date}
📍 {location}

{description}

Don't miss it!
"""

    twitter = f"""
{title} on {date} at {location}.

{description}

#AI #Event
"""

    return {
        "linkedin": linkedin,
        "instagram": instagram,
        "facebook": facebook,
        "twitter": twitter
    }