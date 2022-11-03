from .GQTS import GQTS

import copy

class GNQTS(GQTS):
    def __init__(self, generation, n_solution, n_choice, fitness_function, optimization="max", theta=0.0004):
        GQTS.__init__(self, generation, n_solution, n_choice, fitness_function, optimization, theta)

    def update(self):
        if self.optimization == "max":
            if self.best >= self.global_best:
                self.global_best = copy.deepcopy(self.best)
                self.global_best_solution = copy.deepcopy(self.best_solution)
        elif self.optimization == "min":
            if self.best <= self.global_best:
                self.global_best = copy.deepcopy(self.best)
                self.global_best_solution = copy.deepcopy(self.best_solution)

        for i in range(self.n_choice):
            if self.beta[i] > 0.5 and self.global_best_solution[i] == 0 and self.worst_solution[i] == 1:
                self.beta[i] = 1 - self.beta[i]
            elif self.beta[i] < 0.5 and self.global_best_solution[i] == 1 and self.worst_solution[i] == 0:
                self.beta[i] = 1 - self.beta[i]

        for i in range(self.n_choice):
            if self.global_best_solution[i] == 1 and self.worst_solution[i] == 0:
                self.beta[i] += self.theta
            elif self.global_best_solution[i] == 0 and self.worst_solution[i] == 1:
                self.beta[i] -= self.theta
