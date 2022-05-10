import requests
import json

search_title =["TV LG 49"]

for x in search_title:
    response_search = requests.get('https://api.mercadolibre.com/sites/MLA/search?q=' + x)
    item_id =  response_search.json()['results'][0]['id']
    item_search = requests.get('https://api.mercadolibre.com/items/' + item_id)
    out_file = open("myfile.json", "w")     
    json.dump(item_search.json(), out_file)        
    out_file.close() 

    