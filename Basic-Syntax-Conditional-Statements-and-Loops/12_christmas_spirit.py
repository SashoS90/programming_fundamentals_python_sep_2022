decorations_qty = int(input())
days_left_until_christmas = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_cost = 0
total_spirit = 0

for current_day in range(1, days_left_until_christmas + 1):
    if current_day % 11 == 0:
        decorations_qty += 2
    if current_day % 2 == 0:
        total_cost += decorations_qty * ornament_set_price
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += (decorations_qty * tree_skirt_price) + (decorations_qty * tree_garland_price)
        total_spirit += 3 + 10
    if current_day % 5 == 0:
        total_cost += decorations_qty * tree_lights_price
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_lights_price + tree_garland_price
if days_left_until_christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
