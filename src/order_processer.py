from abc import ABC, abstractmethod
from cashier import Cashier, DefaultCashier
from command_proxy import CommandProxy
import urllib.request

class OrderProcesser(ABC):
    commands = []

    def __init__(self, input):
        commands = self.initializeCommands(input)

    @abstractmethod
    def initializeCommands(self, input):
        """
        Initializes commands list from input
        """
        pass


    def process(self, cashier : Cashier = None):  
        """
        Processes commands from command list
        """
        cashier = cashier if cashier is not None else DefaultCashier() #Use Default Cashier if not defined
        commandProxy = CommandProxy(cashier) #Using commands via proxy for type safety
        
        #Dictionary to choose required command
        commandDict = {
            "submit" : commandProxy.submit,
            "complete": commandProxy.comlete,
            "contents": commandProxy.contents,
            "cancel": commandProxy.cancel,
            "print": commandProxy.print
        }

        for command in self.commands:
            commandDict[command[0]](command[1:] if len(command) > 1 else None) #Choose command form dictionary by first item in command list and providing remainings as proxy args
                
            
class WebSiteOrderProcesser(OrderProcesser) :

    def __init__(self, input) :
        super(WebSiteOrderProcesser, self).__init__(input)

    def initializeCommands(self, input):

        response = urllib.request.urlopen(input)

        html = response.readline()
        while len(html) != 0:
            data = html.decode('utf-8').split()
            
            if (len(data) > 0):
                self.commands.append(data)

            html = response.readline()

class FileOrderProcesser(OrderProcesser) :

    def __init__(self, input):
        super(FileOrderProcesser, self).__init__(input)
        
    def initializeCommands(self, input):

        with open(input, 'r') as file :

            for line in file.readlines() :
                data = line.split()
                self.commands.append(data)
