import pyshorteners
import time
def shorten_url(url):
    s=pyshorteners.Shortener()
    return s.tinyurl.short(url)

original_url=input("Enter a url link:")
print("__wait a while__")
shortened_url=shorten_url(original_url)
time.sleep(5)
print("Successful Shortened URL:",shortened_url)