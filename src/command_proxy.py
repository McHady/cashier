from cashier import Cashier

class CommandProxy:
    cashier : Cashier

    def __init__(self, cashier : Cashier):
        self.cashier = cashier

    def submit(self, args):
        """
        Submit proxy method
        """
        start = -1
        end = -1
        index = 0
        for arg in args :
            if '%' in arg:
                if start == -1:
                    start = index
                else :
                     end = index
            index += 1


        self.cashier.submit(int(args[0]), " ".join(args[start:end+1]).replace("%", "") , float(args[end+1]))
    
    def comlete(self, args):
        """
        Complete proxy method
        """
        self.cashier.complete()
    
    def contents(self, args):
        """
        Contents proxy method
        """
        self.cashier.contents()
    
    def cancel(self, args):
        """
        Cancel proxy method
        """
        self.cashier.cancel(int(args[0]))

    def print(self, args):
        """
        Print proxy method
        """
        self.cashier.print(int(args[0]))