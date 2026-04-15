## Completed Work

Regarding the Data we had originally intended to collect from IStat, which would have included nationwide, provincial, and regional level data on the development of the Italian economy across different segments and industries over the last decade, a majority of this data has been successfully acquired at this point in time, the only complications being with accessing quality data on smaller scales, IStat lacks publicly available datasets for GDP and value added for different industries on a municipal/regional level.

To be more specific, the IStat sourced datasets that we have currently obtained and intend to use for creation of a larger dataset and analysis on the nations economic development include information on employee wages and other compensation on a national level (2016-2025), national level GDP and its main components (2016-2025), Supply side GDP from a regional level (2016-2024) and total output across industries at a national level (2016-2025).

We have begun exploratory work on this data  in terms of the calculation of summaries and some initial visualization and plotting work, however we are lagging behind overall in terms of where the analysis was originally intended to be at this point in time.

Now regarding the World Bank portion, I had detailed my focus being identifying, documenting, and prepping the World Bank datasets so that it can be integrated with Etans aforementioned IStat economic data.

After review, I selected the "Cross-Country Database of Fiscal Space". A dataset that covers 202 different economies (although we are primarily focused on Italy) from 1990-2022 and it includes 23 different indicators across three fiscal dimensions: government debt,  external and private sector debt, and market access. With this, we are provided macro-level fiscal context that goes hand-on-hand with the IStat's national and regional economic indicators.

I decided to use OpenRefine to clean and restructure my CSV file. There were clear issues like country capitalization, missing values, unclear labeling, inconsistent formatting, etc... The preprocessing stage is extremely necessary to allow merging with the IStat data on shared attributes like country and year.

## Updated Timeline

Given the progress we have made so far in terms of performing exploratory analysis on the initial versions of the datasets we have acquired thus far, as well as issues with merging the datasets towards a more refined final product, we have had to push back our original timeline somewhat, as well as scale down the number of questions that we intended to answer based on the original plan for what data was supposedly accessible.

While we have completed some work in terms of processing our data and preparing it for visualizations that would allow for more obvious conclusions and answers to our research questions at this point, there is still work to be done in regards to cleaning the data and performing a merger on the data we have acquired from IStat and WorldBank respectively at this point in time. 

We had intially intended to be done forming our final dataset at this point and done with basic analysis of summary statistics and exploratory work, the timeline has sort of flipped upon itself to the point where we have done more of the exploratory work than intended and less of the data preparation.

Our new timeline goals are as follows:

April 17th :

Ethan -> Finalization of merging current data and any remaining exploratory analysis (noting assessment of any data quality issues we've encountered)

Alex -> Finalize OpenRefine cleaning workflows
Normalize country identifiers and time ranges
Restructure fiscal indicators (GDP-related, fiscal balance, debt, government finance)

April 18 - 26th :

Ethan -> Further analysis, production of final visualizations, making future projection, identifying any future work in this subject area

Alex -> Support exploratory analysis related to fiscal capacity, debt burden, and government spending. Assist with visualization design and interpretation

April 27 - May 3:

Together -> Contribute to final analysis write-up, review findings for consistency with original research questions, assist in final documentation and reproducibility checks.

This updated timeline should still allow ample time for the completion of our project as intended with regards to the updates we will be applying to our intended scale.

## Changes to Original Plan

The changes to the plan thus far are relatively minor, we have scaled down the research questions that we are able to answer given the data that is available, accessing unemployment data has been difficult, so barring further data acquistion it will be hard for us to answer questions with regards to this, and provincial level analysis will be more limited than originally planned for. However we intend to supplment the lack of analysis on unemployment data with an exploration of how wages can very across space and industry.

Looking at our feedback, a few changes I made in response were to: Explicitly document our dataset with direct links, clean up descriptions, and define clearer roles. My role is simple yet important; To handle the World Bank data acquisition, cleaning, and prep. Finally, we can address the lack of tags and releases by communicating proper versioning in GitHub prior to each milestone.

## Challenges Thus Far

The primary challenges with IStat as a data source so far has been with the acquistion of data on a smaller scale, most of what is available is only in regards to national level statistics and economic components.

There have thus far been little to no issues with the data quality in regards to the IStat data, it is generally well formatted and complete, with a high degree of consistency, the only data quality issues that are easily identifiable with what IStat provides thus far are in relation to how timely the data is.

Finding World Bank datasets that are both detailed and compatible has been far more challenging than expected. Some sets were comprehensive while not providing consistent indicators that would allow for basic integration.

## Individual Contributions

Ethan has thus far handled most of the work with garnering and performing basic analysis and cleaning on the IStat datasets, as well as doing further planning work on what our final analysis and conclusions will ideally look like.

Alex has been responsible for sourcing, documenting, cleaning, and preparing the World Bank fiscal space dataset, as well as using OpenRefine to standardize and restructure the data for integration. I also contributed to revising the project plan and status report sections to address prior feedback related to dataset clarity, roles, and documentation.