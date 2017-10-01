import lib.Obstacles
file = "resources/obstacles.csv"
myObstacles = lib.Obstacles.Obstacles(file)

obstacleNames = myObstacles.getObstacleNames()
obstacleSpaces = myObstacles.getObstacleSpaces()
print(obstacleNames)
print(obstacleSpaces)

key = "32"
if key in obstacleNames:
    print(obstacleNames[key])

if key in obstacleSpaces:
    print(obstacleSpaces[key])
