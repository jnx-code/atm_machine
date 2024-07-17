import time
print("please Insert your Card")
time.sleep(5)
password = 6504

pin = int(input("ENTER YOUR ATM PIN:"))

balance = 10000

if pin==password:
    while True:
        print("""
          1 == balance
          2 == withdraw balance
          3 == deposit balance
          4 == exit
          """ )
        try:
          option = int(input("please enter your choice:"))
        except:
           print("please enter valid option")

        if option == 1:
           print(f"your current balance is {balance}")
        if option == 2:
           withdrawl_amount = int(input("please enter withdrawl_amount "))
           balance = balance-withdrawl_amount
           print(f"your updated balance is {balance}")
        if option == 3:
           deposit_amount = int(input("please enter deposit_amount "))
           balance = balance+deposit_amount
           print(f"{deposit_amount} is debited from your account")
           print(f"your updated balance is {balance}")
        if option == 4:
          break
else:
    print("wrong pin please try again")