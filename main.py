import json
import requests

with open('config.json', 'r') as file:
    config = json.load(file)

apiToken = config['spoonacular']['apitoken']
baseURL = config['spoonacular']['url']

def get_random_recipe(apiToken,baseURL):
    params = {
        'apiKey': apiToken
    }
    requestURL = baseURL +"recipes/random?number=1&type=maincourse"
    response = requests.get(requestURL, params)
    print(requestURL)
    if response.status_code == 200:
        recipeSTR = response.text
        recipeJSON = json.loads(recipeSTR)
        return recipeJSON['recipes'][0]
    else:
        print('Failed to query properly')

recipe = get_random_recipe(apiToken, baseURL)

print('The recipe found is \n\t Title: ' + recipe['title'] + '\n\tURL: '+ recipe['spoonacularSourceUrl'])