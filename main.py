from room_to_grow import User, Plant

username = input("Enter your username: ")
name = input("Enter your name: ")
zip = input("Enter your 5-digit Zip Code (US) or 6-digit Postal Code with no spaces (UK/Canada): ")
currentUser = User(username,name,zip)

plant_name = input("Enter your new plant's name: ")
plant_breed = input(f"Enter in {plant_name}'s breed: ")
currentUser.create_plant(plant_name, plant_breed)

print(username)
print(name)
print(zip)
print(plant_name)
print(plant_breed)
print(currentUser)
