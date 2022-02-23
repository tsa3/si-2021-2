# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food


def setup():
    global vehicle
    global food
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    food = Food(9, 44, PVector(0, 0))

number = 0

def draw():
    background(25)
    mouse = PVector(mouseX, mouseY)
    vehicle.update()
    vehicle.display()
    food.update()
    food.display()
    
    global number
    
    vehicle.applyForce(food.position)
    
    if food.position.dist(vehicle.position) < 3:
        food.newState()
        number += 1
        
    text("Comidas: ", 50, 50)
    text(number, 110, 50)
