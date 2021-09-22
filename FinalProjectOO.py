#------------------------------------------------------------------------------
#               Tom Lytle
#           CPDM198 Final Project
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Final project Class area
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Class Name: CreateAccount
# Class purpose: to create objects with basic customer info, First name, Last name, SSN, # of checking and savings opening and initial deposits for checking and savings
#------------------------------------------------------------------------------

class CreateAccount:  
    

    def __init__(self, strFirstName, strLastName, intSSN, intCheckingAccountOpening = 0, intSavingsAccountOpening = 0, dblInitialCheckingDeposit = 0, dblInitialSavingsDeposit = 0):
        self.strFirstName = strFirstName
        self.strLastName = strLastName
        self.intSSN = intSSN
        self.intCheckingAccountOpening = intCheckingAccountOpening
        self.intSavingsAccountOpening = intSavingsAccountOpening
        self.dblInitialCheckingDeposit = dblInitialCheckingDeposit
        self.dblInitialSavingsDeposit = dblInitialSavingsDeposit
        
       
      
       

        _dblCheckingAccountBalance = dblInitialCheckingDeposit 
        _dblSavingsAccountBalance = dblInitialSavingsDeposit 
        

#------------------------------------------------------------------------------
# Property and setter to add validation on strFirstName to make sure in only contains Alpha characters or - or white space
#------------------------------------------------------------------------------

    @property
    def strFirstName(self):
        return self._strFirstName

    @strFirstName.setter
    def strFirstName(self, strFirstName):
        valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'
        if all(char in valid_characters for char in strFirstName):
            self._strFirstName = strFirstName
        else:
             raise Exception ('First name can only contain Alpha Characters. User input was {}'.format(strFirstName))


#------------------------------------------------------------------------------
# Property and setter to add validation on strLastName to make sure in onlt contains Alpha characters or - or white space
#------------------------------------------------------------------------------

    @property
    def strLastName(self):
        return self._strLastName

    @strLastName.setter
    def strLastName(self, strLastName):
        valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'
        if all(char in valid_characters for char in strLastName):
            self._strLastName = strLastName
        else:
            raise Exception ('Last name can only contain Alpha Characters. User input was {}'.format(strLastName))


#------------------------------------------------------------------------------
# Property and setter to add validation for intSSN to make sure it only contains integers and is 8 characters long
#------------------------------------------------------------------------------

    @property 
    def intSSN(self):
        return self._intSSN

    @intSSN.setter
    def intSSN(self, intSSN):
        __strSSN = str(intSSN)
        _intLength = len(__strSSN)
        if _intLength != 9:
            raise Exception('Social Security Number musst be 9 digits long. User input was {}'.format(intSSN))
        else:
            if intSSN > 0:
                self._intSSN = intSSN
            else:
                raise Exception('Social Security Number must be positive. User input was {}')


#------------------------------------------------------------------------------
# Property and Setter to check that intCheckingAccountOpening is a positive digit equal to or great than 0
#------------------------------------------------------------------------------
    
    @property 
    def intCheckingAccountOpening(self):
        return self._intCheckingAccountOpening

    @intCheckingAccountOpening.setter
    def intCheckingAccountOpening(self, intCheckingAccountOpening):
        if intCheckingAccountOpening >= 0:
            self._intCheckingAccountOpening = intCheckingAccountOpening
        else:
            raise Exception('Checking accounts being opened must be equal to or greater than 0. User input was {}'.format(intCheckingAccountOpening))


#------------------------------------------------------------------------------
# Property and Setter to check that intSavingsAccountOpening is a positive digit equal to or great than 0
#------------------------------------------------------------------------------

    @property
    def intSavingsAccountOpening(self):
        return self._intSavingsAccountOpening

    @intSavingsAccountOpening.setter
    def intSavingsAccountOpening(self, intSavingsAccountOpening):  
        if intSavingsAccountOpening >= 0:
            self._intSavingsAccountOpening = intSavingsAccountOpening
        else:
            raise Exception ('Savings accounts being opened must be equal to or greater than 0. User input was {}'.format(intSavingsAccountOpening))
    
#------------------------------------------------------------------------------
# Property and Setter to check that dblInitialCheckingDeposit is positive if intCheckingAccountOpening is > 0
#------------------------------------------------------------------------------
    
    @property
    def dblInitialCheckingDeposit(self):
        return self._dblInitialCheckingDeposit
        
    @dblInitialCheckingDeposit.setter
    def dblInitialCheckingDeposit(self, dblInitialCheckingDeposit):
        if dblInitialCheckingDeposit >= 0:
            if self._intCheckingAccountOpening > 0:
                self._dblInitialCheckingDeposit = dblInitialCheckingDeposit
            else:
                raise Exception('Checking accounts being opened is 0. Can not make initial checking account deposit until checking account is opened')
        else:
            raise Exception('Initial checking account deposit must be a positive number. User input was {}'.format(dblInitialCheckingDeposit))


