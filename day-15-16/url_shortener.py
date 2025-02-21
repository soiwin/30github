import pyshorteners


pys = pyshorteners.Shortener()

url = input('Enter URL: ')

short_url = pys.tinyurl.short(url)

print(short_url)
