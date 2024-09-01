# RECUR VENMO
Python script to automate frequent venmo requests.

It's currently set up to request monthly venmos for a spotify family plan.

## Getting started

#### Local setup
1. `pip install -r requirements.txt`
2. Create a `.env` file with the following variables:
    - `VENMO_ACCESS_TOKEN`
    - `VENMO_USERNAMES`
3. Run `python3 main.py` to request venmo payments.

#### GitHub Actions
1. Add the following GitHub secrets to the repository:
    - `VENMO_ACCESS_TOKEN`
    - `VENMO_USERNAMES`
2. Add a request payments action, using the existing `venmo_request.yml` file, under `.github/workflows`. Update the cron job with the desired frequency.

## Venmo Access Token

#### Request token
To get your access token, you will need to complete the 2FA process
This will print the access token after the first time you use the library.

```
access_token = Client.get_access_token(username='email@email.com', password='******')
```

##### Revoke token
**Note** that your access token never expires! If you want to revoke it, you can do so by calling...

```
client.log_out(f"Bearer {access_token}")
```

##### Learn more
https://github.com/mmohades/Venmo#usage
