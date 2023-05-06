import copy
import random

# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs) -> None:
        self.arguments = dict(kwargs)
        self.balls = list()
        for k,v in self.arguments.items():
            for _ in range(v):
                self.balls.append(k)
        self.contents = self.balls.copy()

    def draw(self, number_of_balls):
        drawn_balls = list()
        self.contents = self.balls.copy()
        if number_of_balls >= len(self.contents):
            return self.balls
        for _ in range(number_of_balls):
            ball = random.choice(self.contents)
            drawn_balls.append(ball)
            self.contents.remove(ball)
        
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    exact_draws = 0

    for n in range(num_experiments):
        draw_dict = dict()
        copy_hat = copy.copy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)
        found = True
        for ball in balls_drawn:
            if ball not in draw_dict:
                draw_dict[ball] = 1
            else:
                draw_dict[ball] += 1
        for key in expected_balls:
            if key in draw_dict:
                if draw_dict[key] < expected_balls[key]:
                    found = False
                    break
            else:
                found = False
                break
        if found == True:
            exact_draws += 1

    return exact_draws / num_experiments