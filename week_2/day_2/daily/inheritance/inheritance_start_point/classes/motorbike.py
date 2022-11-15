
from classes.vehicle import Vehicle


class Motorbike(Vehicle):
      def start_engine(self):
        # we can still acces the super value it is not overwritten 
        supers_start_val = super().start_engine()
        print(supers_start_val)
        return "Meow"