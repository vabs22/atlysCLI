# AtlysCLI

A CLI tool to fetch visa details for any country

# Features
- Scrapes visa related information from atlys.com

- You don't need to enter the exact country name, the tool will do a fuzzy search

- Not sure which countries you want to explore? Just ask to show all the countries supported

# Installation
This CLI would work in debian OS with make installed

Install dependencies
```commandline
make setup
```

That's it

# Usage

Check visa details for any country
```commandline
make checkVisa country=singapore
```

![Screenshot](checkVisa_singapore.png)

For countries whose name can have multiple words, use double quotes in the command
```commandline
make checkVisa country="united arab"
```

![Screenshot](checkVisa_UAE.png)

To check all the supported countries
```commandline
make getSupportedCountries
```

![Screenshot](getSupportedCountries.png)

# Working
- The tool first builds a map of supported countries by fetching the static file `_next/data/XvaaJjGr7B9FuCpjZo0q1/en-IN.json`
 from server. This enables the tool to know which countries are supported
- When user makes a request, tool first checks if the country is supported
- If so, it scrapes the web page of country's visa to get realtime ETA and price

# Future Extensions
- Currently this tool is fetching a static react file containing country related data. This might not work after
deployments on atlys.com. This can be extended to instead scrape the home page and derive list of countries supported

- More visa related details can be scraped 

