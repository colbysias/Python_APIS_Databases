'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the area of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''

import requests
from pprint import pprint

America_url = "https://restcountries.com/v3.1/name/united%20states%20of%20america"
Canada_url = "https://restcountries.com/v3.1/name/Canada"


America_response = requests.get(America_url)
Canada_response = requests.get(Canada_url)

America_data = America_response.json()
Canada_data = Canada_response.json()


America_population = America_data[0]["population"]
Canada_population = Canada_data[0]["population"]
Population_difference = America_population - Canada_population

print("America's population is " + str(America_population) + " and Canada's Population is " + str(Canada_population) + ". So America has the larger population by " + str(Population_difference) + " people.\n")


America_area = America_data[0]["area"]
Canada_area = Canada_data[0]["area"]
Area_difference = Canada_area - America_area
String_difference = str(Area_difference)



print("America's Area is: " + str(America_area) + " sq. miles")
print("Canada's Area is: " + str(Canada_area) + " sq. miles")
print("This means Canada's Area is " + String_difference + " sq. miles bigger than America\n")

America_name = America_data[0]["name"]["nativeName"]["eng"]["official"]
Canada_name = Canada_data[0]["name"]["nativeName"]["eng"]["official"]
America_capital = America_data[0]["capital"][0]
Canada_capital = Canada_data[0]["capital"][0]


print("America's Native Name is " + str(America_name) + " and it's Capital is " + str(America_capital))
print("Canada's Native Name is " + str(Canada_name) + " and it's Capital is " + str(Canada_capital))

