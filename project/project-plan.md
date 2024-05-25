# Project Plan

## Title
<!-- Give your project a short title. -->
A study of climate change in India

## Main Question

<!-- Think about one main question you want to answer based on the data. -->

1. What all does climate affect?
2. How has climate change affected India?
3. Are the effects reversible?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Climate change is something we have talked about since decades and have made several attempts to slow it down, but we have not been able to address the issues it has caused in the process. This project attempts to take a look at how much of an impact climate change has made to the Indian subcontinent. The reason I am focusing on India is due to the fact that India has been in the picture of global expansion since quite a lot of time now and also, it is one of the unfortunate handful of countries that have suffered the most due to climate change. The mode of achieving a thorough analysis of the topic in question is going to be analysis of the dataset of temperature changes in the recent years in India and then taking a look at floods in India, after that, we will look into how imports and exports have changed in the recent years in the port cities and whether or not there was an impact in that sector.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Temperature Change
* Metadata URL: https://www.fao.org/faostat/en/#data/ET/metadata
* Data URL: https://www.kaggle.com/datasets/sevgisarac/temperature-change
* Data Type: CSV

The FAOSTAT Temperature Change domain disseminates statistics of mean surface temperature change by country, with annual updates. The current dissemination covers the period 1961–2019.

### Datasource2: Floods in India
* Metadata URL: https://link.springer.com/article/10.1007/s11069-021-04698-6
* Data URL: https://www.kaggle.com/datasets/aditya2803/india-floods-inventory/data
* Data Type: CSV

The first freely-available, analysis-ready, official geospatial dataset to facilitate comprehensive flood research

### Datasource3: Import and Export data of India
* Metadata URL: https://www.kaggle.com/datasets/ramjasmaurya/exports-and-imports-of-india19972022/data
* Data URL: https://www.kaggle.com/datasets/ramjasmaurya/exports-and-imports-of-india19972022/data
* Data Type: CSV

The data shows how much of trade was carried (in Million USD) between the period of Jan 1997-July 2022 exploring 250 different countries

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. *Project Setup and Data Identification* [#1][issue1] 
    1. Indentify the major question
    2. Find data sources
    3. Select the appropriate data sources
2. *Data Manipulation* [#2][issue2]
    1. Clean the data
    2. Filter the data to remove the columns and rows that are not appropriate for answering the main question
    3. Form a stable Data Pipeline
3. *Data Analysis and Reporting* [#3][issue3]
    1. Execute initial data exploration and basic visualizations
    2. Conduct data analysis
    3. Address all the research questions
    4. Show conclusions form the analysis

The work packages are dependent on the previous ones and hence **will be worked on in a sequential manner**. As time progresses, steps will be added and/or altered according to the situation at the time

[issue1]: https://github.com/auniyal26/made-xu40lofi/issues/1
[issue2]: https://github.com/auniyal26/made-xu40lofi/issues/2
[issue3]: https://github.com/auniyal26/made-xu40lofi/issues/3
