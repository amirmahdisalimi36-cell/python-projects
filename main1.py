from string import digits
import random

def get_board (row: int = 3, column: int = 3):
    pattern= "{{{}}}" * column
    pattern=f"{pattern.strip()}\n"
    pattern=pattern*row
    pattern=pattern.strip()

    return pattern

def print_board (pattern: str , iterable):
    print(pattern.format(*iterable))



def name_player ():
    first_player=input('insert your name: ')
    second_player=input('insert your name:  ')
    if first_player and second_player:
        return first_player , second_player
    print('players is OB')



def get_first_player(first_player , second_player):
    return random.choice([first_player,second_player])



def final_board(tic_toc, choise , random_player , first_player):
    if random_player==first_player:
        tic_toc=tic_toc.replace(choise ,"X")
    else:
        tic_toc=tic_toc.replace(choise ,"O")

    return tic_toc



def change_player (first_player , second_player , random_player):
    if random_player==first_player:
        random_player=second_player
    else:
        random_player=first_player



def get_choise(choises):
    while True:
        choise=input('insert your choise:  ')
        if len (choise)==1 and choise in choises:
            return choise
        else:
            print('rour choise was wrong')

def main():
    tic_toc='123456789'
    pattern=get_board()
    first_player, second_player=name_player()
    random_player= get_first_player(first_player,second_player)
    print(f"{random_player} starts the game")
    while True:
        choise=get_choise(tic_toc)
        tic_toc=final_board(tic_toc,choise,random_player,first_player)
        print_board(pattern, tic_toc)
        random_player=change_player(random_player,first_player,second_player)






if __name__ == "__main__":
    main()    


