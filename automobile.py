class Automobile:

    def __init__(self, num_wheels,color, mpg): #constructor method, initizalize

        self.wheels=num_wheels
        self.color=color
        self.gas=0
        self.mpg=mpg
        self.miles=0

    def fill_gas (self, gallons):

        self.gallons=self.gas+gallons

    def drive(self, num_miles):

        if ((num_miles/self.mpg)<self.gas):
            self.gas=self.gas -(num_miles/self.mpg)
            self.miles=self.miles+num_miles
        else:
            print("Not enough gas")


newCar1= Automobile(4, "Black", 20) # create an object, put in paramneters in our init fucntion
newCar1.fill_gas(5)
newCar1.drive(2)

    
    
    

    





        
            
