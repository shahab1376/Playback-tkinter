## Dataset Builder Script


# Importing libraries
import random as rnd
import copy
import json

# Number of cars
CarNum = 10
# Number of Trajectory Points
TrajectoryPoints = 3000

# Creating the class for defining atributes of car
class Car:
    def __init__(self,Latitude,Longitude):
        self.name = ''
        self.company = ''
        self.year = ''
		# position of a car is being saved in a python dictionary
        self.position = {'latitude':Latitude,'longitude':Longitude}
		
		
# The main function  
def DatasetBuilder(CarNum,TrajectoryPoints):

    cars = [] 
    lat = []
    lon = []
	
	# Entries for car attributes setting
    
    for i in range(CarNum):
        while True:
            try:
                Lat = float(input(f'Please enter initial latitude of the car #{i+1}: '))
                Lon = float(input(f'Please enter initial longitude of the car #{i+1}: '))
                assert -90<Lat<90 and -90<Lon<90,'Oops!'
                lat.append(Lat)
                lon.append(Lon)
                break
            except AssertionError:
                print('Oops! Latitude and longitude must be between 90 and -90!')
                continue
            
        car = Car(Latitude = lat[i] ,Longitude = lon[i])
        car.name = input(f'Please enter the name of the car #{i+1}: ')
        car.company = input(f'Please enter the company of the car #{i+1}: ')
        car.year = input(f'Please enter the year of fabrication of the car #{i+1}: ')
        cars.append(car)
	# Gathering all of the car instances
    Dataset = [car.__dict__ for car in cars]
    Copyholder = []

	# Building the trajectory
    for i in range(TrajectoryPoints):
        for j in range(CarNum):
            w = rnd.random()
			# Put random number in the interval [-1,1]
            lat[j] += (2*w - 1)
            lon[j] += (2*w - 1)
			# Copying each instance and changing their position attribute
            Copyholder.append(copy.deepcopy(cars[j]))
            Copyholder[j].__dict__['position']['latitude'] = round(lat[j],2)
            Copyholder[j].__dict__['position']['longitude'] = round(lon[j],2)
            Dataset.append(Copyholder[j].__dict__)
        Copyholder.clear()
	# Saving the data as a json file
    
    try:
        with open('Dataset.json' , 'w') as Json:
            json.dump(Dataset,Json, indent = 4)
    except:
        print('Something went wrong!')
    else:
        print('Dataset has been successfully stored in a json file in directory!')

if __name__ == '__main__':
    DatasetBuilder(CarNum,TrajectoryPoints)