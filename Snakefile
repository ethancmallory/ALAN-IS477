rule all:
    input:
        "italy_economic_data_cleaned.csv"


rule merge_data:
    input:
        emp="Compensation of employees and its components by industry (IT1,93_1227_DF_DCCN_TNA1_2,1.0).csv",
        gdp="Gross domestic product supply side (IT1,93_498_DF_DCCN_PILT_1,1.0)(1).csv"

    output:
        "italy_economic_data_cleaned.csv"

    shell:
        """
        python ALAN_merge.py "{input.emp}" "{input.gdp}" "{output}"
        """