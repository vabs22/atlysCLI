class AtlysOrchestrator(object):
    def __init__(self, country_service, visa_service):
        self.country_service = country_service
        self.visa_service = visa_service

    def get_country_visa_data(self, search_query) -> (str, str):
        """
        Steps:
            - Identify country code from customer's search query
            - Check if country is supported. If not, report error
            - Fetch country page
            - Parse visa data from country page
        """
        found, country_code, country_name = self.country_service.identify_country_code(search_query)
        if not found:
            return "Oops, I didn't understand which country you asking from your input: \"{}\"".format(search_query), None

        supported, country_metadata = self.country_service.get_country_metadata(country_code)
        if not supported:
            return "Unfortunately we don't support this country at Atlys, but you can refer the full list of " \
                   "countries we support using command: \"make getSupportedCountries\"", None

        visa_url = self.country_service.generate_country_visa_page(country_metadata)
        return None, self.visa_service.get_country_visa_details(visa_url, country_metadata)

    def fetch_and_save_all_country_metadata(self):
        """
        Steps:
            - Fetch country metadata
            - Save it
        """
        self.country_service.fetch_and_save_all_country_metadata()
