from abc import ABC, abstractclassmethod
from dataclasses import dataclass

class Cashier(ABC):

    @abstractclassmethod
    def submit(self, order_id : int, order : str, total : float):
        """
        Submit command
        """
        pass

    @abstractclassmethod
    def complete(self):
        """
        Complete command
        """
        pass
    
    @abstractclassmethod
    def contents(self):
        "Queue contents command"
        pass

    @abstractclassmethod
    def cancel(self, order_id : int):
        "Cancel command"
        pass

    @abstractclassmethod
    def print(self, order_id : int):
        "Print command"
        pass

@dataclass
class Order :
    order_id : int
    order : str
    total : float

class DefaultCashier(Cashier):

    orders = []
    totalOrders = 0

    def __index_by_order_id(self, order_id : int):
        """
        Seems there's no such method for default lists to get index of list member by property, so i'll do it myself
        """
        index = 0
        for order in self.orders:
            order : Order
            if order.order_id == order_id:
                return index
            index += 1

        return -1

    def submit(self, order_id : int, order : str, total : float):

        order = Order(order_id, order, total)
        self.orders.append(order)
        self.totalOrders += 1

        print(f'Adding {order.order_id} to the queue.')
    
    def complete(self):

        order : Order = self.orders.pop(0)
        print(f'Completed order {order.order_id}.')

    def contents(self):
        print(f'Orders in queue: {len(self.orders)}\nTotal orders: {self.totalOrders}.')

    def cancel(self, order_id : int):
        
        index = self.__index_by_order_id(order_id)
        # Print "Unable to cancel..." if there's no such order in queue
        if index == -1 :
            print("Unable to cancel this job -- it has already been processed or never exists")
        else :
            self.orders.pop(index)
            print(f'Canceled order #{order_id}')
    
    def print(self, order_id : int):

        index = self.__index_by_order_id(order_id)
        print(f'This order contains the following food items: {self.orders[index].order}')

            


