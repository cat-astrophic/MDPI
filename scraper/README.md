## MDPI Scraper

This project scrapes bibliographic data for publications in MPDI journals and creates a data set containing data on international collaborations at the national level. Data for publications through the end of 2019 are available and can be found in data directory. 

### Using these scripts:

The scripts should be run in the following order:

1. MDPI.py -- this scrapes search results and gather links for all papers published by EOY 2018
2. MDPI_scraper.py -- this scrapes each link from MDPI.py and returns bibliographic data on all papers
3. MDPI_annual_data.py -- this creates bibliographic data files for each year
4. MDPI_interaction_matrix.py -- this does the primary data curation and also returns interaction (spatial) matrices

