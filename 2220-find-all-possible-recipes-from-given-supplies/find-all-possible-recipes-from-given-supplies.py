from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        count = {}  # number of ingredients each recipe needs
        graph = defaultdict(list)  # maps ingredient -> list of recipes that require it

        # Build the graph and count dependencies
        for i, recipe in enumerate(recipes):
            count[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)
        
        avail = set(supplies)
        queue = deque(supplies)  # start with initial supplies
        result = []

        while queue:
            ing = queue.popleft()
            # For each recipe that depends on this ingredient
            for recipe in graph[ing]:
                count[recipe] -= 1  # reduce the dependency count
                if count[recipe] == 0:
                    # All ingredients are available, so add the recipe
                    result.append(recipe)
                    avail.add(recipe)
                    queue.append(recipe)
        
        return result
