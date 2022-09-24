party_size = int(input())
days = int(input())
gold_stash = 0
food_cost = 2
water_cost = 3
killing_boss_monster = 20

for day in range(1, days + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    if day % 3 == 0:
        gold_stash -= party_size * water_cost
    if day % 5 == 0:
        gold_stash += party_size * killing_boss_monster
        if day % 3 == 0:
            gold_stash -= party_size * food_cost
    gold_stash += 50
    gold_stash -= party_size * food_cost
coins_per_companion = int(gold_stash // party_size)
print(f"{party_size} companions received {coins_per_companion} coins each.")