import csv

from requests_html import HTMLSession

s = HTMLSession()

def get_producers_url():

    url = "https://aurendezvousdesnormands.fr/partenaires?code=&lieu_recherche="
    list = []
    r = s.get(url)
    producers = r.html.find("div.liste-inscrits-wrap ul li")
    prod_name = r.html.find("div.inscrit-name h2 a")
    # first = True

    for i in prod_name:
        list.append("https://aurendezvousdesnormands.fr" + str(i.attrs["href"]))
    return list

def parse_producer(url):
    
    r = s.get(url)
    cat_list = []
    contact = []
    user_cat = {}

    name = r.html.find("div.fiche-name h1", first=True).text
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

    #relation producteur métiers
    #mauvaise méthode, problème avec les clés pour la rentré en BDD.
    #voir pour peupler un dico préformaté pour que toutes les lignes correspondent
    #essayer de chopper toutes les catégories pour les organiser dans un dico prérempli puis remplir le dico à ce moment
    for i in r.html.find("div.fiche-cate-produits ul li"):
        cat_list.append(i.text)
    for i in cat_list:
        user_cat[i] = name

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
        "addr" : addr,
        "cp" : cp,
        "ville" : ville,
        "dept" : dept,
        "contact" : contact,
        "lat" : lat,
        "lon" : lon
    }
    return producer, user_cat

def save_user_csv(datas):
    keys = datas[0].keys()
    with open("producteurs.csv", "w", newline="", encoding="utf-8") as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(datas)

def save_user_link_csv(datas):
    keys = datas[0].keys()
    with open("products.csv", "w", newline="", encoding="utf-8") as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(datas)

urls = get_producers_url()
users = []
users_link = []
for url in urls:
    users.append(parse_producer(url)[0])
    users_link.append(parse_producer(url)[1])
    print(users)
    print(users_link)
save_user_csv(users)
save_user_link_csv(users_link)
