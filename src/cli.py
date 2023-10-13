import sys
from orchestrator import AtlysOrchestrator
from country_service import CountryService
from visa_service import VisaService

orchestrator_service = AtlysOrchestrator(CountryService(), VisaService())

if len(sys.argv) <= 1:
    print("[Error] Command name missing")
    exit(1)

if len(sys.argv) <= 2:
    print("File path missing")
    exit(1)

command_name = sys.argv[1]

if command_name == "checkVisa":
    if len(sys.argv) <= 2:
        print("[Error] Please provide a country name to try out this feature. A rough hint about name would also work :)")
        exit(1)

    search_query = sys.argv[2]
    error_message, success_message = orchestrator_service.get_country_visa_data(search_query)
    if error_message != "":
        print(error_message)
    else:
        print(success_message)

elif command_name == "precomputeCountryMetadata":
    orchestrator_service.fetch_and_save_all_country_metadata()

elif command_name == "getSupportedCountries":
    message = orchestrator_service.get_supported_countries()
    print(message)

print("||| Bye |||")
