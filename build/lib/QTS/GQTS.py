from .QTS import QTS

import copy
import numpy as np

class GQTS(QTS):
    def __init__(self, generation, n_solution, n_choice, fitness_function, optimization = "max", theta=0.0004):
        QTS.__init__(self, generation, n_solution, n_choice, fitness_function, optimization, theta)
        self.global_best = 0
        self.global_best_solution = np.zeros(self.n_choice, dtype=int)

    def fitness(self):
        self.best = 0
        self.best_solution = np.zeros(self.n_choice, dtype=int)
        self.worst = 0
        self.worst_solution = np.zeros(self.n_choice, dtype=int)

        for s in range(self.n_solution):
            fitness_value = self.fitness_function.get_fitness(self.solution[s])

            if self.optimization == "max":
                if fitness_value > self.best:
                    self.best = copy.deepcopy(fitness_value)
                    self.best_solution = copy.deepcopy(self.solution[s])

                if fitness_value < self.worst or self.worst == 0:
                    self.worst = copy.deepcopy(fitness_value)
                    self.worst_solution = copy.deepcopy(self.solution[s])
            elif self.optimization == "min":
                if fitness_value < self.best:
                    self.best = copy.deepcopy(fitness_value)
                    self.best_solution = copy.deepcopy(self.solution[s])

                if fitness_value > self.worst or self.worst == 0:
                    self.worst = copy.deepcopy(fitness_value)
                    self.worst_solution = copy.deepcopy(self.solution[s])

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
            if self.global_best_solution[i] == 1 and self.worst_solution[i] == 0:
                self.beta[i] += self.theta
            elif self.global_best_solution[i] == 0 and self.worst_solution[i] == 1:
                self.beta[i] -= self.theta

    def get_best(self):
        return self.global_best, self.global_best_solution