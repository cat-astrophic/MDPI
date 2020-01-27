## MDPI 2018 Initial

This project scrapes bibliographic data for publications in MPDI journals and performs various analyses that can be found in the paper "International Collaboration in Open Access Publications: How Income Shapes International Collaboration" which is currently under review at *Publications*.

### Using these scripts:

The scripts should be run in the following order:

1. MDPI.py -- this scrapes search results and gather links for all papers published by EOY 2018
2. MDPI_scraper.py -- this scrapes each link from MDPI.py and returns bibliographic data on all papers
3. MDPI_annual_data.py -- this creates bibliographic data files for each year
4. MDPI_interaction_matrix.py -- this does the primary data curation and also returns interaction (spatial) matrices
5. MDPI_summary_data.py -- this creates dataframes containing summary data in a variety of ways as well as histograms
6. MDPI_maps.py -- this uses networkx and geopandas to create weighted graphs on maps to visualize collaborations
7. MDPI_scimago.py -- this curates scimago data, making it usable for creating the panel data set in MDPI_panel_data.py
8. MDPI_panel_data.py -- this creates a panel data set with bibliographic and some socioeconomic data
9. MDPI_data_analysis.py -- this perfroms initial data analysis for the project including Kolmogorov-Smirnov tests
10. MDPI_regional_maps.py -- this creates plots of the income group and continent of the top collaborator by nation
11. MDPI_FM_prep.py -- this creates the annualized files from (3) (plus a comprehensive file) replcaing journal with Frascati Manual classification

### Data files:

The files containing the scraped MDPI data are presented here and can be used in lieu of running the .py files. This includes the cleaned Scimago data. Additional data from the World Bank WDI data set which is used is included here as well.
