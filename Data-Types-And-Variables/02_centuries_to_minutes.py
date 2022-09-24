century = int(input())
century_to_years = century * 100
years_to_days = int(century_to_years * 365.2422)
days_to_hours = years_to_days * 24
hours_to_minutes = days_to_hours * 60
print(f"{century} centuries = {century_to_years} years = {years_to_days} days = {days_to_hours} hours = {hours_to_minutes} minutes")
