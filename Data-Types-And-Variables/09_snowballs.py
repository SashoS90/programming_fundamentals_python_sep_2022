number_of_snowballs = int(input())
highest_snowball_value = 0
highest_value_snowball_weight = 0
highest_value_snowball_flight_time = 0
highest_value_snowball_quality = 0

for snowballs in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_flight_time = int(input())
    snowball_quality = int(input())
    current_snowball_value = int((snowball_weight / snowball_flight_time) ** snowball_quality)
    if current_snowball_value > highest_snowball_value:
        highest_snowball_value = current_snowball_value
        highest_value_snowball_weight = snowball_weight
        highest_value_snowball_flight_time = snowball_flight_time
        highest_value_snowball_quality = snowball_quality

print(f"{highest_value_snowball_weight} : {highest_value_snowball_flight_time} = {highest_snowball_value} \
({highest_value_snowball_quality})")
