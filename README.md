## MDPI

### This project was featured on the cover of Volume 8 Issue 1 of [*Publications*](https://www.mdpi.com/2304-6775/8)

This repo contains the beginning of a project which will pull bibliographic information from open access articles (from MDPI journals initially) to study topics related to international scholarly collaboration. For now the data set only contains data for Opean Access journals (MDPI).

Each subdirectory besides *scraper* and *data* represents a distinct project; *data* contains the most recent data and *scraper* contains the web scraper in its most current form. The initial version of the basis of this project (the scrapers and cleaners) can be found in the *2018_Initial* subdirectory. Detailed user instructions can be found in each subdirectory.

In order to successfully use the scraper the following modules are required:

* **urllib** for webscraping
* **bs4** for webscraping
* **pandas** for data management and analysis
* **numpy** for data management and analysis

In addition to those modules, the remainder of the scripts used in various analyses of the data require the following modules:

* **matplotlib** for general plotting
* **networkx** for plotting networks
* **geopandas** for plotting on maps

If any of these modules are not already installed, simply run the following line for each module:

* **pip install module**

If you are interested in collaborating on a project using any of this data or data collection tools, please reach out to me by [email](macary@mix.wvu.edu)

## Citation

### APA

Cary, M., & Rockwell, T. (2020). International Collaboration in Open Access Publications: How Income Shapes International Collaboration. *Publications*, 8(1), 13.

### MLA

Cary, Michael and Taylor Rockwell. "International Collaboration in Open Access Publications: How Income Shapes International Collaboration." *Publications* 8.1 (2020): 13.

### Bibtex

@article{cary2020international,\
&nbsp;&nbsp;&nbsp;&nbsp;title={International Collaboration in Open Access Publications: How Income Shapes International Collaboration
},\
&nbsp;&nbsp;&nbsp;&nbsp;author={Cary, Michael and Rockwell, Taylor},\
&nbsp;&nbsp;&nbsp;&nbsp;journal={Publications},\
&nbsp;&nbsp;&nbsp;&nbsp;volume={8},\
&nbsp;&nbsp;&nbsp;&nbsp;number={1},\
&nbsp;&nbsp;&nbsp;&nbsp;pages={13},\
&nbsp;&nbsp;&nbsp;&nbsp;year={2020},\
&nbsp;&nbsp;&nbsp;&nbsp;publisher={MDPI}\
}

