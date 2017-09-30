import lib.Obstacles
file = "resources/obstacles.csv"
myObstacles = lib.Obstacles.Obstacles(file)

data = myObstacles.getObstacles()
print(data)

key = "32"
if key in data:
    print(data[key])
