#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batches = -1
    for ingredient, amount in recipe.items():
        print(f'{ingredient}, {amount}')
        batch = ingredients[ingredient] // amount
        print(f'{batch}')
        if batch < max_batches or max_batches == -1:
            max_batches = batch
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 50, 'butter': 10, 'flour': 5}
    ingredients = {'milk': 200, 'butter': 100, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
