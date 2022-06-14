import requests
import seccodes


from random import randrange

class RequestParser:
    """Is charged to parse user's request and retrieve infos from API"""

    SECRET_KEY = seccodes.key

    def __init__(self):
        self.qreturn = ""
        self.qprocess = ""
        self.matchlist = []
        self.formatted_adress = ""
        self.summary = ""
        self.coordinates = {"lat": 0, "lng": 0}
        self.error = 1
        self.quote = ""
        self.qtoshow = ""

    def string_to_list(self, question):
        """remove some special characters and change string to list"""

        spe_char = [",", ".", "!", "?", "<", ">", ";", "/", ":", "§", "*", '"',
                    "=", "+", "[", "]", "|", "\\", "_", "^", "@", "{", "}",
                    "$", "¨", "£", "¤", "µ", "%", "`"]

        self.qprocess = question
        for characters in spe_char:
            self.qprocess = self.qprocess.replace(characters, " ")
        self.qtoshow = self.qprocess.lstrip()
        self.qtoshow = self.qtoshow.rstrip()
        self.qprocess = self.qprocess.lower()
        self.qprocess = self.qprocess.replace("'", " ' ")
        self.qprocess = self.qprocess.replace("(", " ( ")
        self.qprocess = self.qprocess.split()

    def request_reading(self, stop_word):
        """read the word list to check which word is a stop word and which word
        is a keyword"""

        for q_words in self.qprocess:
            for s_words in stop_word:
                if s_words == q_words:
                    self.matchlist.append(0)
                    break
                elif (stop_word.index(s_words) + 1) == len(stop_word):
                    self.matchlist.append(1)

    def stop_word_remover(self, stop_word):
        """Remove stop words that are not between key words"""

        del self.qprocess[:self.matchlist.index(1)]
        self.qprocess = self.qprocess[::-1]
        self.matchlist = self.matchlist[::-1]
        del self.qprocess[:self.matchlist.index(1)]
        self.qprocess = self.qprocess[::-1]
        for q_word in self.qprocess:
            for s_words in stop_word:
                if s_words == q_word:
                    self.qreturn += ("_" + s_words)
                    break
                elif (stop_word.index(s_words) + 1) == len(stop_word):
                    self.qreturn += ("_" + q_word.capitalize())
        self.qreturn = self.qreturn.replace("_", "", 1)
        self.qreturn = self.qreturn.replace("_'_", "'")
        self.qreturn = self.qreturn.replace("(_", "(")

    def geocoding_researcher(self, json):
        """retrieve coordinates and adress from a json file retrieved
        from Google API"""

        map_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" +\
        "query=" + self.qreturn + "&region=fr&key=" + self.SECRET_KEY
        response = requests.get(map_url)
        map_found = json.loads(response.text)
        found_list = map_found["results"]
        try:
            found_list = found_list[0]
            for key, value in found_list.items():
                if key == "formatted_address":
                    self.formatted_adress = value
                if key == "geometry":
                    self.coordinates = value["location"]
                    self.error = 0
                    break
        except IndexError:
            pass
