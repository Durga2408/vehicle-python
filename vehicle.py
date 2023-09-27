class vehicle:
    no_of_Wheels = 2
    fuel_type="petrol"
    mileage=42
    speed=155
    brand="suzuki gixxer"
    manfucture=2010
    def vehicle_type(self,no_of_Wheels):
        if no_of_Wheels==2:
          print("The vechile is:suzuki gixxer")
        else:
          print("The vechile is:Car")
    def vehicle_manfacture(self,manfucture):
        if manfucture==2010:
          print("The manufacture year is:2010")
        else:
          print("The current year is:2023")

vechileObj=vehicle()
vechileObj.vehicle_type(2)
vechileObj.vehicle_manfacture(2012)
