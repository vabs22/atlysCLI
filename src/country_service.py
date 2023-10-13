import os
import json
from iso3166 import countries as iso3166_countries
from utils import get_json_data

FILE_DIRECTORY_PATH = os.path.dirname(__file__)


class CountryService(object):
    country_data_json_file_path = "{}/../resources/country_metadata.json".format(FILE_DIRECTORY_PATH)

    def fetch_and_save_all_country_metadata(self):
        countries_json_data = get_json_data('https://www.atlys.com/_next/data/XvaaJjGr7B9FuCpjZo0q1/en-IN.json')
        supported_countries = (countries_json_data.get("pageProps") or {}).get("clpPages") or {}

        country_metadata = {}
        for country_data in supported_countries:
            country_code = country_data.get("data").get("destination_code")
            country_metadata[country_code] = {
                "ref_url": country_data.get("uid"),
                "id": country_data.get("id"),
                "country_code": country_code
            }

        # Writing to sample.json
        with open(self.country_data_json_file_path, "w") as outfile:
            food_categories_json = json.dumps(country_metadata, indent=4)
            outfile.write(food_categories_json)

    def get_country_metadata(self, country_code) -> (bool, {}):
        countries_metadata_file = open(self.country_data_json_file_path, "r")
        countries_metadata_map = json.load(countries_metadata_file)
        countries_metadata_file.close()

        if country_code not in countries_metadata_map:
            return False, None

        return True, countries_metadata_map.get(country_code)

    def identify_country_code(self, search_query) -> (bool, str, str):
        country = iso3166_countries.get(search_query)
        if not country:
            return False, None, None

        return True, country.alpha2, country.name

    def generate_country_visa_page(self, country_metadata) -> str:
        ref_url = country_metadata.get("ref_url")
        return "https://www.atlys.com/en-IN/{}".format(ref_url)
