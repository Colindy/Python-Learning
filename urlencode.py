import urllib.parse

url = "Chapple & Seidl"

encodedurl = urllib.parse.quote_plus(url)

print(f"Original URL: {url}")
print(f"Endoded URL: {encodedurl}")