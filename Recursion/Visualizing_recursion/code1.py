#!/usr/bin/env python3

import turtle

my_turtle = turtle.Turtle()
my_window = turtle.Screen()

def draw_spiral(my_turtle, linelen):
    if linelen > 0:
        my_turtle.forward(linelen)
        my_turtle.right(90)
        draw_spiral(my_turtle, linelen - 5)

draw_spiral(my_turtle, 100)
my_window.exitonclick()
