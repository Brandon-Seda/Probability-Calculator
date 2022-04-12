import random
import copy
from collections import Counter

class Hat:

    def __init__(self, **balls):
        self.contents = []

        for k,v in balls.items():
            for c in range(0, v):
                self.contents.append(k)
    
    

    def draw(self, picks):
        removed_balls = []
        if picks >= len(self.contents):
                return self.contents
        for i in range(picks):
            ball = random.choice(self.contents)

            removed_balls.append(ball)
            self.contents.remove(ball)
        return removed_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = 0

    for e in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        taken_balls = Counter(drawn)
        expected = True

        for k, v in expected_balls.items():
            if k not in taken_balls.keys() or expected_balls.get(k) > taken_balls.get(k):
                expected = False
                break
        
        if expected == True:
            M += 1
        
        N += 1

        print(M, N)
    
    probability = M/N

    return probability

