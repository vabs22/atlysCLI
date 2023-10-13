import os
import json
import pycountry
from utils import get_json_data

FILE_DIRECTORY_PATH = os.path.dirname(__file__)


class CountryService(object):
    country_data_json_file_path = "{}/../resources/country_metadata.json".format(FILE_DIRECTORY_PATH)

    def fetch_and_save_all_country_metadata(self):
        countries_json_data, is_error, error_message = \
            get_json_data('https://www.atlys.com/_next/data/XvaaJjGr7B9FuCpjZo0q1/en-IN.json')
        if is_error:
            print(error_message)
            return

        supported_countries = (countries_json_data.get("pageProps") or {}).get("clpPages") or {}

        country_metadata = {}
        for country_data in supported_countries:
            country_code = country_data.get("data").get("destination_code")
            iso_country_data = pycountry.countries.get(alpha_2=country_code)
            country_metadata[country_code] = {
                "ref_url": country_data.get("uid"),
                "id": country_data.get("id"),
                "country_code": country_code,
                "name": iso_country_data.name
            }

        # Writing to sample.json
        with open(self.country_data_json_file_path, "w") as outfile:
            food_categories_json = json.dumps(country_metadata, indent=4)
            outfile.write(food_categories_json)

    def get_all_country_metadata(self) -> {}:
        countries_metadata_file = open(self.country_data_json_file_path, "r")
        countries_metadata_map = json.load(countries_metadata_file)
        countries_metadata_file.close()

        return countries_metadata_map

    def get_country_metadata(self, country_code) -> (bool, {}):
        countries_metadata_map = self.get_all_country_metadata()
        if country_code not in countries_metadata_map:
            return False, None

        return True, countries_metadata_map.get(country_code)

    def identify_country_code(self, search_query) -> (bool, str, str):
        try:
            countries = pycountry.countries.search_fuzzy(search_query)
            if not countries or len(countries) < 1:
                return False, None, None

            return True, countries[0].alpha_2, countries[0].name
        except:
            return False, None, None

    def generate_country_visa_page(self, country_metadata) -> str:
        ref_url = country_metadata.get("ref_url")
        return "https://www.atlys.com/en-IN/{}".format(ref_url)
