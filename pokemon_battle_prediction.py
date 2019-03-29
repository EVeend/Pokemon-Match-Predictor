import pandas as pd 
import pokemon_matchups as pkmn 

def load_csv(filename):
	dataset = pd.read_csv(filename)
	return dataset

def format_date(combats, pokemon):
	formatted_list = []

	for count in range(len(combats)):
		combats[count][0] = po
	return 0	

combats_file = "Dataset/combats.csv"
pokemon_file = "Dataset/pokemon.csv"

combats_list = load_csv(combats_file)
pokemon_list = load_csv(pokemon_file)

print(combats_list)
print(pokemon_list['id'][3])

