print('welcom to ussd')

def get_board(row : int = 4, column : int = 3):
    
    pattern="{{{}}}" * column
    pattern= f'{pattern.strip()}\n'
    pattern=pattern * row
    pattern=pattern.strip()

    return pattern



def print_board (pattern : str , iterable):
    print(pattern.format(*iterable))


def get_ussd_code():
    board=get_board(row=4, column=3)
    numbers=[1,2,3,4,5,6,7,8,9,"*",0,"#"]
    print_board(board,numbers)

    return input("insert your USSD code:")


def show_menu():
    print('original menu')
    print ("1 : internet")
    print ("2 : charge")
    print ("3 : bill")
    print ("0 : back")



def internet_menu():
    print('internet pakage')
    print("1 : 1GB")
    print("2 : 2GB")
    print("3 : 3GB")
    print("0 : back to menu")
    
    choise=input("insert your choise: ")

    if choise in ("1", "2","3"):
        procces_payment()
    elif choise ==0:
        return
    else:    
        print("invalid")



def charge_menu():
    print('charge pakage')
    print("1 : 10 toman")
    print("2 : 20 toman")
    print("3 : 50 toman")
    print("0 : back to menu")
    choise=input("insert your choise")
    
    if choise in ("1", "2","3"):
        procces_payment()
    elif choise ==0:
        return
    else:
        print("invalid")



def bill_menu():
    print('bill pakage')
    print("1 : electricity")
    print("2 : watter")
    print("3 : gas")
    print("0 : back to menu")
    choise=input("insert your choise")
    
    if choise in ("1", "2","3"):
        procces_payment()
    elif choise ==0:
        return
    else:
        print("invalid")


def procces_payment():
    card_number= input('insert your card number : ')
    cvv2=input("insert your CVV2: ")
    if len (card_number) !=16 or not card_number.isdigit():
        print("invalid card number")
        return False
    if len(cvv2) !=4 or not cvv2.isdigit():
        print("invalid cvv2 ")
        return False
    print("payment successful")
    return True


def main():
    while True:
        code=get_ussd_code()

        if code !="*780#":
            print("invalid ussd code")
            continue

        while True:
            show_menu()
            choise=input("insert your choise : ")

            if choise=="1":
                internet_menu()
            elif choise=="2":
                charge_menu
            elif choise=="3":
                bill_menu()
            elif choise=="0":
                print("ussd code is end ")
            else:
                print('invalid option')




if __name__=="__main__":
    main()
