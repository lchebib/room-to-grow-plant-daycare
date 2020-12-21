from room_to_grow import User, Plant
import users
# set current_user to blank
current_user = None

welcome = input("Welcome! Are you a new user? (Y/N): ")

if welcome = "N":
  existing_user = input("Okay, you are an existing user. Enter your username: ")
  print(f"Welcome back, {existing_user}")
  current_user = existing_user
else:
  print("Let's create your account. ")
  username = input("Enter a username: ")
  name = input("Enter your name: ")
  zip = input("Enter your 5-digit Zip Code (US) or 6-digit Postal Code with no spaces (UK/Canada): ")
  new_user = User(username,name,zip)
  current_user = new_user

plant_name = input("Enter your new plant's name: ")
plant_breed = input(f"Enter in {plant_name}'s breed: ")
current_user.create_plant(plant_name, plant_breed)
response = input("Would you like to add any more plants? Y | N")
if response == "Y":
  plant_name = input("Enter your new plant's name: ")
  plant_breed = input(f"Enter in {plant_name}'s breed: ")
  current_user.create_plant(plant_name, plant_breed)
elif reponse == "N":
  print(f"Okay{new_user.username}, see ya!")
else:
  print("That is not a valid answer")

# print(username)
# print(name)
# print(zip)
# print(plant_name)
# print(plant_breed)
# print(current_user.username)

users.create_user_info()
users.enter_user_info(current_user)


users.create_plant_info()
users.enter_plant_info(current_user.Plants[0])
