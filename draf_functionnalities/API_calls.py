import requests
import json

#Variables URL
APIKey = "ati45mja2ige4zv6u021ri7fto6dxovr"
headers = {'user-agent': 'Chrome/109.0.0.0'}
url_images = 'https://mushroomobserver.org/api2/images?&format=json&detail=high'
url_observation = 'https://mushroomobserver.org/api2/observations?&format=json&detail=high'
url_species_lists = 'https://mushroomobserver.org/api2/species_lists?&format=json&detail=high'
url_names = 'https://mushroomobserver.org/api2/names?&format=json&detail=high'
url_external_sites = 'https://mushroomobserver.org/api2/external_sites?&format=json&detail=high'
url_external_links = 'https://mushroomobserver.org/api2/external_links?&format=json&detail=high'
url_herbaria = 'https://mushroomobserver.org/api2/herbaria?&format=json&detail=high'
url_locations = 'https://mushroomobserver.org/api2/locations?&format=json&detail=high'
url_comments = 'https://mushroomobserver.org/api2/comments?&format=json&detail=high'
url_sequences = 'https://mushroomobserver.org/api2/sequences?&format=json&detail=high'


#APIs calls
liste_db = ['images', 'observation', 'species_lists', 'names', 'external_sites', 'external_links',
        'herbaria', 'locations', 'comments', 'sequences']

liste_url  = [url_images, url_observation, url_species_lists, url_names,url_external_sites, 
        url_external_links, url_herbaria, url_locations, url_comments, url_sequences]

#Exctraction of the pagination information
pagination = {}
for database, url in zip(liste_db, liste_url):
        pagination['max_page_{}'.format(database)] = requests.get(url, headers = headers).json()['number_of_pages']

print(pagination)

#Data extraction
response_API_results = {}
response_API_results = {}
for database, url in zip(liste_db, liste_url):
        for page in range(1,pagination['max_page_{}'.format(database)]):
                API_request = requests.get(url, headers = headers, params={'page': page})
                response_API_results['results'] = API_request.json()['results']
                if API_request.status_code != 200 :
                        print('code erreur :', API_request.status_code)
                print('itération')
        data_var = json.dumps(response_API_results)
        writeFile = open(database+'.json', 'w')