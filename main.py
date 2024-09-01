from datetime import datetime
from dotenv import load_dotenv
from venmo import Venmo
import os

def main():
    spotify_request = {
        "total": 21.31,
        "usernames": os.getenv("VENMO_USERNAMES").split(",")
        "splitBy": 6,
    }

    now = datetime.now()
    description = f"Spotify - {now.strftime('%B %Y')}"

    venmo = Venmo(access_token=os.getenv("VENMO_ACCESS_TOKEN"))

    perUserAmount = spotify_request["total"] / spotify_request["splitBy"]
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
