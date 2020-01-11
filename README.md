# BattleShipGame

#rule
This is a player vs computer
Player places ships in the grid by input
Computer places ships in the grid by file
Player and computer shot other ships by turn, 1 turn 1 shot until defeate other

#how computer shot
Computer first take random shot in the grid
If computer hit player shit first time, It will create 4 potential next shot around the correct shot which is 1 above, 1 below
1 left, and 1 right in the list
Computer continue take random 1 of 4 potential shot. If hit agian, computer knows your ship lie Vertically or Horizontally.
Computer will delete 2 incorrect shot and will continue with two potentail shots in vertical or horizontaly until sink your ship
