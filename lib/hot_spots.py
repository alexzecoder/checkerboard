import csv


class Hotspots(object):
    fileName = ""
    spots = {}
    points = {}

    def __init__(self, file):
         self.fileName = file
         self.readCsv()

    def readCsv(self):
        with open(self.fileName) as csvfile:
            data= csv.reader(csvfile, delimiter=',')
            for row in data:
                square = row[1]
                description = row[0]
                squares_to_move = row[2]
                self.spots[square] = description
                self.points[square] = squares_to_move

    def get_spot_names(self):
         return self.spots

    def get_squares_to_move(self):
        return self.points
