class PointsForPlace():
    def __init__(self):
        self.points = 0
        
    def get_points_for_place(self, place):
        self.place = place
        if place > 100:
            print(f"Баллы начисляются только первым 100 участникам")
            return 0 
        elif place < 1:
            print(f'Спортсмен не может занять нулевое или отрицательное место')
            return 0 
        else:
            self.points = 101 - place
            return self.points

class PointsForMeters():
    def __init__(self):
        self.points = 0
        
    def get_points_for_meters(self, meters):
        self.meters = int(meters)
        if meters < 0:
            print(f'Количество метров не может быть отрицательным')
            return 0
        else:
            self.points = meters * 0.5
            return int(self.points)
    
class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()
        self.total = 0
        
    def get_total_points(self, place, meters):
        self.total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return int(self.total)
        
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))      