class Account():
    def __init__(self, intCheckingAccountOpening):
        self._intCheckingAccountOpening = intCheckingAccountOpening

    @property 
    def intCheckingAccountOpening(self):
        return self._intCheckingAccountOpening

    @intCheckingAccountOpening.setter
    def intCheckingAccountOpening(self, intCheckingAccountOpening):
        if intCheckingAccountOpening >= 0:
            self._intCheckingAccountOpening = intCheckingAccountOpening
        else:
            raise Exception('Checking accounts being opened must be equal to or greater than 0. User input was {}'.format(intCheckingAccountOpening))
            

PersonOne = Account(-10)