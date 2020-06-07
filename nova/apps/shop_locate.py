from apps.base import App as BaseApp


# for testing purposes i'll mimic the future database
stores = {
    "DOUALA": [
        "Ecotex, AKWA, around Station Totale near Ancien Dalip",
        "CICAM Store, Boulevard du President Ahmadou Ahidjo, new MAHIMA",
        "Laking Textile, BEPANDA, around Petit Marche crossroad",
        "Laking Textile, New-Bell, Avenue Douala Manga Bell",
        "Shop Center, NDOKOTI, next to BICEC going towards \
        PK8 from NDOKOTI crossroad",
        "Laking Textile, Madagascar, at Rond-Point Dakar"
    ],
    "YAOUNDE": [
        "Ecotex, Madagascar, around Mokolo Market",
        "Laking Textile, Avenue KENNEDY",
        "Laking Textile, BIYEM ASSI, Acacia crossroad",
        "Laking Textile, MVOG-MBI, near the chapel",
        "Laking Textile, MENDONG, at MENDONG's market crossroad"
    ],
    "LIMBE": [ "Laking Textile, Avenue of Churches, around Down Beach" ],
    "BAFOUSSAM": ["Laking Textile, front Marche A"],
    "BAMENDA": ["Laking Textile, Commercial Avenue, faced to COMECI around MTN"],
    "FOUMBAN": ["Laking Textile, Town hall, near CAMTEL"],
    "SANGMELIMA": ["Laking Textile, Independence Square, around Hotel AFAMBA"],
    "BERTOUA": ["Laking Textile, CAMPOST crossroad, beside the cathedral"],
    "EBOLOWA": ["Laking Textile, Montee GMI, around BUCA Travel Agency"],
    "NGAOUNDERE": ["Laking Textile, Cameroon Breweries, not far from MTN"],
    "KOUSSERIE": ["Laking Textile, Independence Square"],
    "MAROUA": ["Laking Textile, Next to QUIFFEROU"],
    "GAROUA": [
        "Laking Textile, Bank Avenue, comming from YELWA",
        "Shop Center, CICAM Factory comming from NJAMBOUTOU crossroad"
    ]
}


class App(BaseApp):
    """
    Shop localization feature
        :: apps.shop_localize.App extends apps.base.App
    """
    def __init__(self):
        self.template_filename = "templates\\locate_shop.json"
        self.__context = {}
        self.__responses = self.__load_responses()
        self.intents = self.__load_intents()

    def execute(self, doc):
        """::overwrites apps.base.App.execute method"""
        intent = doc._.intent
        try:
            return getattr(self, intent)(doc)
        except AttributeError:
            raise AttributeError(f"Intent '{intent}' do not have a \
                                handler for app 'shop_locate'")

    @staticmethod
    def __get_store_for(town_name):
        """Return all stores for a given town of none if not found"""
        _raw = stores.get(town_name.upper(), None)
        if _raw:
            _temp = "\n".join(_raw)
            return f"In {town_name}, the stores locations are :\n" + _temp
        else:
            return _raw

    def locate_shop(self, doc):
        """Locate various shops or shops of a given city..."""
        # get the first location entity in the doc
        gpe = None
        for ent in doc.ents:
            if ent.label_ == "GPE":
                gpe = ent.text
                break
        # print(gpe)

        if gpe:
            _response = None
            if gpe.lower() == "cameroon":
                _stores = ", ".join(list(set(stores.keys())))
                _response = "CICAM group has stores in: "+_stores
            else:
                _response = self.__get_store_for(gpe)

            if _response != None:
                return {
                    "message": _response,
                    "state": 1
                }
            else:
                return {
                    "message": f"Sorry but we have no stores in {gpe}",
                    "state": 0
                }
        else:
            return {
                "message": "where are you looking for the stores?",
                "state": 0
            }
        

    def locate_item(self, doc):
        for ent in doc.ents:
            print(ent.text, ent.label_)
        return {
            "message": "let me check the items in the stores...",
            "state": 1
        }