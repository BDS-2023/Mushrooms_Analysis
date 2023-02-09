import json
import pandas as pd
 
liste_db = ['images', 'observation', 'species_lists', 'names', 'external_sites', 'external_links',
        'herbaria', 'locations', 'comments', 'sequences']


# Opening JSON file
dict_keys = {}
databases_df = {}
for count, names in enumerate(liste_db) : 
    with open(names+'.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        databases_df['{}'.format(names)] = pd.DataFrame(json_object['results'])

df_names = databases_df['names']
df_observation = databases_df['observation']
df_species_lists = databases_df['species_lists']
df_images = databases_df['images']
df_external_sites = databases_df['external_sites']
df_external_links = databases_df['external_links']
df_herbaria = databases_df['herbaria']
df_locations = databases_df['locations']
df_comments = databases_df['comments']
df_sequences = databases_df['sequences']

df_names.head(10)
df_locations.to_json('location.json' )
df_observation.to_json('observation.json' )
df_names.to_json('names.json' )
