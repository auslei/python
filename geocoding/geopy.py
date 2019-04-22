import keys 
import geocoder
import pandas as pd

result = {}
failed = []

add = ["100 collins street, melbourne, australia"]

for a in add:
    try:
        print("getting address: {}".format(a))
        g = geocoder.bing(a, key=keys.keys['bing'])
        result[a] = g.json
    except:
        failed.append(a)
        print("error: {}".format(a))

df = pd.Series(result).reset_index()
df.columns = ["address", "detail"]
df.to_csv("address_map.csv")

def latlon(x):
    postcode = ""
    state = ""
    country = ""
    confidence = -1
    lat = -1
    lng = -1
    street = ""
    formated = ""
    try:
        lat = x['lat']
        lng = x['lng']
        postcode = x['postal']
        state = x['state']
        confidence = x['confidence']
        formated = x['raw']['address']['formattedAddress']
        street =  x['raw']['address']['addressLine']
        country = x['raw']['address']['countryRegion']

    except:
        print("oops")
    return [lat, lng, street, postcode, state, country, confidence, formated]

df[['lat', 'lng', 'street', 'state', 'postcode', 'country','confidence', 'formated']] = df.apply(lambda x: pd.Series(latlon(x.detail)), axis=1)

print(df)