#------------------------------------------------------------------------------
# Property and Setter to check that dblInitialSavingsDeposit is > 500 if intSavingsAccountOpening is > 0
#------------------------------------------------------------------------------

    @property
    def dblInitialSavingsDeposit(self):
        return self._dblInitialSavingsDeposit

    @dblInitialSavingsDeposit.setter
    def dblInitialSavingsDeposit(self, dblInitialSavingsDeposit):
        if self._intSavingsAccountOpening > 0:
            if dblInitialSavingsDeposit >= 500:
                self.dblInitialCheckingDeposit = dblInitialSavingsDeposit
            else:
                raise Exception('Initial savings account deposit must be greater than $500. User input was{}'.format(dblInitialSavingsDeposit))
        else:
            raise Exception('Savings accounts being opened is 0. Can not make intital savings account deposit without opening saving account')

#------------------------------------------------------------------------------
# Method to close checking or savings accounts. Validates that customer can not close more accounts than they have
#------------------------------------------------------------------------------

    def CloseAccount(self):

        global _dblTotalCheckingAccountBalance
        global _dblTotalSavingsAccountBalance
        global _intCheckingAccountOpening
        global _intSavingsAccountOpening

        intCloseChecking = int(input('How many checking accounts are being closed: '))
        intCloseSavings = int(input('How many savings accounts are being closed: '))

       

        if intCloseChecking > self._intCheckingAccountOpening:
            raise Exception ('Cannot close more accounts than the customer has. Customer has {} attepted to close {} accounts'.format(self._intCheckingAccountOpening, intCloseChecking))
        else:
            intCheckingAccountTotal = self._intCheckingAccountOpening - intCloseChecking  
        if intCheckingAccountTotal == 0:
            _dblTotalCheckingAccountBalance = _dblTotalCheckingAccountBalance - _dblCheckingAccountBalance

        if intCloseSavings > self._intSavingsAccountOpening:
            raise Exception ('Cannot close more accounts than the customer has. Customer has{} attepted to close {} accounts'.format(self._intSavingsAccountOpening, intCloseSavings))
        else:
            intSavingsAccountTotal = self.intSavingsAccountOpening - intCloseSavings
        if intSavingsAccountTotal == 0:
            _dblTotalSavingsAccountBalance = _dblTotalSavingsAccountBalance - _dblSavingsAccountBalance
            

        
#------------------------------------------------------------------------------
# Class Name: Transaction
#
#------------------------------------------------------------------------------

class Transaction(CreateAccount):

    

    def __init__(self, strFirstName, strLastName, intSSN, intCheckingAccountOpening, intSavingsAccountOpening, dblInitialCheckingDeposit, dblInitialSavingsDeposit, dblCheckingDeposit = 0 , dblSavingsDeposit = 0, dblCheckingWithdraw = 0, dblSavingsWithdraw = 0):
        CreateAccount.__init__ (self, strFirstName, strLastName, intSSN, intCheckingAccountOpening, intSavingsAccountOpening, dblInitialCheckingDeposit, dblInitialSavingsDeposit)
        
        global _dblTotalCheckingAccountBalance
        global _dblTotalSavingsAccountBalance

        self.dblCheckingDeposit = dblCheckingDeposit
        self.dblSavingsDeposit = dblSavingsDeposit  
        self.dblCheckingWithdraw = dblCheckingWithdraw
        self.dblSavingsWithdraw = dblSavingsWithdraw

        _dblTotalCheckingAccountBalance =  dblInitialCheckingDeposit + dblCheckingDeposit - dblCheckingWithdraw 
        _dblTotalSavingsAccountBalance =  dblInitialSavingsDeposit + dblSavingsDeposit - dblSavingsWithdraw

       

        

        if _dblTotalCheckingAccountBalance < 0:
            _dblTotalCheckingAccountBalance = _dblTotalCheckingAccountBalance - 20

        if _dblTotalSavingsAccountBalance < 500:
            raise Exception('Savings Account balance can not go below $500.')

        

        


#------------------------------------------------------------------------------
# property and setter to make sure dblCheckingDeposit is an integer only or it raises exception
#------------------------------------------------------------------------------

    @property 
    def dblCheckingDeposit(self):
        return self._dblCheckingDeposit

    @dblCheckingDeposit.setter
    def dblCheckingDeposit(self, dblCheckingDeposit):
        if dblCheckingDeposit >= 0:
            self._dblCheckingDeposit = dblCheckingDeposit
        else:
            raise Exception('Checking depsoit must be posivite. user input was {}'.format(dblCheckingDeposit))
            
