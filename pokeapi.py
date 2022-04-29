from urllib import response
from xmlrpc.client import ResponseError
import requests


def get_pokemon_info(name):
    """
    Gets a dictionary of information from the PokeApi for a specified Pokemon

    :param name: Pokemon's name (or Poke index) 
    """

    print("Getting Pokemon information...", end='')
    if name is None:
        return


    name = name.strip().lower()

    if name == '':
        return

    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
    response = requests.get(URL)

    if response.status_code == 200:
        print('success')
        return response.json() #Convert response body to a dictionary
    else: 
        print('failed. Response code:', response.status_code)
        return