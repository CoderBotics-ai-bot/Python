"""

Scrape the price and pharmacy name for a prescription drug from rx site
after providing the drug name and zipcode.

"""

from urllib.error import HTTPError

from bs4 import BeautifulSoup
from requests import exceptions, get
from requests import get, exceptions

BASE_URL = "https://www.wellrx.com/prescriptions/{0}/{1}/?freshSearch=true"

def fetch_pharmacy_and_price_list(drug_name: str, zip_code: str) -> list | None:
    """
    Same as original docstring
    """

    def extract_pharmacy_data(soup_content):
        pharmacy_price_list = []
        grid_list = soup_content.find_all("div", {"class": "grid-x pharmCard"})
        for grid in grid_list:
            pharmacy_name = grid.find("p", {"class": "list-title"}).text
            price = grid.find("span", {"p", "price price-large"}).text
            pharmacy_price_list.append({"pharmacy_name": pharmacy_name, "price": price})

        return pharmacy_price_list

    if not drug_name or not zip_code:
        return None

    try:
        request_url = f"https://www.wellrx.com/prescriptions/{drug_name}/{zip_code}/?freshSearch=true"
        response = get(request_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return extract_pharmacy_data(soup)
    except (HTTPError, exceptions.RequestException, ValueError):
        return None


if __name__ == "__main__":
    # Enter a drug name and a zip code
    drug_name = input("Enter drug name: ").strip()
    zip_code = input("Enter zip code: ").strip()

    pharmacy_price_list: list | None = fetch_pharmacy_and_price_list(
        drug_name, zip_code
    )

    if pharmacy_price_list:
        print(f"\nSearch results for {drug_name} at location {zip_code}:")
        for pharmacy_price in pharmacy_price_list:
            name = pharmacy_price["pharmacy_name"]
            price = pharmacy_price["price"]

            print(f"Pharmacy: {name} Price: {price}")
    else:
        print(f"No results found for {drug_name}")
