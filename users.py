import sqlite3
# information we need: user name, user location, user instances of plants

# users
  # name
  # location
  # plants
    # breed
    # name

#need to to create two tables one for our users and one for out plants
#each plant instance will have a property tied to the user so when we want to recall a certain plant we know which user it belongs to


# c = conn.cursor()
# c.execute("CREATE TABLE users (username TEXT);")


# def plantCreator(name, breed):
#   newPlant = Plant(name,breed )
#   query = "INSERT INTO users SELECT  (?)"

#   c.execute(query, name, breed)

# def insertUser(user):
#   # data = (name,zip, newPlant)
#   query = "INSERT INTO users VALUES (?,)"
#   c.execute(query,user)

# conn.commit()
# conn.close()

conn = sqlite3.connect("users.db")

def create_user_info():
  c = conn.cursor()
  c.execute('CREATE TABLE IF NOT EXISTS user_info (username TEXT, name TEXT, zipcode BLOB)')
  c.close()

def enter_user_info(user):
  c = conn.cursor()
  data = (user.username, user.name, user.location)
  query = "INSERT INTO user_info VALUES (?,?,?)"
  c.execute(query, data)
  conn.commit()
  c.close()

def create_plant_info():
  c = conn.cursor()
  c.execute('CREATE TABLE IF NOT EXISTS plant_info (name TEXT, breed TEXT, owner TEXT)')
  c.close()

def enter_plant_info(plant):
  c = conn.cursor()
  data = (plant.name, plant.breed, plant.owner)
  query = "INSERT INTO plant_info VALUES (?,?,?)"
  c.execute(query, data)
  conn.commit()
  c.close()