# Description: This script fetches information for a specified Pokemon from the PokeAPI.
import requests

# Define the function to fetch Pokemon information from the PokeAPI.
def get_pokemon_info(pokemon_name):
    """
    Fetches information for a specified Pokemon from the PokeAPI.
    Args:
        pokemon_name (str): The name or PokéDex number of the Pokemon.
    Returns:
        dict: A dictionary containing the Pokemon information if successful, None otherwise.
    """
    # Construct the PokeAPI URL for the specified Pokemon.
    POKE_API_URL = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower().strip()}'
    # Send a GET request to the PokeAPI to fetch the Pokemon information.
    print(f"Getting information for {pokemon_name}...")
    response = requests.get(POKE_API_URL)

    if response.status_code == 200:
        print("Information fetched successfully!")
        return response.json()
    else:
        print(f"Failed to fetch information. Response code: {response.status_code}")
        return None
    
if __name__ == '__main__':
    # Example usage
    info = get_pokemon_info("butterfree")
    print(info)  # Output the information for Butterfree