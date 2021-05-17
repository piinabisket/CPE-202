"""
Code for the CPE 202 Final.
Course: CPE 202
Quarter: Spring 2020
Author: Forrest Dudley
"""


class HowToFixRecipe:
    """
    Data definition for HowToFixRecipe,
    defining steps for a repair guide.
    Attributes:
        body (str): body of the step.
        parts (str): requires parts
    """
    def __init__(self, what_to_do=None, parts=None):
        self.parts = parts
        self.body = what_to_do

    def __eq__(self, other):
        return self.body == other.body, self.parts == other.parts

    def __repr__(self):
        return 'Required Parts: %s, Step: %s' % (self.parts, self.body)
