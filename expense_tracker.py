def expense_tracker():
    Balance=10000  ###capital
    Texpense=0    ###Total expenses
    day=input('Enter the day-')

    with open(f'{day}.txt','w') as f:
        f.write('Expense Details \n\nTotal amount in hand=10000')
    while True:
        print('Do you want to add expense details? \noptions \n1.Yes \n2.No')
        a=int(input('Enter the choice- '))
        if a==1:
            name=input('Enter the name of the expense-')
            amount=int(input('Enter the expense amount-'))
            Texpense=Texpense+amount
            Balance=Balance-amount
            with open('Expense_tracker_details.txt','a') as f:
                f.write(f'\n\nName of Expense={name} \nExpense amount={amount} \nBalance Amount={Balance} \n \n')
        else:
            break
        
expense_tracker()





# class ExpenseTracker:
#     with open('Expense_tracker_details.txt','w') as f:
#         f.write('Expense Details \n\nTotal amount in hand=10000')
#     # def __init__(self,Name,Amount):
#     #     self.Name_of_expense=Name
#     #     self.Expense_Amount=Amount
#     def add_expense():
#         print('Do you want to add expense details? \noptions \n1.Yes \n2.No')
#         a=int(input('Enter the choice- '))
#         if a==1:
#             Name=input('Enter the name of the expense-')
#             amount=int(input('Enter the expense amount-'))
#             Texpense=Texpense+amount
#             Balance=Balance-amount
#     def view_expense():
#         open('Expense_tracker_details.txt','r')
#     def expence_tracker():
#         Texpense=0
#         Balance=1000
#         with open('Expense_tracker_details.txt','a') as f:
#             f.write(f'\n\nName of Expense={Name} \nExpense amount={amount} \nBalance Amount={Balance} \n \n')
    

# E1=ExpenseTracker()
# print(E1.add_expense())
# print(E1.view_expense())
# print(E1.expence_tracker())

