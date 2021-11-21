class Country:
    def __init__(self, name):
        self.name = name

class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

cities = [City("Cairo", Country("Egypt")),
         City("Paris", Country("France")),
         City("Istanbul", Country("Turkey")),
         ]
