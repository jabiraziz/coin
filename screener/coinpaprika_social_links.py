import requests
from coin_profile.models import CoinProfile

def coinpaprika_social_links():
    # ids = ["eth-ethereum"]
    ids = CoinProfile.objects.values_list('symbol', flat=True)[:100]
    coins_data = []
    for symbol in ids:
        print(symbol)
        url = f"https://api.coinpaprika.com/v1/coins/{symbol}"
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            response_data = response.json()
            if "links" in response_data:
                links = response_data["links"]
                iid = response_data.get("id")
                if iid:
                    coins_data.append({"id": iid, "Social_links": links})
    return coins_data

