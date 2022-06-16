import json

from requests_html import HTMLSession

s = HTMLSession()

def get_producers_url():

    url = "https://aurendezvousdesnormands.fr/partenaires?code=&lieu_recherche="
    list = []
    r = s.get(url)
    prod_name = r.html.find("div.inscrit-name h2 a")

    for i in prod_name:
        list.append("https://aurendezvousdesnormands.fr" + str(i.attrs["href"]))
    return list

def parse_producer(url):
    
    r = s.get(url)
    cat = []
    contact = []

    name = r.html.find("div.fiche-name h1", first=True).text
    for i in r.html.find("div.fiche-cate-produits ul li"):
        cat.append(i.text)
    try:
        addr1 = r.html.find("span.address-line1", first=True).text
        addr2 = r.html.find("span.address-line2", first=True).text
        cp = r.html.find("span.postal-code", first=True).text
    except:
        addr1 = ""
        addr2 = ""
        cp = ""
    local = r.html.find("div.fiche-place p", first=True).text
    for i in r.html.find("div.fiche-contact a"):
        contact.append(i.text)
    contact = " ".join(str(e) for e in contact) 
    lat = r.html.find("div#mapfiche", first=True).attrs["data-geo-lat"]
    lon = r.html.find("div#mapfiche", first=True).attrs["data-geo-lon"]

    #some cleanup
    if addr2:
        addr = addr1 + " " + addr2
    else:
        addr = addr1
    local = local.split(", ")
    try:
        ville = local[0].replace("&#039;", "'")
    except:
        ville = ""
    try:
        dept = local[1].replace("&#039;", "'")
    except:
        dept = ""

    producer = {
        "name" : name,
        "cat" : cat,
        "addr" : addr,
        "cp" : cp,
        "ville" : ville,
        "dept" : dept,
        "contact" : contact,
        "lat" : lat,
        "lon" : lon
    }
    return producer

def save_user_json(datas):
    with open("producteurs.json", "w", encoding="utf-8") as file:
        json.dump(datas, file, ensure_ascii=False)

urls = get_producers_url()
users = []
users_link = []
for url in urls:
    users.append(parse_producer(url))
    print(url)
save_user_json(users)
