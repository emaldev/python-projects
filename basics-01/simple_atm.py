#This is an ATM
#You can check your balance.
# and make a withdrawal
# Add funds to your card 
#These are the things we will practice :
# :=>(input, int(change type of variable) , if/elif, and operator(+ , -))
#I hava a Big Bank System Management project for Java 
# I Lave you 

balance = 1000

print('choose operator')
print('1. Check Balance.')
print('2. Deposit')
print('3. Withdraw')


choise = int(input("Enter your choise:"))

if choise == 1:
    print(f'Balance: {balance}')
elif choise == 2:
    depo = int(input('Enter deposit amount :'))
    balance += depo
    print('Deposit successful!')
    print(f'Your new balance is : {balance}')

elif choise == 3:
    withdraw = int(input('Enter whithdraw amout:'))
    if(balance >= withdraw):
        balance -= withdraw
        print('Withdrawal successful!')
        print(f'Your new balance is : {balance}')
    else:
        print('Insufficient balance!')
else:
    print('Inbalid choice!')
    
