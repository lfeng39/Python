import requests

p = []
for i in range(1,50):
    if 50 % i == 0:
        pass
    else:
        p.append(i)
print(p)

wiki_http = "https://www.facebook.com"
wiki_page = requests.get(wiki_http)
print(wiki_page)