# get public license data from City of Chicago's data portal
import ssl
import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)

json_file = "rr23-ymwb"

results = client.get(json_file, limit=500)
# convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df.info()

vehicles = results_df[["public_vehicle_number", "vehicle_fuel_source"]]
print("Public vehicle numbers and fuel sources:")

vehicles.info()
vehicles_by_fuel = vehicles.groupby("vehicle_fuel_source").count()
print(vehicles_by_fuel)