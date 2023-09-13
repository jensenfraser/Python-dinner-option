import json
import time
import requests
import os

with open('config.json', 'r') as file:
    config = json.load(file)
try:
    apiToken = config['spoonacular']['apitoken']
    baseURL = config['spoonacular']['url']
except:
    print('Unable to parse the configuration file')

if apiToken == 'CHANGEME':
    print('API token needed in the config.json file!')
    time.sleep(5 * 60)
    exit

def get_random_recipe(apiToken,baseURL):
    params = {
        'apiKey': apiToken,
        'tags' : 'main course'
    }
    requestURL = baseURL +"recipes/random?number=1"
    response = requests.get(requestURL, params)
    print(requestURL)
    if response.status_code == 200:
        recipeSTR = response.text
        recipeJSON = json.loads(recipeSTR)
        return recipeJSON['recipes'][0]
    else:
        print('Failed to query properly')

while True:
    recipe = get_random_recipe(apiToken, baseURL)
    print('The recipe found is \n\t Title: ' + recipe['title'] + '\n\tURL: '+ recipe['spoonacularSourceUrl'])
    open_in_browser = input('Would you like to open the recipe in your browser?\n')
    if open_in_browser == 'y' or open_in_browser == 'yes':
        os.system('start {}'.format(recipe['spoonacularSourceUrl']))

    rerun = input('Would you like a new recipe to be selected?\n')
    if rerun == 'n' or rerun == 'no':
        exit()