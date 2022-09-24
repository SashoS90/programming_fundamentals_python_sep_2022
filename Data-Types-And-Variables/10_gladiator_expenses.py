lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_shields_count = lost_fights_count // 6
broken_helmets_count = lost_fights_count // 2
broken_armors_count = broken_shields_count // 2
broken_swords_count = lost_fights_count // 3
total_repair_cost = (broken_helmets_count * helmet_price) + (broken_swords_count * sword_price) + \
                    (broken_shields_count * shield_price) + (broken_armors_count * armor_price)
print(f"Gladiator expenses: {total_repair_cost:.2f} aureus")