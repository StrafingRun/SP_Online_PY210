"""
Test code for circle.py
"""

import pytest
import math

from circle import *

########
# Step 1
########
"""
Create a circle class that has c = Circle(5) as the signature
Ensure radius is a required attribute
"""


def test_init():
    """
    Test that we pass the
    """
    # check for missing radius intput
    with pytest.raises(TypeError):
        c = Circle()

    c = Circle(5)
    assert c.radius == 5


########
# Step 2
########
"""
Add a diameter property so the user can get the diameter of the circle
"""


def test_diameter():
    """Test that diameter attribute exists and twice the radius"""
    c = Circle(5)

    assert c.diameter == 10


########
# Step 3
########
"""
Allow the user to set the diameter of the circle.
Ensure that the radius and diameter are always in sync.
Make the diameter and radius both properties.
"""


def test_diameter_radius_property():
    c = Circle(5)

    assert c.radius == 5
    assert c.diameter == 10

    # check that diameter change works and updates radius
    c.diameter = 20

    assert c.diameter == 20
    assert c.radius == 10

    # check that radius change works and updates diameter
    c.radius = 25

    assert c.radius == 25
    assert c.diameter == 50


########
# Step 4
########
"""
Add an area property so the user can get the property of the circle.

Make sure they user can't set the area.
"""


def test_area():

    c = Circle(5)

    # test area gets calculated properly
    assert c.area == 5*5*math.pi

    # test user can't set area property
    with pytest.raises(AttributeError):
        c.area = 12

    # ensure area gets updated with radius and diameter updates
    c.diameter = 20
    assert c.radius == 10
    assert c.area == 100*math.pi

    c.radius = 20
    assert c.diameter == 40
    assert c.area == 20*20*math.pi


########
# Step 5
########
"""
Created an alternate initializer so the user can initialize from a diameter.
"""


def test_initialize_diameter():
    c = Circle.from_diameter(10)

    # test radius, area, diameter properties
    assert c.diameter == 10
    assert c.radius == 5
    assert c.area == 25*math.pi

    # test chaning radius updates diameter and area
    c.radius = 10
    assert c.diameter == 20
    assert c.area == 100*math.pi

    # test initializer fails on empty diameter
    with pytest.raises(TypeError):
        c = Circle.from_diameter()


########
# Step 6
########
"""
Create a __str___ method to create the informal string representation of cirlces
Create a __repr__ method to create the formal string representation of circle

print(c) == "Circle with radius: 4.000000"

repr(c) == "Circle(5)"
"""


def test__str__method():
    c = Circle(5)

    print(c)
    d = c.__str__()
    assert d == "Circle with radius: 5.000000"


def test__repr_method():
    c = Circle(5)

    repr(c)
    d = c.__repr__()
    assert d == "Circle(5)"
