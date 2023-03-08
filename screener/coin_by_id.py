import requests
from coin_profile.models import CoinProfile

def coin_by_id():
    """
    Retrieve information about a specific cryptocurrency.

    Uses CoinPaprika API to retrieve information about a specific
    cryptocurrency, identified by its `id`.

    Returns:
        dict: A dictionary containing information about the specified cryptocurrency.
    """
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
                if "explorer" in links:
                    explorer_links = links["explorer"]
                    iid = response_data.get("id")
                    if iid:
                        coins_data.append({"id": iid, "explorer_links": explorer_links})
    return coins_data
                    
# coin_by_id()
