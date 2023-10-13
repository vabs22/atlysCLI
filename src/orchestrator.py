class AtlysOrchestrator(object):
    def __init__(self, country_service, visa_service):
        self.country_service = country_service
        self.visa_service = visa_service

    def get_country_visa_data(self, search_query):
        # Steps:
        """
        Steps:
            - Identify country code from customer's search query
            - Check if country is supported. If not, report error
            - Fetch country metadata
            - Fetch country page
            - Parse visa data from country page
        """
        return

    def fetch_and_save_all_country_metadata(self):
        """
        Steps:
            - Fetch country metadata
            - Save it
        """
        return

