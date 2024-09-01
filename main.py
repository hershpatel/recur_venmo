import os
from datetime import datetime
from venmo import Venmo
from dotenv import load_dotenv

def main():
    spotify_request = {
        "total": 21.33,
        "usernames": os.getenv("VENMO_USERNAMES").split(",")
    }

    now = datetime.now()
    description = f"TEST - DO NOT ACCEPT - Spotify Premium - {now.strftime('%B %Y')}"

    venmo = Venmo(access_token=os.getenv("VENMO_ACCESS_TOKEN"))

    perUserAmount = spotify_request["total"] / len(spotify_request["usernames"])
    venmo_requests = [
        (
            username,
            venmo.request_money(
                venmo.get_user_id(username),
                perUserAmount,
                description
            ),
        )
        for username in spotify_request["usernames"]
    ]

    failed_venmo_requests = [username for username, success in venmo_requests if not success]
    if failed_venmo_requests:
        raise Exception(f"[ERROR] Failed to request [${perUserAmount}] from the following users for [{description}]: {', '.join(failed_venmo_requests)}")

if __name__ == "__main__":
    load_dotenv()
    main()
