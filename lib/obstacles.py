import csv
class Obstacles:
    fileName = ""
    obstacleNames = {}
    obstacleSpaces = {}
    def __init__(self, file):
         self.fileName = file
         self.readCsv()

    def readCsv(self):
        with open(self.fileName, newline='') as csvfile:
            data= csv.reader(csvfile, delimiter=',')
            for row in data:
                position = row[1]
                obstacleName = row[0]
                spaces = row[2]
                self.obstacleNames[position] = obstacleName
                self.obstacleSpaces[position] = spaces

    def getObstacleNames(self):
         return self.obstacleNames

    def getObstacleSpaces(self):
        return self.obstacleSpaces
