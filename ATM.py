import time
def register():
    pass

def account_access():
        correct_pin = 1234
        balance = 0
        pin = int(input('\nPLEASE ENTER YOUR ATM PIN: '))
        try:
            if pin == correct_pin:
                account_holder_name_entry = input('\nPLEASE ENTER YOUR NAME: ')
                account_holder_name = account_holder_name_entry.upper()
                while True:
                    time.sleep(4)
                    print('===================================================================')
                    print(f"\nHELLO {account_holder_name}, WELCOME TO STATE BANK OF INDIA")
                    print('PLEASE SELECT AN BANKING OPTION TO CONTINUE')
                    print("""
                        1== BALANCE ENQUIRY
                        2== CASH DEPOSITE
                        3== CASH WITHDRAWAL
                        4== EXIT\n""")
                    print('===================================================================')
                    try:        
                        option = int(input('\nPLEASE SELECT YOUR OPTION: '))
                    except Exception as ex:
                        print('\nPLEASE ENTER CORRECT OPTION')
                    try:    
                        if option == 1:
                            print('===================================================================')
                            print(f"\nHELLO {account_holder_name}")                 
                            print("\nAVAILABLE BALANCE IN YOUR ACCOUNT: ",balance)
                            print('===================================================================')

                        elif option == 2:
                            try:   
                                deposite = int(input('\nENTER AMOUNT YOU WANT TO DEPOSITE: '))
                                if deposite % 100 ==0 and deposite <= 20000:
                                    balance += deposite
                                    print('===================================================================')
                                    print('\nAMOUNT YOU HAVE DEPOSITED: ',deposite)
                                    print('\nAVAILABLE BALANCE IN YOUR ACCOUNT: ',balance)
                                    print('===================================================================')
                                else:
                                    print('===================================================================') 
                                    print('\nENTERED AMOUNT IS INVALID PLEASE TRY AGAIN')
                                    print('===================================================================')
                            except Exception as ex:
                                print('===================================================================')
                                print('\nENTERED VALUE IS INVALID PLEASE TRY AGAIN')
                                print('===================================================================')

                        elif option == 3:
                            try:   
                                withdraw = int(input('\nENTER AMOUNT YOU WANT TO WITHDRAW: '))
                                if withdraw % 100 ==0 and withdraw <= 20000:
                                    if balance >= withdraw:
                                        balance -= withdraw
                                        print('===================================================================')
                                        print('\nAMOUNT YOU WANT TO WITHDRAW: ',withdraw)
                                        print('\nAVAILABLE BALANCE IN YOUR ACCOUNT: ',balance)
                                        print('===================================================================')
                                    else:
                                        print('===================================================================')
                                        print('\nINSUFFICIENT BALANCE IN YOUR ACCOUNT PLEASE TRY AGAIN')
                                        print('===================================================================')
                                else:
                                    print('===================================================================')
                                    print('\nENTERED AMOUNT IS INVALID PLEASE TRY AGAIN')
                                    print('===================================================================')
                            except Exception as ex:
                                print('===================================================================')
                                print('\nENTERED VALUE IS INVALID PLEASE TRY AGAIN')
                                print('===================================================================')
                                

                        elif option == 4:
                            print('===================================================================')
                            print(f'\nTHANK YOU FOR BANKING WITH US {account_holder_name}, HAVE A NICE DAY\n')
                            print('===================================================================')
                            time.sleep(3)
                            break

                        else:
                            print('===================================================================')
                            print("\nINVALID OPTION, PLEASE TRY AGAIN")
                            print('===================================================================')
                            time.sleep(3)
                            account_access()

                            
                    except Exception as ex:
                        print('===================================================================')
                        print("\nINVALID OPTION, PLEASE TRY AGAIN")
                        print('===================================================================')
                        time.sleep(3)
                        account_access()
                                    

            else:
                print('===================================================================')
                print("\nINCORRECT PIN, PLEASE TRY AGAIN")
                print('===================================================================')
                time.sleep(3)
                account_access()

        except Exception as ex:
            print('===================================================================')
            print("\nINCORRECT PIN, PLEASE TRY AGAIN")
            print('===================================================================')
            time.sleep(3)
            account_access()                

def home(option=None):
    print('===================================================================')
    print('\n***   WELCOME TO STATE BANK OF INDIA   ***')
    print('\n***   PLEASE CHOOSE YOUR OPTION   ***')
    print("""
    1 == NEW USER
    2 == OLD USER""")
    print('===================================================================')

    try:
        option = int(input("\nPLEASE ENTER YOUR OPTION: "))
        if option == 1:
            print('===================================================================')
            print('\nUSER ALREADY REGISTERED PLEASE TRY AGAIN\n')
            print('===================================================================')
            home()
        elif option == 2:
            time.sleep(3)
            account_access()
        else:
            print('===================================================================')
            print('\nPLEASE SELECT A VALID OPTION')
            print('===================================================================')
            time.sleep(3)
            home()
    except Exception as ex:
        print('===================================================================')
        print('\nPLEASE SELECT A VALID OPTION')
        print('===================================================================')
        time.sleep(3)       
        home()

home()

