class Bus:
    def __init__(self, route_numb, destination, ):
        self.route_number = route_numb
        self.destination = destination
        self.passenger= []
       


    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passenger)


    def pick_up(self, passenger):
        self.passenger.append(passenger)

    def empty(self,):
        self.passenger.clear()

    def add_to_queue(self, passenger):
        self.queue.append(passenger)

    def drop_off(self, passenger):
        self.passenger.remove(passenger)
    
    
    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.passenger.append(passenger)
        bus_stop.clear()
