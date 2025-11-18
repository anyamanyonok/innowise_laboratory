user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year


def generate_profile(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"


hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)


user_profile = {
    'Name': user_name,
    'Age': current_age,
    'Life stage': life_stage,
    'Hobbies': hobbies
}


print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['Name']}")
print(f"Age: {user_profile['Age']}")
print(f"Life Stage: {user_profile['Life stage']}")


if not user_profile['Hobbies']:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['Hobbies'])}):")
    for hobby in user_profile['Hobbies']:
        print(f"- {hobby}")
print("---")
