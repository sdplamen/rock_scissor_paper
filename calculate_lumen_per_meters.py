# The formula for calculating lumens per square meter is:
# Lumens per square meter = Lux × area in square meters
# lux = lumen / m2
# Luminous intensity [cd] = luminous flux [lm] / solid angle [sr]
# Illuminance Lux [lx] = luminous flux [lm] / area [m2]

def calculate_lumens_per_square_meter(lux, area_square_meters):
    lumens_per_square_meter = lux * area_square_meters
    return lumens_per_square_meter

#  Level of illuminance for a specific use case

lux_values = {# 'Residential and Living Spaces':
    'general_living': 100, # - 200, 
    'kitchen': 300, # - 500,
    'reading': 500, # - 1000,

# 'Office Spaces':
    'general_office': 300, # - 500,
    'detailed_office': 500, # - 1000,

# 'Educational and Learning Environments':
    'classroom': 300, # - 500, 
    'library': 500, 

# 'Industrial and Commercial Settings':
    'warehouse': 150, 
    'detailed_mechanical': 500, # - 1000, 
    'retail': 750, # - 1500, 

# 'Outdoor Areas':
    'overcast_day': 1000, # - 2000, 
    'full_daylight': 10000, # - 25000
}

# Example usage:
lux_value = input('Type of lux category space - general_living, kitchen, reading, general_office, detailed_office, classroom, warehouse, library, detailed_mechanical, retail,  overcast_day, full_daylight : ')  # Example lux value
area_value = int(input('Type area value : '))  # Example area in square meters

result = calculate_lumens_per_square_meter(lux_values[lux_value], area_value)
print(f'Lumens per square meter: {result}')

# calculates total lumen level in a room

def calculate_lumen_level(room_area, light_sources):
    total_lumens = 0
    for light in light_sources:
        total_lumens += light['luminous_flux'] * light['quantity']
    return total_lumens / room_area

# Example usage
room_area = int(input('Type area in square meters : '))  # area in square meters
lights = [{'luminous_flux': 800, 'quantity': 4}, {'luminous_flux': 1200, 'quantity': 2}]  # list of dictionaries containing light source details
lumen_level = calculate_lumen_level(room_area, lights)
print(f"The lumen level in the room is {lumen_level} lumens per square meter.")

# lux requierement in a room

lux_value = input('Type of lux category space - general_living, kitchen, reading, general_office, detailed_office, classroom, warehouse, library, detailed_mechanical, retail,  overcast_day, full_daylight : ')  # Example lux value

def calculate_lux_requirement(activity):
    lux_values = {
        "general_living": (100, 200),
        "kitchen": (300, 500),
        "reading": (500, 1000),
        "general_office": (300, 500),
        "detailed_office": (500, 1000),
        "classroom": (300, 500),
        "library": (500),
        "warehouse": (150,),
        "detailed_mechanical": (500, 1000),
        "retail": (750, 1500),
        "overcast_day": (1000, 2000),
        "full_daylight": (10000, 25000)
    }
    if activity in lux_values:
        return lux_values[activity]
    else:
        return "Activity not found."

# Example usage:
activity = lux_value  # Example activity
lux_range = calculate_lux_requirement(activity)
if isinstance(lux_range, str):
    print(lux_range)
else:
    if len(lux_range) == 1:
        print(f"Recommended lux: {lux_range[0]}")
    elif len(lux_range) == 2:
        print(f"Recommended lux range: {lux_range[0]} - {lux_range[1]}")
