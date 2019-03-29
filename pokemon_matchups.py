# Returns a dictionary containing details of type matchup of a specific type
# ex. Normal = {'Rock': 0.5, 'Ghost': 0.0, 'Steel':0.5}
def type_matchups(pokemon_type):
	if pokemon_type == "Normal":
		return {'Rock': 0.5, 'Ghost': 0.0, 'Steel':0.5}
	elif pokemon_type == "Fighting":
		return {'Normal': 2.0, 'Flying': 0.5, 'Poison':0.5, 'Rock':2.0, 'Bug':0.5, 'Ghost':0.0, 'Steel':2.0,'Pyschic':0.5,'Ice':2.0,'Dark':2.0,'Fairy':0.5} 
	elif pokemon_type == 'Flying':
		return {'Fighting':2.0, 'Rock':0.5, 'Bug':2.0, 'Steel':0.5,'Grass':2.0,'Electric':0.5}
	elif pokemon_type == 'Poison':
		return {'Poison':0.5, 'Ground':0.5, 'Rock':0.5, 'Ghost':0.5, 'Steel':0.0, 'Grass': 2.0, 'Fairy':2.0}
	elif pokemon_type == 'Ground':
		return {'Flying':0.0, 'Poison':2.0,'Rock':2.0,"Bug":0.5,'Steel':2.0,'Fire':2.0,'Grass':0.5,'Electric':2.0}
	elif pokemon_type == 'Rock':
		return {'Fighting':0.5,'Flying':2.0,'Ground':0.5,'Bug':2.0,'Steel':0.5,'Fire':2.0,'Ice':2.0}
	elif pokemon_type == 'Bug':
		return {'Fighting':0.5,'Flying':0.5,'Poison':0.5,'Ghost':0.5,'Steel':0.5,'Fire':0.5,'Grass':2.0,'Pyschic':2.0,'Dark':2.0,'Fairy':0.5}
	elif pokemon_type == 'Ghost':
		return {'Normal': 0.0,'Ghost':2.0,'Pyschic':2.0,'Dark':0.5}
	elif pokemon_type == 'Steel':
		return {'Rock':2.0,'Steel':0.5,'Fire':0.5,'Water':0.5,'Electric':0.5,'Ice':2.0,'Fairy':2.0}
	elif pokemon_type == 'Fire':
		return {'Rock':0.5,'Bug':2.0,'Steel':2.0,'Fire':0.5,'Water':0.5,'Grass':2.0,'Ice':2.0,'Dragon':0.5}
	elif pokemon_type == 'Water':
		return {'Ground':2.0,'Rock':2.0,'Fire':2.0,'Water':0.5,'Grass':0.5,'Dragon':0.5}
	elif pokemon_type == 'Grass':
		return {'Flying':0.5,'Poison':0.5,'Ground':2.0,'Rock':2.0,'Bug':0.5,'Steel':0.5,'Fire':0.5,'Water':2.0,'Dragon':0.5,'Grass':0.5}
	elif pokemon_type == 'Electric':
		return {'Flying':2.0,'Ground':0.0,'Water':2.0,'Grass':0.5,'Electric':0.5,'Dragon':0.5}
	elif pokemon_type == 'Pyschic':
		return {'Fighting':2.0,'Poison':2.0,'Ghost':0.5,'Pyschic':0.5,'Dark':0.0}
	elif pokemon_type == 'Ice':
		return {'Flying':2.0,'Ground':2.0,'Steel':0.5,'Fire':0.5,'Water':0.5,'Grass':0.5,'Ice':0.5,'Dragon':2.0}
	elif pokemon_type == 'Dragon':
		return {'Steel':0.5,'Dragon':2.0,'Fairy':0.0}
	elif pokemon_type == 'Dark':
		return {'Fighting':0.5,'Ghost':2.0,'Pyschic':2.0,'Dark':0.5,'Fairy':0.5}
	elif pokemon_type == 'Fairy':
		return {'Fighting':2.0,'Poison':0.5,'Steel':0.5,'Fire':0.5,'Dragon':2.0,'Dark':2.0}

# Gets only weaknesses == 0 or strenghts == 1
def sort_type_details(type_details, filter):
	filtered_list = []
	for item in type_details:
		if filter == 0:
			if type_details[item] < 1:
				filtered_list.append(item)
		elif filter == 1:
			if type_details[item] > 1:
				filtered_list.append(item)
	return filtered_list

# Returns two list, first is list of strengths and second is list of weakness
def dual_type_matchup(type_x, type_y):
	type_x_details = type_matchups(type_x)
	type_y_details = type_matchups(type_y)

	type_x_weakness = sort_type_details(type_x_details, 0)
	type_x_strengths = sort_type_details(type_x_details, 1)

	type_y_weakness = sort_type_details(type_y_details, 0)
	type_y_strenghts = sort_type_details(type_y_details, 1)

	# Sets new weakness 
	for item in type_x_weakness:
		if item in type_y_strenghts:
			type_x_weakness.remove(item)
	for item in type_y_weakness:
		if item in type_x_strengths:
			type_y_weakness.remove(item)
	new_type_weakness = type_x_weakness + type_y_weakness
	new_type_strenghts = type_x_strengths + type_y_strenghts
	print(new_type_weakness)
	print(new_type_strenghts)
	return [new_type_strenghts, new_type_weakness]

# pokemon_type = "Fire"
# matchup = type_matchups(pokemon_type)
# filtered_list = sort_type_details(matchup, 1)
# # print(filtered_list)
# dual_type_matchup("Flying", "Ground")