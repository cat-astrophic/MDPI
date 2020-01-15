## MDPI Data Set

This constitutes the data set from the MDPI project. Data is current through EoY 2018. Updated data through EoY 2019 is expected in January 2020.

1. links.txt contains all of the urls returned by MDPI.py. Each url is to a unique paper published by MDPI.
2. papers_all.zip is a compressed csvfile containing all raw bibliographic data collected from each url in links.txt. For each paper, the data collected consists of (1) the year of publication, (2) the journal in which the paper was published, and (3) all author affiliation data. It is expected that, in the future, more bibliographic data will be included.
3. papers_by_year.zip is a folder of compressed csv files which contain annual data from the previous file.
4. Collaborations.zip is a compressed folder containing csv files containing data on which nations collaborated on each paper. The order reflects the order that the data from the papers was scraped, (i.e., the order their data was scraped by MDPI_scraper.py). This means that each row indicates a paper, and each entry in each row is a country that contributed to the paper.
5. Matrices.zip is a compressed folder containing csv files containing a data frame which indicates the number of times each pair of countries collaborated on a paper published by an MDPI journal. There are files for each year as well as a file containing all data.
