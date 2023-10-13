from utils import scrape_data_from_web_page


class VisaService(object):
    fields_data = {
        "price": [
            {
                "tag": "p",
                "class": "",
                "index": 0
            }
        ],
        "eta": [
            {
                "tag": "div",
                "class": "flex items-center justify-center md:relative md:gap-0 lg:gap-4",
                "index": 0
            },
            {
                "tag": "span",
                "index": 0
            }
        ],
        "visa_type": [
            {
                "tag": "div",
                "class": "flex w-full flex-col gap-4 px-5",
                "index": 0
            },
            {
                "tag": "div",
                "class": "flex flex-row items-center gap-2 border-b-[0.5px] border-[#b8b8b8] border-opacity-75 pb-2",
                "index": 0
            },
            {
                "tag": "p",
                "class": "text-base font-medium text-black",
                "index": 0
            }
        ]
    }

    def get_country_visa_details(self, url, country_metadata) -> str:
        country_name = country_metadata.get("name")
        scraped_response = scrape_data_from_web_page(url, self.fields_data)
        text_response = "You can get a {} visa for {} at just {}. We can guarantee you will get it by {}. " \
                        "#visalikepizza".format(scraped_response.get("visa_type"), country_name,
                                                scraped_response.get("price"), scraped_response.get("eta"))
        return text_response
