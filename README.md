## MDPI

This repo contains the beginning of a project which will pull bibliographic information from open access articles (from MDPI journals initially) to study topics related to international scholarly collaboration. For now the data set only contains data for Opean Access journals (MDPI).

Each subdirectory besides *scraper* and *data* represents a distinct project; *data* contains the most recent data and *scraper* contains the web scraper in its most current form. The initial version of the basis of this project (the scrapers and cleaners) can be found in the *2018_Initial* subdirectory.

In order to successfully use the scraper the following modules are required:

* **urllib** for webscraping
* **bs4** for webscraping
* **pandas** for data management and analysis
* **numpy** for data management and analysis
* **matplotlib** for general plotting
* **networkx** for plotting networks
* **geopandas** for plotting on maps

If any of these modules are not already installed, simply run the following line for each module:

* **pip install module**

If you are interested in collaborating on a project using any of this data or data collection tools, please reach out to me by [email](macary@mix.wvu.edu)
