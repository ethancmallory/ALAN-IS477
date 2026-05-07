# ALAN: Italian Economic Analysis
## Contributors: 
- Ethan Mallory - ethanm8@illinois.edu
- Alex Tapanes - tapanes2@illinois.edu
## Summary:
Work done on this project was set out with the goal of creating a merged dataset combining a series of datasets that contain macroeconomic information about the italian economy over the last ~ 30 years. This analysis was performed with a focus on how things change temporally, with the goal of using these macroeconomic statistics to assess how the Italian economy had development over this period. We took datasets from the World Bank, as well as IStat, or *Istituto Nazionale di Statistica* the Italian National institute of statistics.

Our motivations, beyond developing skills in working with data across varied formats and file structures and improved understanding of best data profiling, cleaning, and preserving practices, is to create a dataset that combines the most readily available macroeconomic data on the Italian economy in a way that makes it the most easily interpretable and easiest to work with for anyone who chooses to use our dataset for any future research or analyis that they desire to perform on the subject. By making the dataset as concise, easily reproducible, and clear to understand as we can, we are making the data accessible to a wider range of potential researchers and or analysts.

The primary research questions that we set out to answer with this project are as follows:
- How has Italy's enonomic structure changed on a national level over the last 3 decades, and what macroenomic measures are most indicative of this change and any devlopment that took place?
- How does unemployment vary across time with respect to the Italian economy, is it getting better or worse at the moment? Can we match periods with the greatest degree of unemployment related strife to major world events (COVID)?
- Based on this historic data, which sectors are in the best position for future economic growth or maintained economic stability?

## Data profile:
The first four datasets used are sourced from IStat, mostly containing a single row of interest besides the time element as related to our analysis per dataset, they are as follows (however it is important to note that the provincial data was not used in the final analysis or merged in the final dataset creation, going against our original plan): 
- Compensation of Employees by Industry, located at "Compensation of employees and its components by industry (IT1,93_1227_DF_DCCN_TNA1_2,1.0).csv" in the Github project repository. This dataset contains estimates of employee pay rates in Italy broken down across industry year by year. Covering the Italian economy on a national level, with a time period of 2015-2024 for this particular dataset. The key variable of interest is "Observation" which contains the relevant compensation data, however there are ~30 other columns specifying informaiton about the indsutry and other economic measures. "Observation" records employee compensation by industry in millions of euros.
- Output and Value Added by Industry, located at "Output and value added by industry (IT1,92_1225_DF_DCCN_ANA1_1,1.0)(1).csv" in the Github project repository. Contains estimates for gross output and gross value added to the total national GDP by industry, once again on a year to year basis. Timeframe is 2016-2025 in this case, unit of measurement is once again millions of euros. Besides these two key columns there are nearly 40 other containg once again a variety of macroeconomic information about the italian economy and its various industries over the specified period.
- GDP Supply Side, located at "Gross domestic product supply side (IT1,93_498_DF_DCCN_PILT_1,1.0)(1).csv" in the Github repository. Containing GDP estimates for Italy at the national level as well as across various states/provinces, with an identical timeframe to the first dataset, 2015-2024. Values in "Observation" are once again in millions of euros, and cover provincial breakdowns of the GDP along with the national total, along with ~30 other columns that can be disregarded with relation to our research questions.
- Provincial Employment Rate, located at "rovincial data (IT1,150_915_DF_DCCV_TAXOCCU1_5,1.0).csv" in the Github Repository. This dataset was not ultimately used for analysis, however it contained unemployment data across different combinations of sex, region, and province from 2023-2025. With the employment rate expressed as a percentage of the working age population that is employed, working age specified as being from 15-89.

These datasets are all published by IStat, and are therefore all subject to the same copyright and otherwise legal constraints. They all have a Creative Commons Attribution 3.0 License, (CC BY 3.0) meaning they can be freely used as long as they are properly attributed. The datasets should also pass on all ethical checks, as there is no information about any single people that could be used to identify individuals, all data points are some form of national or regional aggregate as they relate to people.

## Data quality:
FAIR Principles:
- Findability: The IStat datasets are rather easily accessible via the IStat data browser, located at esploradati.istat.it, and each dataset has a unique identifier contained in the file name before the file extension.
- Accessibility: These datasets are available for download without authentication, coming in standard CSV format, and the documentation notes that they are supposed to be available via IStat's RestAPI and their respective Python package istatapi, however there are noatable issues with the use of this package, and the unique identifiers that work with the data browser do not seem to be consistent for api usage. Indicative of potential accessibility issues relating to API maintenance.
- Interoperability: The datasets as a whole are rather easily interoperable, using standard classification for industries and an easily workable data structure, it is rather easily to work with both the datasets as World Bank uses the same ISO country code which makes for easy matching. It is however notable that the key columns of interest are often recorded differently across these different endpoints, the API refers to "Observation" as "OBS_VALUE" and names are not always descriptive of what the dataset is trying to be representative of.
- Reusability: All the datasets fall under the same CC-BY 3.0 license and contain sufficient metadata describing the units, valuation methods, and data types needed to make them rather reusable. The only issue of note is the lack of descriptivness with the "Observation" columns, leading the user to have to make the connection between the dataset title and the observations meaning.

