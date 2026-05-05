# %%
import pandas as pd

# %%
employee_compensation = pd.read_csv("Compensation of employees and its components by industry (IT1,92_1225_DF_DCCN_ANA1_2,1.0).csv",encoding="utf-8-sig", quotechar="'", on_bad_lines="skip")
employee_compensation = employee_compensation[employee_compensation["BRKDW_INDUSTRY_NACE_REV2"] == "_T"][["TIME_PERIOD", "Observation"]].rename(columns={"Observation": "compensation_euros"})
employee_compensation

# %%
value_added  = pd.read_csv("Output and value added by industry (IT1,92_1225_DF_DCCN_ANA1_1,1.0).csv", encoding="utf-8-sig", on_bad_lines="skip")
value_added   = value_added[value_added["BRKDW_INDUSTRY_NACE_REV2"] == "_T"][["TIME_PERIOD", "Observation"]].rename(columns={"Observation": "gross_value_added_euros"})
value_added

# %%
gdp_supply_side  = pd.read_csv("Gross domestic product supply side (IT1,93_498_DF_DCCN_PILT_1,1.0).csv", encoding="utf-8-sig", on_bad_lines="skip")
gdp_supply_side  = gdp_supply_side[gdp_supply_side["REF_AREA"] == "IT"][["TIME_PERIOD", "Observation"]].rename(columns={"Observation": "gdp_euros"})
gdp_supply_side

# %%
world_bank  = pd.read_csv("World_Bank_Econ.csv", encoding="utf-8-sig")
world_bank

# %%
year_cols = [c for c in world_bank.columns if c.isdigit()]
world_bank = world_bank[world_bank["REF_AREA"] == "ITA"].melt(id_vars=["INDICATOR"], value_vars=year_cols, var_name="TIME_PERIOD", value_name="value")
world_bank = world_bank.pivot_table(index="TIME_PERIOD", columns="INDICATOR", values="value").reset_index()
world_bank["TIME_PERIOD"] = world_bank["TIME_PERIOD"].astype(int)

# %%
merged = employee_compensation.merge(value_added, on="TIME_PERIOD", how="outer")

# %%
merged = merged.merge(gdp_supply_side, on="TIME_PERIOD", how="outer")

# %%
merged = merged.merge(world_bank, on="TIME_PERIOD", how="outer")
merged

# %%
merged.to_csv("italy_economic_data.csv", index=False)


