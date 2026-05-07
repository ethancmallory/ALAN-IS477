import pandas as pd
import sys

emp_file = sys.argv[1]
gdp_file = sys.argv[2]
output_file = sys.argv[3]

#ISTAT comp
employee_compensation = pd.read_csv(emp_file, encoding="utf-8-sig", on_bad_lines="skip")

employee_compensation = employee_compensation[
    employee_compensation["BRKDW_INDUSTRY_NACE_REV2"] == "_T"
][["TIME_PERIOD", "Observation"]].rename(columns={"Observation": "compensation_euros"})

employee_compensation["TIME_PERIOD"] = employee_compensation["TIME_PERIOD"].astype(int)
#ISTAT value add & GDP

value_added = pd.read_csv(gdp_file, encoding="utf-8-sig", on_bad_lines="skip")

value_added = (
    value_added[["TIME_PERIOD", "Observation"]]
    .rename(columns={"Observation": "gross_value_added_euros"})
)

value_added["TIME_PERIOD"] = value_added["TIME_PERIOD"].astype(int)

#merge ISTAT

merged = employee_compensation.merge(value_added, on="TIME_PERIOD", how="outer")

#WB
world_bank = pd.read_csv("World_Bank_Econ.csv", encoding="utf-8-sig")

year_cols = [c for c in world_bank.columns if c.isdigit()]

if "REF_AREA" in world_bank.columns:
    world_bank = world_bank[world_bank["REF_AREA"] == "ITA"]

world_bank = world_bank.melt(
    id_vars=["INDICATOR"],
    value_vars=year_cols,
    var_name="TIME_PERIOD",
    value_name="value"
)

world_bank = world_bank.pivot_table(
    index="TIME_PERIOD",
    columns="INDICATOR",
    values="value"
).reset_index()

world_bank["TIME_PERIOD"] = world_bank["TIME_PERIOD"].astype(int)

#merge ALL

merged = merged.merge(world_bank, on="TIME_PERIOD", how="inner")

#restrict years cause was looking all the way at 90's
merged = merged[(merged["TIME_PERIOD"] >= 2000) & (merged["TIME_PERIOD"] <= 2024)]

merged.to_csv(output_file, index=False)