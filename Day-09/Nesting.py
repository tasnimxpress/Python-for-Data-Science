"Nesting dictionary"

capitals = {
    'Bangladesh': 'Dhaka',
    'Germany': 'Berlin',
    'Australia': 'Sydney'
}

# nesting a list in a dictionary
cities = {
    'Bangladesh': ['Dhaka', 'Dinajpur', 'Kurigram'],
    'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
}

# nesting a list within a dictionary in a dictionary
travel_log = {
    'Bandarban': {'cities_visited': ['golden temple', 'Boga lake', 'Nilgiri hill', 'Chimbuk hill'], 'total_visit': 2},
    'Coxbazar': {'cities_visited': ['Inani', 'Kolatoli', 'Alikodom'], 'total_visit': 1}
}

print(travel_log)


# nesting multiple dictionary inside a list
travel_log_list = [
    {
        'City': 'Bandarban',
        'Place_visited': ['golden temple', 'Boga lake', 'Nilgiri hill', 'Chimbuk hill'],
        'total_visit': 2
    },

    {
        'City': 'Coxbazar',
        'Place_visited': ['Inani', 'Kolatoli', 'Alikodom'],
        'total_visit': 1
    },

    {
        'City': 'Sylet',
        'Place_visited': ['Sadapathor', 'Lalakhal', 'Bichanakandi', 'Jaflong', 'Ratargul'],
        'Total_visited': 6
    }
]
