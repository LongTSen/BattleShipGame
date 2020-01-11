from PlaceShips import PlaceShips
from random import randint

class gamePlay():
    def __init__(self):
        #Creates object for player
        self.yourShip = PlaceShips()

        #Creates object for computer
        self.computerShip = PlaceShips()

        #Places Ships for computer
        self.computerShip.fillShipByFile()
        self.yourShip.printShipMatrix()

        #Places Ships for player
        self.yourShip.fillAllShips()
        self.hit = False
        self.sunk = False
        self.listOfShot = []    #list of previous shots
        self.potentialShot = []  #Potential shots for computer after hit
        self.direction = ''     #Direction: Horizontal and Vertical
        self.exclude = []

    #Checks if ships are sunk
    def checkSunk(self, checkPlayer,player):
        if len(checkPlayer.Carrier) == 3 and checkPlayer.Carrier[0] == 'Floating':
            checkPlayer.Carrier[0] = 'Sunk'
            if player == 2:
                print("Computer sink your Carrier")
                self.hit = False
                self.potentialShot.clear()
                self.direction = ''
            else:
                print('You sink their Carrier')

        if len(checkPlayer.Battleship) == 3 and checkPlayer.Battleship[0] == 'Floating':
            checkPlayer.Battleship[0] = 'Sunk'
            if player==2:
                print("Computer sink your BattleShip")
                self.hit = False
                self.potentialShot.clear()
                self.direction = ''
            else:
                print('You sink their BattleShip')

        if len(checkPlayer.Destroyer) == 3 and checkPlayer.Destroyer[0] == 'Floating':
            checkPlayer.Destroyer[0] = 'Sunk'
            if player==2:
                print("Computer sink your Destroyer")
                self.hit = False
                self.potentialShot.clear()
                self.direction = ''
            else:
                print("You sink their Destroyer")

        if len(checkPlayer.Submarine) == 3 and checkPlayer.Submarine[0] == 'Floating':
            checkPlayer.Submarine[0] = 'Sunk'
            if player==2:
                print("Computer sink your Submarine")
                self.hit = False
                self.potentialShot.clear()
                self.direction = ''
            else:
                print("You sink thier Submarine")

        if len(checkPlayer.Cruiser) == 3 and checkPlayer.Cruiser[0] == 'Floating':
            checkPlayer.Cruiser[0] = 'Sunk'
            if player==2:
                print("Computer sink your Cruiser")
                self.hit = False
                self.potentialShot.clear()
                self.direction = ''
            else:
                print("You sink their Cruiser")

    #Check if hit a ship
    def checkShot(self, shot, player):
        if player == 1:
            checkPlayer = self.computerShip
            myMatrix = self.yourShip
            shot = str(checkPlayer.dict[shot[0]]) + str(shot[1])
        else:
            checkPlayer = self.yourShip
            myMatrix = self.computerShip
        if shot in checkPlayer.shipsPosition:
            checkPlayer.shipMatrix[int(shot[0])][int(shot[1])] = ' O '
            myMatrix.checkMatrix[int(shot[0])][int(shot[1])] = ' O '
            checkPlayer.shipsPosition.remove(shot)
            if player==1:
                print('You hit opponent ship.')
                myMatrix.printBothMatrix()
            if player == 2:
                self.hit = True
                self.listPotentialShot(shot)
                print('Computer hit your ship')
            if shot in checkPlayer.Carrier:
                checkPlayer.Carrier.remove(shot)
            elif shot in checkPlayer.Battleship:
                checkPlayer.Battleship.remove(shot)
            elif shot in checkPlayer.Destroyer:
                checkPlayer.Destroyer.remove(shot)
            elif shot in checkPlayer.Submarine:
                checkPlayer.Submarine.remove(shot)
            else:
                checkPlayer.Cruiser.remove(shot)
            if player==1:
                self.checkSunk(checkPlayer,1)
            else:
                self.checkSunk(checkPlayer,2)
        else:
            checkPlayer.shipMatrix[int(shot[0])][int(shot[1])] = ' X '
            myMatrix.checkMatrix[int(shot[0])][int(shot[1])] = ' X '
            if player ==1:
                print('You miss')
                myMatrix.printBothMatrix()
            else :
                print('Computer miss')
                self.hit = False
        # myMatrix.printBothMatrix()
        # checkPlayer.printBothMatrix()

        if player==1 and len(checkPlayer.shipMatrix)==0:
            print("You Win The Game!!!!!")
            quit()

        if player==2 and len(checkPlayer.shipsPosition)==0:
            print("Computer Win The Game!!!")
            quit()

    #Creates potential next shots for computer after a correct shot
    def listPotentialShot(self, shot):

        # 4 Potential shots
        if len(self.potentialShot) == 0 and self.hit == True:
            VIshot = str(int(shot[0])+1) + str(shot[1])
            if len(VIshot)==3:
                VIshot = '0'
            self.potentialShot.append(VIshot)
            VDshot = str(int(shot[0])-1) + str(shot[1])
            if len(VDshot)==3:
                VDshot = '0'
            self.potentialShot.append(VDshot)
            HIshot = str(shot[0]) + str(int(shot[1]) + 1)
            if len(HIshot)==3:
                HIshot = '0'
            self.potentialShot.append(HIshot)
            HDshot = str(shot[0]) + str(int(shot[1]) - 1)
            if len(HDshot)==3:
                HDshot = '0'
            self.potentialShot.append(HDshot)

        # 2 Potential shots when known a ship lie Vertically or Horizontally
        elif len(self.potentialShot) == 4 and self.hit == True:
            if shot == self.potentialShot[0] or shot == self.potentialShot[1]:
                self.direction = 'V'
                self.potentialShot.pop()
                self.potentialShot.pop()
                if shot == self.potentialShot[0]:
                    while shot in self.listOfShot:
                        shot = str(int(shot[0])+1) + str(shot[1])
                        if len(shot)==3:
                            shot = '0'
                        self.potentialShot[0] = shot
                elif shot == self.potentialShot[1]:
                    while shot in self.listOfShot:
                        shot = str(int(shot[0])-1) + str(shot[1])
                        if len(shot)==3:
                            shot = '0'
                        self.potentialShot[1] = shot

            elif shot == self.potentialShot[2] or shot == self.potentialShot[3]:
                self.direction = 'H'
                self.potentialShot.pop(0)
                self.potentialShot.pop(0)
                if shot == self.potentialShot[0]:
                    shot = str(shot[0]) + str(int(shot[1]) + 1)
                    if len(shot)==3:
                        shot = '0'
                    self.potentialShot[0] = shot
                elif shot == self.potentialShot[1]:
                    shot = str(shot[0]) + str(int(shot[1]) - 1)
                    if len(shot)==3:
                        shot = '0'
                    self.potentialShot[1] = shot

        # 2 potential Shots when known a ship lie Vertically
        elif len(self.potentialShot) == 2 and self.direction == 'V':
            if shot == self.potentialShot[0]:
                while shot in self.listOfShot:
                    shot = str(int(shot[0])+1) + str(shot[1])
                    if len(shot)==3:
                        shot = '0'
                    self.potentialShot[0] = shot
            elif shot == self.potentialShot[1]:
                while shot in self.listOfShot:
                    shot = str(int(shot[0]) - 1) + str(shot[1])
                    if len(shot)==3:
                        shot = '0'
                    self.potentialShot[1] = shot

        # 2 potential Shots when known a ship lie Horizontially
        elif len(self.potentialShot) == 2 and self.direction == 'H':
            if shot == self.potentialShot[0]:
                while shot in self.listOfShot:
                    shot = shot[0] + str(int(shot[1]) + 1)
                    if len(shot)==3:
                        shot = '0'
                    self.potentialShot[0] = shot
            elif shot == self.potentialShot[1]:
                while shot in self.listOfShot:
                    shot = shot[0] + str(int(shot[1]) - 1)
                    if len(shot)==3:
                        shot = '0'
                    self.potentialShot[1] = shot

    #Computer Plays
    def computerPlaying(self):
        #Random shots exclude previous shots
        if len(self.potentialShot) == 0:
            print('Potential Shots for computer',self.potentialShot)
            while (True):
                value = randint(0, 9)
                value1 = randint(0, 9)
                shot = str(value)+str(value1)
                if shot not in self.listOfShot:
                    self.listOfShot.append(shot)
                    break
            print('Computer Shot: ',shot)
            self.checkShot(shot, 2)

        #Random choice one of 4 potential shots
        elif len(self.potentialShot) == 4:
            print('Potential shots for computer:', self.potentialShot)
            while (True):
                choice = randint(0, 3)
                shot=self.potentialShot[choice]
                if self.potentialShot[choice] != '0' and shot not in self.listOfShot:
                    self.listOfShot.append(shot)
                    break
            print('Computer Shot: ',shot)

            self.checkShot(shot, 2)

        #Random choice one of 2 potential shots
        elif len(self.potentialShot) == 2:
            print('Potential shots for computer: ', self.potentialShot)
            choice = randint(0, 1)
            choice2 = 1 - choice
            shot= self.potentialShot[choice]
            if shot !='0' and shot not in self.listOfShot:
                print('Computer Shot: ',shot)
                self.listOfShot.append(shot)
                self.checkShot(shot,2)
            else:
                shot = self.potentialShot[choice2]
                if shot !='0' and shot not in self.listOfShot:
                    self.listOfShot.append(shot)
                    self.checkShot(shot,2)
                    print('Computer shot: ',shot)
                else:
                    self.potentialShot.clear()
                    self.computerPlaying()



    def startGame(self):
        turn = 1
        while (True):
            if turn == 1:
                shot = input("Position you want to shot(q to quit)")
                if shot =='q':
                    quit()
                else:
                    self.checkShot(shot, 1)
                    turn = 2
            else:
                self.computerPlaying()
                turn = 1


if __name__=='__main__':
    game = gamePlay()
    game.startGame()
