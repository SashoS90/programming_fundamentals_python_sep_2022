number_of_water_additions = int(input())
water_tank_capacity = 255
litres_of_water_added = 0

for litres in range(number_of_water_additions):
    litres_poured = int(input())
    if litres_poured > water_tank_capacity:
        print(f"Insufficient capacity!")
        continue
    water_tank_capacity -= litres_poured
    litres_of_water_added += litres_poured
print(litres_of_water_added)