import requests


def fetch_meal():
    url = "https://api.freeapi.app/api/v1/public/meals/meal/random"
    response = requests.get(url)
    data = response.json()
    return data

# Fetch a random meal from the API
data = fetch_meal()
meal = data["data"]

name = meal["strMeal"]
print("Meal Name:", name)
print()

instructions = meal["strInstructions"]
print("Meal Instructions:\n", instructions)

print()
youtube_link = meal["strYoutube"]
print("YouTube Link: ", youtube_link)


print()


meal_ingredients = []

for i in range(1, 21):
    meal_ingredients.append(meal[f"strIngredient{i}"])

print(meal_ingredients)    