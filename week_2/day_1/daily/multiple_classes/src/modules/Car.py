class Car:
    def __init__(self, colour, model, engine, gearBox):
        self.colour = colour
        self.model = model 
        self.engine = engine
        self.gearBox = gearBox
        self.miles = 0

    

    def add_miles(self, go):
        if go:
            self.miles += 5
