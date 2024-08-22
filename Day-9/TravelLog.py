"""Program to add values in a dictionary without changing the code, take input from users and insert the value to the dictionary"""
import os

travel_log_list = [
    {
        'City': 'Bandarban',
        'Place_visited': ['golden temple', 'Boga lake', 'Nilgiri hill', 'Chimbuk hill'],
        'Total_visit': 2
    },

    {
        'City': 'Coxbazar',
        'Place_visited': ['Inani', 'Kolatoli', 'Alikodom'],
        'Total_visit': 1
    },

    {
        'City': 'Sylet',
        'Place_visited': ['Sadapathor', 'Lalakhal', 'Bichanakandi', 'Jaflong', 'Ratargul'],
        'Total_visit': 6
    }
]

# Function to add new travel log


def add_new_city(city, place_visited, number_of_visit):
    new_entry = {}

    new_entry['City'] = city
    new_entry['Place_visited'] = place_visited
    new_entry['Total_visit'] = number_of_visit

    travel_log_list.append(new_entry)


os.system('cls')
new_city = input(
    f'You are entering a new city to your travel log.\nEnter new city: ')

new_place_visited = input(f'Enter the places you visited: ').split(', ')

total_visits = int(
    input(f'Enter the number of times you visited these places: '))
os.system('cls')

add_new_city(new_city, new_place_visited, total_visits)

print(f"I've been to {travel_log_list[3]['City']} {
      travel_log_list[3]['Total_visit']} times.")
print(f'My favorite place was {travel_log_list[3]['Place_visited'][0]}.')
