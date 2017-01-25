def End_of_Year_Balance(balance, annualInterestRate, monthlyPaymentRate):
    """
    The following gives the remaining balance after 12 months on a credit
    card, given an initial balance, an annual interest rate, and 
    a monthly rate.
    ###
    balance - the outstanding balance on the credit card
    annualInterestRate - annual itnerest rate as a decimal
    montlyPaymentRate - minimum monthly payment rate as a decimal
    """
    months_left = 12
    while months_left > 0:
        balance = (
            (
                balance
                -(
                    balance
                    * monthlyPaymentRate
                 )
                
            )
            *(
                1
                +((annualInterestRate/12.0))
            )
            
        )
        months_left -= 1
    print(round(balance,2))
###########################################################################

def Min_Payment_to_Pay_off_Card(balance, annualInterestRate, payment=.38):
    """
    The following prints out the minimum (constant) monthly payment to pay
    off a credit card, given a balance and an interest rate
    """
    balance0 = balance
    months_left = 12
    while months_left > 0:
        balance = (
            (balance - payment)
            *(
                1
                +((annualInterestRate/12.0))
            )
            
        )
        months_left -= 1
    if balance <0:
        print(round(payment,2))
    else:
        return Min_Payment_to_Pay_off_Card(balance0, annualInterestRate, payment+.38)
###########################################################################
def Min_Payment_to_Pay_off_Card_Bisect(
     balance
    ,annualInterestRate
    ,lower_bound = 0
    ,upper_bound = 0
    ):
    """
    The following prints out the minimum (constant) monthly payment to pay
    off a credit card, given a balance and an interest rate
    """
    if lower_bound == 0:
        lower_bound = balance/12
        ##print('lower bound:' +str(lower_bound))
    if upper_bound == 0:
        upper_bound = (
            (
                balance
                *(
                    (
                        1
                        +(annualInterestRate/12)
                    )**12
                 )
            )
            /12.0
        )
        ##print('upper bound: ' +str(upper_bound))
    var = .01
    balance0 = balance
    payment = (lower_bound+upper_bound)/2
    months_left = 12
    #######
    while months_left > 0:
        balance = (
            (balance - payment)
            *(
                1
                +((annualInterestRate/12.0))
            )
            
        )
        months_left -= 1
    #######
    if balance <= (-var):
        ##print('balance below: '+str(balance))
        return Min_Payment_to_Pay_off_Card_Bisect(
            balance0
            ,annualInterestRate
            ,lower_bound
            ,payment
            )
    if balance >= (var):
        ##print('balance above: '+str(balance))
        return Min_Payment_to_Pay_off_Card_Bisect(
            balance0
            ,annualInterestRate
            ,payment
            ,upper_bound
            )
    else:
        ##print('end: '+str(balance))
        print(round(payment, 2))

#Min_Payment_to_Pay_off_Card_Bisect(320000, .2)
End_of_Year_Balance(32000, .2, .1)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    