We also considered assessing things such as the datasets respective completeness, consistency, timeliness, and relative provenance before begining working with the data. Our observations were as follows:
- Completeness: While the datasets do not all cover the same time period, World Bank going all the way until the 90s and most of the IStat data only being back until around 2015, we were able to find around a ten year period of overlap where all the datasets should provide coverage on the Italian economy between 2016-2024 period.
- Consistency: Most measures are summary values recorded some macroeconmic total, and consistency is good as the majority of the data points are in millions of euros, with very low counts of missing values in the original datasets, the biggest consistency challenge being that the majority of World Bank data uses percentage based summaries which should not be compared directly with nominal totals.
- Timeliness: The IStat datasets are generally up until 2025, making them very recent however the World Bank data creates some lag in our datas timeliness as it is not up to the same date.
- Provenance: World Bank and IStat are both authoritative sources on worldwide and Italian Economic data, providing a strong degree of provenance for the use of these particular datasets.
## Data cleaning:
The data cleaning for this particular project occurred in two primary stages, during the initial merge of the 4 datasets that were ultimately used, and cleaning with openrefine to reduce redudancy and remove any duplicate rows as well as augment the column names with the hopes of improved reproducibility.

The merge script reduces any additional data to Italy national level aggregates of the column of interest for that particular dataset regarding the IStat datasets, and includes only information relevant to Italy that was originally in the much larger World Bank dataset. This was done by filtering each Istat dataset to only contain a time element and its relevant "Observation" column, before performing an outer merge based on time. The world bank data was additionally reshaped to long format before the merge.

The OpenRefine cleaning was a relatively simple process as well as the merge script inherently reduced a lot of redudancy by eliminating useless columns in the IStat datasets and removing countries outside our nation of interest from the World Bank data. The merge had originally produced duplicate columns of every relevant World Bank colmn, these were removed. In this process the columns were renamed to several variations of column_x and column_y, after removing the duplicates these names and the respective names that should have been with the IStat data from the start were fixed. I then manually selected the first row of every relevant year as there were several thousand duplicate rows, and kept only the rows that contained non-duplicate information relevant to analysis.

This cleaning process yielded a datast that contains no duplicate rows or columns, with a final shape of 36 years of data across 25 different economic indicators.

The final dataset was restricted to the overlapping period 2000–2024 and merged using an inner join with World Bank indicators to ensure temporal alignment across sources.

## Findings: [~500 words] Description of any findings including numeric results and/or visualizations.
The final merged dataset provides a unified annual view of Italy’s structure from 2000 to 2024, combining national accounts data from ISTAT with financial stability and indicators from the World Bank. Our resulting dataset allows for cross variable comparison across things like labor compensation, value added, GDP-related metrics, and financial system indicators within a consistent time-series structure.

One of the most immediate observations from the dataset is the strong temporal alignment between gross value added and GDP-related measures, which is expected given their shared macroeconomic foundations. Over time, both indicators show steady growth with noticeable volatility during major global disruptions, particularly the 2008 financial crisis and the 2019/2020 COVID-19 pandemic. These shocks are reflected as temporary declines or stagnation in multiple economic indicators, followed by recovery trends in subsequent years.

Labor compensation, while included as a key structural variable, shows significantly more missingness due to limited temporal coverage in the underlying ISTAT dataset. However, in the years where data is available, compensation trends generally move in line with value added, which makes sense. This idea continues to align with classical macroeconomic expectations where wages and output are positively correlated over long-run periods, though short-term deviations may occur during economic shocks.

The World Bank indicators introduce a complementary financial dimension to the dataset. These variables capture aspects of debt structure, financial exposure, and macro-financial risk. Compared to the ISTAT real-economy variables, these indicators tend to exhibit smoother trends with gradual structural changes rather than sharp cyclical movements. This contrast highlights the difference between real economic output and financial system evolution, where financial indicators often adjust more slowly but can signal longer-term vulnerabilities.

Across the full dataset, missing data patterns are non-random and primarily driven by source coverage differences rather than data quality issues. ISTAT variables are more recent but narrower in scope, while World Bank indicators provide broader coverage but are more abstract in interpretation. As a result, the merged dataset reflects a tradeoff between temporal completeness and variable richness.

