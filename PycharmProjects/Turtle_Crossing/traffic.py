from cars import Car




class Traffic(Car):
    def __init__(self,CAR_AMOUNT = 3):
        super().__init__()
        self.batch = []
        self.car_count = CAR_AMOUNT
        self.create_traffic()
        # self.unique_loc()
        self.ht()

    def create_traffic(self):
        for car in range(self.car_count):
            car = Car()
            self.batch.append(car)

    def move_traffic(self):
        for car in self.batch:
            car.moving()

    def more_cars(self):
        self.batch.append(Car())


    # def unique_loc(self):
    #     for i in self.batch:
    #         for j in self.batch:
    #             # if i.ycor() == j.ycor() or i.ycor() == (j.ycor())+20 or i.ycor() == (j.ycor())-20:
    #             # if j.ycor()-20 <= i.ycor() <= j.ycor()+20:
    #             if i.distance(j) == 20:
    #                 print("collide")
    #                 j.update_origin()
    #             else:
    #                 print("pass")
