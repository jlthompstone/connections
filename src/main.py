import json

file = open("data/puzzles.json", "r")
puzzle_data = json.load(file)

def check_selection(selected_words):
    selected_categories = []

    for i in range(4): 
        for j in range(4):
            if selected_words[i] in puzzle_data[0]["groups"][j]["words"]:
                selected_categories.append(puzzle_data[0]["groups"][j]["difficulty"])

    if selected_categories[0] == selected_categories[1] == selected_categories[2] == selected_categories[3]:
        return True
    else:
        return False

selection = []

for i in range(4):
    selection.append(input("Enter a word: "))

print(str(check_selection(selection)))