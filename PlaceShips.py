import csv
from random import randint


class PlaceShips:
    def __init__(self):

        #Matrix to place Ship
        self.shipMatrix = [["   " for x in range(10)] for y in range(10)]

        #Matrix to check shot
        self.checkMatrix = [["   " for x in range(10)] for y in range(10)]
        self.alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','a','b','c','d','e','f','g','h','i','j']

        #Convert aphalbet to integer
        self.dict = {'A':0,'a':0,'b':1,'B':1,'c':2,'C':2,'D':3,'d':3,'e':4,'E':4,'F':5,'f':5,'G':6,'g':6,'H':7,'h':7
                     ,'I':8,'i':8,'J':9,'j':9}

        #Number of grid of ships
        self.shipDict = {'Carrier': 5, 'Battleship': 4, 'Destroyer': 4, 'Submarine': 3, 'Cruiser': 2}

        #Check Ship status and name
        self.Carrier = ['Floating', 5, 'Carrier']
        self.Battleship = ['Floating', 4, 'BattleShip']
        self.Destroyer = ['Floating', 4, 'Destroyer']
        self.Submarine = ['Floating', 3, 'Submarine']
        self.Cruiser = ['Floating', 2, 'Cruiser']
        self.shipsPosition = []

    def printShipMatrix(self):
        print("   0    1    2    3    4    5    6    7    8    9  ")
        for i in range(10):
            print(self.alpha[i], end="")
            for j in range(10):
                print(self.shipMatrix[i][j], "|", end="")
            print("")

    def printBothMatrix(self):
        x = ' '
        b='-'
        print(b*15,"Your Ship Position",b*15,x*5,b*18,"Your Shot",b*18)
        print(
            "   0    1    2    3    4    5    6    7    8    9         0    1    2    3    4    5    6    7    8    9  ")
        for i in range(10):
            print(self.alpha[i], end="")
            for j in range(10):
                print(self.shipMatrix[i][j], "|", end="")
            print(x * 4, self.alpha[i], end="")
            for k in range(10):
                print(self.checkMatrix[i][k], "|", end="")
            print('')

    #Fill a ship from input for player
    def fillaShip(self, shipType):
        done = False
        while (done != True):
            while (1):
                ship = input("Position for " + shipType[2] + ":")
                if ship[0] in self.alpha and int(ship[1]) in range(0, 10) and len(ship) == 2:
                    break
                else:
                    print("Wrong input")

            place = input("V for vertically placing, H for horizontally placing:")
            if place == 'V' or place == 'v':
                ship = str(self.dict[ship[0]]) + str(ship[1])
                shipPosition = []
                for i in range(shipType[1]):
                    if i + int(ship[0]) > 9:
                        shipPosition = []
                        break
                    else:
                        shipPosition.append(str(int(ship[0]) + i) + str(int(ship[1])))
                if len(list(set(shipPosition).difference(self.shipsPosition))) == shipType[1]:
                    for i in range(len(shipPosition)):
                        shipType.append(shipPosition[i])
                        self.shipsPosition.append(shipPosition[i])
                    for i in range(3, len(shipType)):
                        self.shipMatrix[int(shipType[i][0])][int(shipType[i][1])] = shipType[2][0:3]
                    done = True
                else:
                    print('Cannot place that position')
            elif place == 'H' or place == 'h':
                ship = str(self.dict[ship[0]]) + str(ship[1])
                shipPosition = []
                for i in range(shipType[1]):
                    if i + int(ship[1]) > 9:
                        break
                    else:
                        shipPosition.append(str(int(ship[0])) + str(int(ship[1]) + i))
                if len(list(set(shipPosition).difference(self.shipsPosition))) == shipType[1]:
                    for i in range(len(shipPosition)):
                        shipType.append(shipPosition[i])
                        self.shipsPosition.append(shipPosition[i])
                    for i in range(3, len(shipType)):
                        self.shipMatrix[int(shipType[i][0])][int(shipType[i][1])] = shipType[2][0:3]
                    done = True
                else:
                    print('Cannot place that position')
            else:
                print('Cannot place that postion')

    #Place a ship from file
    def placeShip(self, shipType, ship, place):
        if place == 'V' or place == 'v':
            ship = str(self.dict[ship[0]]) + str(ship[1])
            shipPosition = []
            for i in range(shipType[1]):
                if i + int(ship[0]) > 9:
                    shipPosition = []
                    break
                else:
                    shipPosition.append(str(int(ship[0]) + i) + str(int(ship[1])))
            if len(list(set(shipPosition).difference(self.shipsPosition))) == shipType[1]:
                for i in range(len(shipPosition)):
                    shipType.append(shipPosition[i])
                    self.shipsPosition.append(shipPosition[i])
                for i in range(3, len(shipType)):
                    self.shipMatrix[int(shipType[i][0])][int(shipType[i][1])] = shipType[2][0:3]
            else:
                print('Cannot place that position')
        elif place == 'H' or place == 'h':
            ship = str(self.dict[ship[0]]) + str(ship[1])
            shipPosition = []
            for i in range(shipType[1]):
                if i + int(ship[1]) > 9:
                    break
                else:
                    shipPosition.append(str(int(ship[0])) + str(int(ship[1]) + i))
            if len(list(set(shipPosition).difference(self.shipsPosition))) == shipType[1]:
                for i in range(len(shipPosition)):
                    shipType.append(shipPosition[i])
                    self.shipsPosition.append(shipPosition[i])
                for i in range(3, len(shipType)):
                    self.shipMatrix[int(shipType[i][0])][int(shipType[i][1])] = shipType[2][0:3]
            else:
                print('Cannot place that position')
        else:
            print('Cannot place that postion')

    #Fill all ships from input for player
    def fillAllShips(self):
        self.fillaShip(self.Carrier)
        self.printShipMatrix()
        self.fillaShip(self.Battleship)
        self.printShipMatrix()
        self.fillaShip(self.Destroyer)
        self.printShipMatrix()
        self.fillaShip(self.Submarine)
        self.printShipMatrix()
        self.fillaShip(self.Cruiser)
        self.printShipMatrix()

    #Fill all ships by File for computer
    def fillShipByFile(self):
        with open('ship-placement.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
            for row in readCSV:
                if row[0] == 'Carrier':
                    shipType = self.Carrier
                elif row[0] == 'Battleship':
                    shipType = self.Battleship
                elif row[0] == 'Destroyer':
                    shipType = self.Destroyer
                elif row[0] == 'Submarine':
                    shipType = self.Submarine
                elif row[0] == 'Cruiser':
                    shipType = self.Cruiser
                else:
                    print('Wrong format, Can not place', row[0])
                    break
                ship = row[1]
                place = row[2]
                self.placeShip(shipType, ship, place)

