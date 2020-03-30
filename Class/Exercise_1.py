"""
Exercise 1
Follow the steps:

Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments.
Make sure to set these appropriately in the body of the __init__()method.
Create a variable named number_of_sides and set it equal to 3.
Create a method named check_angles. The sum of a triangle's three angles is
It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
Print out my_triangle.number_of_sides and print out my_triangle.check_angles().

"""
from pip._vendor.distlib.compat import raw_input


class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle_1 = angle1
        self.angle_2 = angle2
        self.angle_3 = angle3
        self.number_of_sides = 3

    def check_angles(self):
        if (self.angle_1 + self.angle_2 + self.angle_3) == 180:
            print("True, Value: ",self.angle_1, self.angle_2, self.angle_3)
            print("number_of_sides: ", self.number_of_sides)

        else:
            print("False, Value: ",self.angle_1, self.angle_2, self.angle_3)
            print("number_of_sides: ", self.number_of_sides)


if __name__ == "__main__":
    angle_1 = int(raw_input("Sayi giriniz: "))
    my_triangle = Triangle(angle_1, 50, 50)
    my_triangle.check_angles()

    my_triangle2 = Triangle(angle_1, 85, 90)
    my_triangle2.check_angles()