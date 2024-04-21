# import requests

# url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"

# querystring = {"query":"<REQUIRED>"}

# headers = {
# 	"X-RapidAPI-Key": "1e559a1c55mshee1e34f721c08f3p10dc50jsnbbdfbe15b9aa",
# 	"X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())  



# simplified way 




import requests

url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"
querystring = {"query": "<REQUIRED>"}
headers = {
    "X-RapidAPI-Key": "1e559a1c55mshee1e34f721c08f3p10dc50jsnbbdfbe15b9aa",
    "X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Extract and print quotes
print("Quotes:")
for quote in data.get('quote', []):
    print(f"Symbol: {quote.get('symbol')}")
    print(f"Name: {quote.get('name')}")
    print(f"Region: {quote.get('region')}")
    print(f"Country: {quote.get('country')}")
    print(f"Resource Type: {quote.get('resourceType')}")
    print()

# Extract and print news articles
print("News Articles:")
for news in data.get('news', []):
    print(f"Title: {news.get('title')}")
    print(f"Date: {news.get('date')}")
    print(f"URL: {news.get('longURL')}")
    print()

