budget = float(input())
flour_kg_price = float(input())
eggs_price_per_pack = flour_kg_price * 0.75
milk_price_per_liter = flour_kg_price * 1.25 / 4
cost_for_one_bread = flour_kg_price + eggs_price_per_pack + milk_price_per_liter
breads_counter = 0
colored_eggs_counter = 0
while budget >= cost_for_one_bread:
    budget -= cost_for_one_bread
    breads_counter += 1
    colored_eggs_counter += 3
    if breads_counter % 3 == 0:
        colored_eggs_counter -= breads_counter - 2
print(f"You made {breads_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
