# Simple dictionary example

countryInfo = {
    "USA": {"capital": "Washington, D.C.", "population": 331002651},
    "Canada": {"capital": "Ottawa", "population": 40000000},
    "France": {"capital": "Paris", "population": 68000000},
}

print("The capital of America is:", countryInfo["USA"]["capital"])

countryInfo["England"] = {"capital": "London", "population": 56000000}


for country in countryInfo:
    print("The capital of", country, "is:", countryInfo[country]["capital"], "and the population is:", countryInfo[country]["population"])

print("Germany" in countryInfo)
print("England" in countryInfo)
