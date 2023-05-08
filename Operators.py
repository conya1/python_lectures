#This code is a simple calculation of a household average monthly bill
months = "Jan", "Feb", "Mar"
Jan = int(input("Enter bill for January :"))
Feb = int(input("Enter bill for February :"))
Mar = int(input("Enter bill for March :"))
Total_Monthly_Bill = (Jan + Feb + Mar)
#Total = int(input(Total_Monthly_Bill))
Avge_Monthly_Bill = float(Total_Monthly_Bill / 3)
print("What is the total monthly bill? :",Total_Monthly_Bill)
print("The Average montly bill for the last three months is :",Avge_Monthly_Bill) 