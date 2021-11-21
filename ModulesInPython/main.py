import geo as g
city = str(input("Enter city: "))

found = False
for c in g.cities:
    if city == c.name:
        print(city, "is in", c.country.name)
        found = True
        break
if not found:
    print(city, "is not found in our database")
