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


conn = sqlite3.connect("users.db")

c = conn.cursor()

# c.execute("CREATE TABLE users (first_name TEXT, zip_code TEXT);")

n = input("Please enter your name: ")
z = input("Please enter your zip/area code: ")

def plantCreator(name, breed):
  newPlant = Plant(name,breed )
  query = "INSERT INTO users SELECT  (?)"

  c.execute(query, name, breed)

def insertUser(n,z):
  # data = (name,zip, newPlant)
  query = "INSERT INTO users VALUES (?,?,?)"
  c.execute(query,n, z, plantCreator())
  # wrap in a funtion

conn.commit()
conn.close()