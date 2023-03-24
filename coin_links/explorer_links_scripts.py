from coin_profile.models import CoinProfile
from .models import ExplorerLinks

from .api_scripts.coinpaprika_explorer_links import coinpaprika_explorer_links

def explorer_links_scripts():
    coins_explorer_links = coinpaprika_explorer_links()
    for coin_data in coins_explorer_links:
        coin_name = coin_data["id"]
        try:
            all_explorer_links = coin_data["explorer_links"]
            coin_profile = CoinProfile.objects.get(coin_id=coin_name)
            for explorer_link in all_explorer_links:
                ExplorerLinks.objects.update_or_create(
                    symbol=coin_profile,
                    explorer_link=explorer_link,
                )
        except:
            pass