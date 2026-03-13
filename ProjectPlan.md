## Overview

For our project we intend to perform analysis on Italian economic development data. Primarily performing time based analysis on how the economy has developed and changed in the period of the last decade or so.

We want to analyze how the composition of different sectors in the nations overall GDP has changed over the last decade, and see if this is different when stratified by province or overall region (i.e. is the north primarily responsible for manufacturing while the south specializes in agriculture?)

We would also like to delve into how unemployment changes across industry/sector and time, contrasting these changes with major real world events, considering things like how COVID-19 or changes in EU law during this period may have impacted the economy.

This will ideally be accomplished by collecting overall economic and sector data from both WorldBank and the Italians Statistics Institute Istat (Istituto Nazionale di Statistica). This data will be aggregated, standardized, or otherwise validated where necessary.

We will then perform the analysis using a range of visualization and exploratory techniques using different Python packages as our primary tools.

## Team

Both team members (Ethan Mallory - ethanm8@illinois.edu and Alex Tapanes - tapanes2@illinois.edu) will assume equal responsibility for completing all required tasks and coordinate to complete the goals as desingated above throughout the duration of the project.

Ethan will additionally handle any issues with maintaining our project's repository via GitHub as he is the owner of the repository.

## Research / Business Questions

How has Italy’s economic structure changed over the past decade, and which sectors have consistently driven GDP growth? -
    Using national data from the World Bank, we can examine long-term trends to identify sectors that have shown consistent growth or decline.

How do economic specialization patterns differ across Italian regions, and have these differences narrowed or intensified over time? -
    Using our more specific regional data from Istat, we analyze whether traditional patterns; Like manufacturing dominance in the North and agriculture or services in the South have and continued to change.

How have unemployment rates changed across industries and regions, and which sectors appear most immune to economic shocks? -
    For this question we shift our focus to identifying industries that recover more quickly or maintain stable employment during periods of disruption.

How did major events like the COVID-19 pandemic impact Italy’s GDP composition and unemployment trends? -
   We assess whether these events caused short-term disruptions or longer-term structural changes in the economy.

Based on historical trends, which sectors and regions are best positioned for future economic growth and employment stability? -
   Using past GDP and unemployment patterns, we explore how historical data can be used to predict future economic outcomes, highlighting regions and industries likely to drive growth or face increased risk.

## Datasets

We intend to access various datasets from two primary databases in order to obtain the data necessary to perform the analysis as it has been described above. 

These will be, as previously noted, WorldBank - https://www.worldbank.org/ext/en/country/italy and Istat - https://www.istat.it/en/.

We currently intend to use the data from WorldBank for more general nationwide analysis and examining trends on a larger scale, while garnering more region specific data from Istat to see how trends in industry weight and unemployment may change spatially.

Aggregation of the data for verifying data validity and consitency across sources will be performed to ensure the data quality of our projects analysis as well.

## Timeline

This project outline is intended to be completed by the 12th of March 2026.

We will ideally finish collecting, organizing, aggregating, and cleaning a majority (assuming no unforseen changes or difficulties) of the data required to begin performing analysis, by the time that our interim status report is due on the 31st of March 2026.

Exploratory analysis of the data will be primarily performed in the period between finishing garnering our data and the first week of april, we intend to finish exploratory analysis and identifying any further issues by the 7th of April 2026.

We will then begin visualization of our data and further analysis in order to draw conclusions before beginning the final preparations of our projects report and presentation. This secondary stage of analysis will ideally be complete by the 14th of April 2026.

The final stage of our project will be to tie up any loose ends in terms of managing our data and completing any additional required analysis before writing our final project report and presentation. We intend to finish drafts of these by the 21st and 23rd of April 2026 respectively, and complete our final drafts of each by the 3rd of May 2026.

## Constraints

Data Availability & Granularity -
With readily available  national-level economic data from the World Bank, regional and provincial data from Istat may be incomplete for certain years or sectors.

Data Integration Across Multiple Sources -
The two data sources differ in scope and structure: World Bank data is national, while Istat data is regional.
Sector classifications, economic definitions, and time intervals might not be perfectly aligned, thus limiting direct dataset merging.

Measurement Differences -
Economic indicators may be reported in different units (percent of GDP vs. absolute values, current vs. constant prices).

Predictive Modeling Limitations -
Forecasts are based solely on historical trends and assume that past patterns provide insight into future outcomes.

Causality & External Influences -
This analysis is purely observational, meaning identified relationships should be interpreted as correlations rather than causal effects.

 
 

## Gaps

Currently the only areas where we anticipate needing additional input to ensure the quality of our project plan and the projects foreseeable proceedings are in whether the databases will provide all the anticipated data we will need as they describe respectively (we anticipate the databases will cover all areas outlined above) and what keys would be ideal for any merging between these datasets, as nation wide and region specific data may not necessariily need to be merged or have an obvious means for doing so if this ends up being required.