#------------------------------------------------------------------------------
# property and setter to validate dblSavingsDeposit has only integers or it will raise an exception
#------------------------------------------------------------------------------
    @property
    def dblSavingsDeposit(self):
        return self._dblSavingsDeposit

    @dblSavingsDeposit.setter
    def dblSavingsDeposit(self, dblSavingsDeposit):
       if dblSavingsDeposit >= 0:
           self._dblSavingsDeposit = dblSavingsDeposit
       else:
           raise Exception('Savings Deposit must be positive. User input was {}'.format(dblSavingsDeposit))     



#------------------------------------------------------------------------------
#  property and setter to validate dblCheckingWithdraw has only integers or it will raise an exception
#------------------------------------------------------------------------------
    @property
    def dblCheckingWithdraw(self):
        return self._dblCheckingWithdraw

    @dblCheckingWithdraw.setter
    def dblCheckingWithdraw(self, dblCheckingWithdraw):
        if dblCheckingWithdraw >= 0:
            self._dblCheckingWithdraw = dblCheckingWithdraw

        else:
            raise Exception('Checking withdraw must be positive. User input was {}'.format(dblCheckingWithdraw))


#------------------------------------------------------------------------------
# property and setter to validate dblSavingsWithdraw has only integers or it will raise an exception
#------------------------------------------------------------------------------

    @property
    def dblSavingsWithdraw(self):
        return self._dblSavingsWithdraw

    @dblSavingsWithdraw.setter
    def dblSavingsWithdraw(self, dblSavingsWithdraw):
        if dblSavingsWithdraw >= 0:           
           self._dblSavingsWithdraw = dblSavingsWithdraw
        else:
            raise Exception('Savings withdraw must be posivite. User input was {}'.format(dblSavingsWithdraw))


#------------------------------------------------------------------------------
# Function Name: TransferMoney
# Function Purpose: To transfer money from checking to savings or savings to checking
#------------------------------------------------------------------------------
    def TransferMoney(self):
        global _dblCheckingAccountBalance 
        global _dblSavingsAccountBalance 
         

        _dblCheckingToSavings = float(input('How much do you want to transfer from checking to savings?: '))
        if (_dblCheckingToSavings > 0):
            if (_dblCheckingToSavings <= _dblCheckingAccountBalance):
                _dblCheckingAccountBalance = _dblCheckingAccountBalance - _dblCheckingToSavings
                _dblSavingsAccountBalance = _dblSavingsAccountBalance + _dblCheckingToSavings
            else:
                raise Exception('Can not transfer more money out of chekcing than what is in the account')

        _dblSavingsToChecking = float(input('How much do you want to transfer from savings to checking?: '))
        if (_dblSavingsToChecking > 0):
           if(_dblSavingsAccountBalance - 500) > _dblSavingsToChecking:   
                _dblSavingsAccountBalance = _dblSavingsAccountBalance - _dblSavingsToChecking
                _dblCheckingAccountBalance = _dblCheckingAccountBalance + _dblSavingsToChecking
           else:
                raise Exception('Cannot go below $500 in savings account')
        else:
            raise Exception('Cannot go below $500 in savings account')

    def BalanceInquiry(self):
        

        print('Checking account balance is: {} '.format(_dblTotalCheckingAccountBalance))
        print('Savings account balance is: {}'.format(_dblTotalSavingsAccountBalance))
        print('Total account balance is: {}'.format(_dblTotalCheckingAccountBalance + _dblTotalSavingsAccountBalance))
            
        



#Customers to test

# Variable come in strFirstName, strLastName, intSSN, intCheckingAccountOpening, intSavingsAccountOpening, dblInitialCheckingDeposit
# , dblInitialSavingsDeposit, dblCheckingDeposit, dblSavingsDeposit, dblCheckingWithdraw, dblSavingsWithdraw

# should work perfectly
#PersonOne = Transaction('Bill', 'Nye', 123456789, 1, 1, 500, 500)
#PersonOne.BalanceInquiry()

# Should throw exception for savings account going below 500
#PersonTwo = Transaction('Jill', 'Bill', 123456789, 1, 1, 600, 600, 0, 0, 0, 600)

# should cause OD charge for checking going negative
#PersonThree = Transaction ('Jill', 'Bill', 123456789, 1, 1, 700, 700, 800, 0, 0, 0)





# to do list:
# get to print account balance for a single person and not the last one made


