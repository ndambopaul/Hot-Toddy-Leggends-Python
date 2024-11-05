
capital_city = {
    "name": "Nairobi, City",
    "country": "Kenya",
    "population": 6500000,
    "famous_for": "Nairobi's capital city is the heart of Africa"
}

# Getting values using the keys
# 1. Using the square brackets
population = capital_city["population"]
country = capital_city["country"]


# 2. Using the .get() method
temperature = capital_city.get("temperature")
print(temperature)

rainfall = capital_city.get("rainfall", "No Data Found")
print(rainfall)