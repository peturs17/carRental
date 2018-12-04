from repositories.CarRepository import CarRepository

class CarService:
    def __init__(self):
        self.__car_repo = CarRepository()

    def add_car(self, car):
        if self.is_valid_car(car):
            self.__car_repo.add_car(car)

    def is_valid_car(self, car):
        #here should be some code to
        #validate the car
        return True

    def get_cars(self):
        return self.__car_repo.get_cars()

    def get_cars_by_genre(self, genre):
        pass