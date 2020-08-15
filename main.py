
import os
def cls():
	os.system("clear")


def printTheBoard(board,width):
	print(f"""{board["top-L"]} | {board["top-M"]} | {board["top-R"]}""".center(width))
	print("---------".center(width))
	print(f"""{board["mid-L"]} | {board["mid-M"]} | {board["mid-R"]}""".center(width))
	print("---------".center(width))
	print(f"""{board["low-L"]} | {board["low-M"]} | {board["low-R"]}""".center(width))



def whoIsWinner(pos,players,userSymbol):
	if (pos == userSymbol['player1']):
		return f'{players["player1"]} is the winner'
	else:
		return f'{players["player2"]} is the winner'



def checkWinner(board,players,userSymbol):
	ox = [userSymbol["player1"],userSymbol["player2"]]

	if (board["top-L"] == board["top-M"] == board["top-R"] in ox):
		return whoIsWinner(board["top-L"],players,userSymbol)

	elif (board["mid-L"] == board["mid-M"] == board["mid-R"] in ox):
		return whoIsWinner(board["mid-L"],players,userSymbol)

	elif(board["low-L"] == board["low-M"] ==board["low-R"] in ox):
		return whoIsWinner(board["low-L"],players,userSymbol)
	
	elif (board["low-L"] == board["mid-M"] == board["top-R"] in ox):
		return whoIsWinner(board["low-L"],players,userSymbol)

	elif (board["top-L"] == board["mid-M"] == board["low-R"] in ox):
		return whoIsWinner(board["top-L"],players,userSymbol)

	elif (board["top-L"] == board["mid-L"] == board["low-L"] in ox):
		return whoIsWinner(board["top-L"],players,userSymbol)

	elif (board["top-M"] == board["mid-M"] == board["low-M"] in ox):
		return whoIsWinner(board["top-M"],players,userSymbol)

	elif (board["top-R"] == board["mid-R"] == board["low-R"] in ox):
		return whoIsWinner(board["top-R"],players,userSymbol)
	


if __name__ == '__main__':
	cls()
	width = os.get_terminal_size()[0]

	player1 = input("Name of player1: ")
	player2 = input("Name of player2: ")
	cls()
	players = {"player1":player1,"player2":player2}
	userSymbol = {"player1":"X","player2":"O"}

	print(f'{players["player1"]} => {userSymbol["player1"]}')
	print(f'{players["player2"]} => {userSymbol["player2"]}')

	board ={"top-L": " ","top-M":" ","top-R": " ",
			"mid-L": " ","mid-M":" ","mid-R": " ",
			"low-L": " ","low-M":" ","low-R": " "
		}
	boardMap = {1:"top-L",2:"top-M",3:"top-R",
				4:"mid-L",5:"mid-M",6:"mid-R",
				7:"low-L",8:"low-M",9:"low-R"
	}
	availableChoices =[1,2,3,4,5,6,7,8,9]
	printTheBoard(board,width)
	over = False
	while not over:
		for name in players.keys():
			userName = players[name]
			print(f"{userName}'s turn")
			while True:
				try:
					usrInput = int(input("What is your move : "))
					if usrInput in availableChoices:
						availableChoices.remove(usrInput)
					else:
						print("unavailable choice")
						continue
					break
				except ValueError:
					print("give only numbers not string")
					continue

			usrInput = boardMap[usrInput]
			board[usrInput] = userSymbol[name]
			cls()
			
			printTheBoard(board,width)
			winnerMsg = checkWinner(board,players,userSymbol)
			if (winnerMsg):
				over = True
				print(winnerMsg)
				exit()
			if (len(availableChoices) == 0):
				print("Draw")
				exit()




