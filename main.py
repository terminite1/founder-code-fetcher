# Program to retrieve Fortnite founder invite codes
# If you bought Deluxe/Limited/Ultimate before July 17th 2018 you got a few codes to give out to friends
import requests

account_url = 'https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token'

print("STW Founder Code Fetcher")
print("By: @terminite")
print("\n")

platform = input("Select your platform (epic, xbox): ")
if platform != "epic" and platform != "xbox":
    print("Invalid platform, defaulting to epic")
    platform = "epic"
print("Visit this URL: https://epicgames.com/id/api/redirect?clientId=ec684b8c687f479fadea3cb2ad83f5c6&responseType=code")
auth = input("Insert authorizationCode: ").strip()

global accountInfo

try:
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    body = "grant_type=authorization_code&code=" + auth
    auth = ("ec684b8c687f479fadea3cb2ad83f5c6", "e1f31c211f28413186262d37a13fc84d")
    response = requests.post(account_url, headers=headers, data=body, auth=auth)
    response.raise_for_status()
    response = response.json()
    accountInfo = (response['access_token'], response['account_id'])
except requests.HTTPError as e:
    print("\nWHOOPS ! Something went wrong ! Error 400 means your authorization code invalidated. Try inputting it quicker next time\n")
    print(str(e))
    input("Press enter to exit")
    exit()

print("account info fetched !!")

codes_url = f'https://fngw-mcp-gc-livefn.ol.epicgames.com/fortnite/api/game/v2/friendcodes/{accountInfo[1]}/{platform}'

try:
    headers = {
        "Authorization": "Bearer " + accountInfo[0],
        "Content-Type": "application/json"
    }
    response = requests.get(codes_url, headers=headers)
    response.raise_for_status()
    response = response.json()
    print("Codes: " + str(response))
except requests.HTTPError as e:
    print(str(e))
