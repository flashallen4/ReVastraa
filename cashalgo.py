costprice = float(input("Enter cost price of your appereal: "))
print("Duration of cloth owned \n1. 1 to 6 months \n2. 6 months to 1yr \n3. 1 yr to 3 yrs \n4. more than 3 yrs")
age_of_cloth = int(input("Choose the option above: "))
proof = input("Mobile number: ")

if len(proof) == 10:
    # deposit calculator
    if costprice in range(0,2501) and  age_of_cloth == 1:
        deposit = 10
        lenders = 50

    elif costprice in range(0,2501) and  age_of_cloth == 2:
        deposit = 5
        lenders = 45

    elif costprice in range(0,2501) and  age_of_cloth == 3:
        deposit = 3
        lenders = 40

    elif costprice in range(0, 2501) and age_of_cloth == 4:
        deposit = 0
        lenders = 22.5

    elif costprice in range(2501, 5001) and age_of_cloth == 1:
        deposit = 21.5
        lenders = 67

    elif costprice in range(2501, 5001) and  age_of_cloth == 2:
        deposit = 18.5
        lenders = 53.5

    elif  costprice in range(2501, 5001) and  age_of_cloth == 3:
        deposit = 12
        lenders = 43

    elif  costprice in range(2501, 5001) and  age_of_cloth == 4:
        deposit = 10
        lenders = 35

    elif costprice in range(5001, 8001) and age_of_cloth == 1:
        deposit = 24.5
        lenders = 80

    elif costprice in range(5001, 8001) and age_of_cloth == 2:
        deposit = 22
        lenders = 72

    elif costprice in range(5001, 8001) and age_of_cloth == 3:
        deposit = 18
        lenders = 60

    elif costprice in range(5001, 8001) and age_of_cloth == 4:
        deposit = 15
        lenders = 50

    elif costprice in range(8001, 10001) and age_of_cloth == 1:
        deposit = 38.5
        lenders = 90

    elif costprice in range(8001, 10001) and age_of_cloth == 2:
        deposit = 32
        lenders = 80

    elif costprice in range(8001, 10001) and age_of_cloth == 3:
        deposit = 28
        lenders = 69.5

    elif costprice in range(8001, 10001) and age_of_cloth == 4:
        deposit = 25
        lenders = 62.5

    borrowing_price = costprice * 0.4
    dep = costprice*(deposit/100)
    lend = borrowing_price*(lenders/100)
    company_inc = borrowing_price - lend

    def borrowers_amount_with_deposit(float):
        depositamount = borrowing_price + dep
        return depositamount

    print("Amount to be paid by borrower is ", round(borrowers_amount_with_deposit(borrowing_price), 2))
    if dep != 0:
        print(dep, "will be refunded.")

    print(round(lend, 2), "will be paid to lender")


else:
    print("Invalid Phone number")