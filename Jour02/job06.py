class Commande:
    def __init__(self, order_number) -> None:
        self.__order_number = order_number
        self.__order_list = {}
        self.__order_status = "in progress"
    
    # Getters and Setters
    def get_order_number(self):
        return self.__order_number
    def get_order_list(self):
        return self.__order_list
    def get_order_status(self):
        return self.__order_status
    
    def set_order_number(self, number):
        self.__order_number = number
    def __set_order_status(self, status):
        self.__order_status = status
        
    def add_to_order(self, dish,price):
        self.__order_list[dish] = [price, "in progress"]
    
    def cancel_order(self):
        self.set_order_status("cancelled")
    def cancel_dish(self, dish):
        self.get_order_list()[dish][1] = "cancelled"
    def finish_dish(self, dish):
        self.get_order_list()[dish][1] = "finished"
        
    
    def __calculate_total(self):
        total_price = 0
        for dish, info in self.__order_list.items():
            if info[1] == "finished":
                total_price += info[0]
        return total_price
    
    def __calculate_total_tva(self):
        self.__verify_order_status()
        if self.get_order_status() == "finished":
            total_price = self.__calculate_total()
            total_price += total_price * (20 / 100)
            return total_price
        else:
            return None
    
    def print_ticket(self):
        total_price = self.__calculate_total_tva()
        if total_price != None:
            for dish, info in self.get_order_list().items():
                if info[1] == "finished":
                    print(f"{dish} ------ {info[0]}")
            print(f"Total : {total_price} euros")
        else:
            print("La commande est toujours en cours")
    def __verify_order_status(self):
        cancel_count = 0
        for dish, info in self.get_order_list().items():
            if info[1] == "in progress":
                self.set_order_status("in progress")
                return None
            elif info[1] == "cancelled"
                cancel_count += 1
        if cancel_count == len(self.get_order_list()):
            self.cancel_order()
            return None
       

order = Commande(1)
order.add_to_order("Tartiflette", 8)
order.add_to_order("Raclette", 15)
order.add_to_order("Vin", 7)
order.finish_dish("Vin")
order.finish_dish("Raclette")
order.cancel_dish("Tartiflette")
order.print_ticket()