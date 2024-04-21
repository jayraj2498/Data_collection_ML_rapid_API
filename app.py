import requests
import json
from tabulate import tabulate

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    "X-RapidAPI-Key": "1e559a1c55mshee1e34f721c08f3p10dc50jsnbbdfbe15b9aa",
    "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

# Extract JSON content from response
data = response.json()

# Convert to list of lists
table = []
headers = data['response'][0].keys()
table.append(headers)
for item in data['response']:
    row = [item[key] for key in headers]
    table.append(row)

# Print as table
print(tabulate(table, headers="firstrow", tablefmt="grid"))
