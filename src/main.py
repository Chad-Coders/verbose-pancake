import json

from justwatch import JustWatch

just_watch = JustWatch(country='SE')

results = just_watch.search_for_item(query='avengers')

with open('json_data.json', 'w') as outfile:
    json.dump(results, outfile)