Overall, the dataset successfully enables exploratory macroeconomic analysis across multiple dimensions of the Italian economy. It supports comparative analysis of structural output trends, labor dynamics, and financial stability over time. However, interpretation must account for uneven coverage across variables, particularly when comparing ISTAT and World Bank sources directly.
## Future work: [~500-1000 words] Brief discussion of any lessons learned and potential future work.
While our current dataset provides a structured and reproducible foundation for analyzing Italy’s macroeconomic evolution, there are so many  directions in which this project could be extended to improve in analytical depth.

I believe a primary area for future work likely involves improving data completeness and harmonization across sources. Currently, labor compensation data is incomplete relative to GDP and value-added measures, which limits the ability to perform fully consistent time-series comparisons. Future iterations of this project could incorporate additional ISTAT datasets or alternative labor market indicators to fill temporal gaps. Similarly, expanding World Bank coverage to ensure consistent indicator availability across the full time range would reduce missingness and improve model stability.

Another important extension would be the incorporation of real values. The current dataset primarily uses nominal euro values, which limits the ability to interpret long-term trends without accounting for price level changes. Converting all monetary variables into constant euros using something like CPI deflators would significantly improve comparability across time and strengthen any conclusions about real economic growth.

Looking at it from an analytical perspective, the dataset currently supports descriptive and exploratory analysis but has not yet been used for formal econometric modeling. Future work could include regression analysis to quantify relationships between labor compensation, GDP, and financial indicators. Time-series models such as ARIMA or vector autoregression (VAR) could also be applied to examine dynamic interactions between macroeconomic variables and assess predictive relationships.

Another potential extension involves incorporating regional-level disaggregation. The current dataset focuses on national aggregates, but Italy exhibits strong regional economic heterogeneity. Integrating regional ISTAT datasets would allow for spatial comparisons between northern and southern regions and enable analysis of internal economic divergence over time.

Introspecting on the methods we used, the reproducibility pipeline could certainly be improved by fully containerizing the workflow using a Docker. This would ensure consistent execution across different computing environments and eliminate dependency-related issues. Additionally, integrating automated data validation steps within the Snakemake pipeline (maybe with a schema checks) would improve overall robustness and prevent silent data quality failures.

Finally, a more advanced extension of this project would involve linking macroeconomic indicators to external outcome variables such as unemployment, productivity, or inequality measures. This would enable a more causal interpretation of structural economic changes rather than purely descriptive trends.

Overall, while the current project successfully establishes a clean and reproducible macroeconomic dataset, future work should focus on improving completeness, introducing real-value adjustments, expanding spatial granularity, and moving from descriptive analysis toward predictive and causal modeling.
## Challenges:
API accessibility was a major challenge when working with the IStat data. The istatapi data was not consistent with the data that we had been able to access using their data portal, and using requests with the IStat data portal did not work as intended either. These issues combined made it rather difficult to deteremine a way to write a script that could automatically download the correct datasets, and has greatly harmed the reproducibilty aspect of our project overall.
## Reproducing: Sequence of steps required for someone else to reproduce your results.
IStat datasets must be accessed following the following respective links to access the IStat data browser in order to get the correct versions of the datasets for reproducibility with the scripts used for cleaning and analysis in this repository.

https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,DATAWAREHOUSE,1.0/UP_ACC_TERRIT/IT1,93_1227_DF_DCCN_TNA1_2,1.0

https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,DATAWAREHOUSE,1.0/UP_ACC_ANNUAL/IT1,92_1225_DF_DCCN_ANA1_1,1.0

https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,DATAWAREHOUSE,1.0/UP_ACC_TERRIT/IT1,93_498_DF_DCCN_PILT_1,1.0

https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,Z0500LAB,1.0/LAB_OFFER/LAB_OFF_EMPLOY/DCCV_TAXOCCU1/IT1,150_915_DF_DCCV_TAXOCCU1_5,1.0

#### To reproduce results:
        Clone the repository:
            git clone <repo-url>
            cd ALAN-IS477

        Ensure dependencies are      installed:
            pip install pandas numpy matplotlib openpyxl snakemake

        Place the required ISTAT and World Bank CSV files in the project root directory.

        Run the full pipeline:
            snakemake --cores 1

## References: Formatted citations for any papers, datasets, or software used in your project.

ISTAT (2025). Compensation of employees and its components by industry. Italian National Institute of Statistics. https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,DATAWAREHOUSE,1.0/UP_ACC_TERRIT/IT1,93_1227_DF_DCCN_TNA1_2,1.0

ISTAT (2025). Gross domestic product, supply side. Italian National Institute of Statistics. https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,DATAWAREHOUSE,1.0/UP_ACC_TERRIT/IT1,93_498_DF_DCCN_PILT_1,1.0

ISTAT (2025). Output and value added by industry. Italian National Institute of Statistics. https://esploradati.istat.it/databrowser/#/en/dw/categories/IT1,DATAWAREHOUSE,1.0/UP_ACC_ANNUAL/IT1,92_1225_DF_DCCN_ANA1_1,1.0

https://github.com/openrefine/openrefine