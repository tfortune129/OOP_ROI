class rentalIncome:

    #set up init/selfs for all parts of ROI calculation:
    #(since values are put in manually, attributes should be consistent)
    # def __init__(self):
    #     #initialize attribites
    #     self.income = None
    #     self.expenses = None
    #     self.cashflow = None
    #     self.ROI = None
    #     self.investments = None
    #define each attribute and its sub attributes
       
    def income(self):
        rent = int(input("What is your estimated rental income? "))
        laundry = int(input("what is your estimated laundry income? "))
        storage = int(input("what is your estimated storage income? "))
        misc = int(input("what is your estimated misc. income? "))
        
        #set boundaries for all attributes:
        #rent:
        if rent >= 0:
            print (f'Your rent income estimate for this month is {rent}')
        elif rent < 0:
            print ('Please input a valid value.')
            rent = int(input("What is your estimated rental income? "))    

        #laundry:
        if laundry >= 0:
            print (f'Your laundry income estimate for this month is {laundry}')
        elif laundry < 0:
            print ('Please input a valid value.')
            laundry = int(input("what is your estimated laundry income? "))
        #storage:
        if storage >= 0:
            print (f'Your storage income estimate for this month is {storage}')
        elif storage < 0:
            print ('Please input a valid value.')
            storage = int(input("what is your estimated storage income? "))

        #misc.
        if misc >= 0:
            print (f'Your misc income estimate for this month is {misc}')
        elif misc < 0:
            print ('Please input a valid value.')
            misc = int(input("what is your estimated misc. income? "))
        
        self.income  = rent + laundry + storage + misc
        print(f'Here is your total monthly income: {self.income}')

    def expenses(self):
        tax = int(input("What is your estimated tax value? "))
        insurance = int(input("what is your estimated insurance? "))
        utilities = int(input("what is your estimated utilities? "))
        HOA = int(input("what is your estimated home owner association fee if you have one? "))
        lawnSnow = int(input("What is your estimated lawn and snow cost? "))
        vacancy = int(input("what is your estimated vacancy cost? "))
        capEx = int(input("what do your capital expenses add up to? "))
        management = int(input("what is your estimated management expenses? "))
        mortgage = int(input("what is your estimated mortgage expenses? "))

        #tax:
        if tax >= 0:
            print (f'Your tax expense estimate for this month is {tax}')
        elif tax < 0:
            print ('Please input a valid value.')
            tax = int(input("What is your estimated tax value? "))
        
        #insurance:
        if insurance >= 0:
            print (f'Your insurance expense estimate for this month is {insurance}')
        elif insurance < 0:
            print ('Please input a valid value.')
            insurance = int(input("what is your estimated insurance? "))
        
        #utilities:
        if utilities >= 0:
            print (f'Your utility expense estimate for this month is {utilities}')
        elif utilities < 0:
            print ('Please input a valid value.')
            utilities = int(input("what is your estimated utilities? "))
        
        #home owner association fee:
        if HOA >= 0:
            print (f'Your utility expense estimate for this month is {HOA}')
        elif HOA < 0:
            print ('Please input a valid value.')
            HOA = int(input("what is your estimated home owner association fee if you have one? "))

        #lawn and snow:
        if lawnSnow >= 0:
            print (f'Your insurance expense estimate for this month is {lawnSnow}')
        elif lawnSnow < 0:
            print ('Please input a valid value.')
            lawnSnow = int(input("What is your estimated lawn and snow cost? "))
        
        
        #vacancy:
        if vacancy >= 0:
            print (f'Your insurance expense estimate for this month is {vacancy}')
        elif vacancy < 0:
            print ('Please input a valid value.')
            vacancy = int(input("what is your estimated vacancy cost? "))

        #capital expenses:
        if capEx >= 0:
            print (f'Your insurance expense estimate for this month is {capEx}')
        elif capEx < 0:
            print ('Please input a valid value.')
            capEx = int(input("what do your capital expenses add up to? "))
        #management:
        if management >= 0:
            print (f'Your insurance expense estimate for this month is {management}')
        elif management < 0:
            print ('Please input a valid value.')
            management = int(input("what is your estimated management expenses? "))
        
        #mortgage:
        if mortgage >= 0:
            print (f'Your insurance expense estimate for this month is {mortgage}')
        elif mortgage < 0:
            print ('Please input a valid value.')
            mortgage = int(input("what is your estimated mortgage expenses? "))
        
       
        self.expenses  = tax + insurance + utilities + HOA + lawnSnow + vacancy + capEx + management + mortgage
        print(f'Here is your total monthly expenses: {self.expenses}')



    def cashflow(self):
        self.cashflow = {self.income} - {self.expenses}
        print(f'Here is your total monthly cashflow: {self.cashflow}')
        
        #12 months here?


    
    def investments(self):
        downPayment = int(input("What is your estimated down payment? "))
        closing = int(input("what is your estimated closing fee? "))
        rehab = int(input("what is your estimated rehab budget? "))
        other = int(input("what is your estimated misc. investments? "))

        #down payment:
        if downPayment >= 0:
            print (f'Your insurance expense estimate for this month is {downPayment}')
        elif downPayment < 0:
            print ('Please input a valid value.')
            downPayment = int(input("What is your estimated down payment? "))
        
        #closing:
        if closing >= 0:
            print (f'Your insurance expense estimate for this month is {closing}')
        elif closing < 0:
            print ('Please input a valid value.')
            closing = int(input("what is your estimated closing fee? "))

        #rehab:
        if rehab >= 0:
            print (f'Your insurance expense estimate for this month is {rehab}')
        elif rehab < 0:
            print ('Please input a valid value.')
            rehab = int(input("what is your estimated rehab budget? "))

        #other:
        if other >= 0:
            print (f'Your insurance expense estimate for this month is {other}')
        elif other < 0:
            print ('Please input a valid value.')
            other = int(input("what is your estimated misc. investments? "))
        
        self.investments = downPayment + closing + rehab + other
        print(f'Here is your total monthly investments: {self.cashflow}')


    def ROI(self):
        annualcashflow = {self.cashflow} * 12
        self.ROI = (annualcashflow/{self.investments}) * 100
        print(f'Here is your cash on cash ROI: {self.ROI}%')

    def run(self):
        x = input("Hit enter to calc ROI or 'q' to quit")
        while x != 'q':
            self.income()
            self.expenses()
            self.cashflow()
            self.investments()
            self.ROI()
            x = input("Hit enter to calc ROI or 'q' to quit")

# yourROI = rentalIncome
# yourROI.income()
# yourROI.expenses()
# yourROI.cashflow()
# yourROI.investments()
# yourROI.ROI()
y = rentalIncome()
y.run()       


