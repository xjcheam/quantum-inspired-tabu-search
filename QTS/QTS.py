import copy
import numpy as np

class QTS:
    def __init__(self, generation, n_solution, n_choice, fitness_function, optimization="max", theta=0.0004):
        self.generation = generation
        self.n_solution = n_solution
        self.n_choice = n_choice
        self.theta = theta
        self.beta = np.full((self.n_choice,), 0.5)  # the beta matrix is initialize here

        self.fitness_function = fitness_function
        self.optimization = optimization
        self.best = 0
        self.worst = 0
        self.solution = np.zeros((self.n_solution, self.n_choice), dtype=int)
        self.best_solution = np.zeros(self.n_choice, dtype=int)
        self.worst_solution = np.zeros(self.n_choice, dtype=int)

    def measure(self):
        self.solution = np.zeros((self.n_solution, self.n_choice), dtype=int)
        rand_mat = np.random.random((self.n_solution, self.n_choice))
        for s in range(self.n_solution):
            for c in range(self.n_choice):
                if rand_mat[s][c] < 0.5:
                    self.solution[s][c] = 1

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
        for i in range(self.n_choice):
            if self.best_solution[i] == 1 and self.worst_solution[i] == 0:
                self.beta[i] += self.theta
            elif self.best_solution[i] == 0 and self.worst_solution[i] == 1:
                self.beta[i] -= self.theta

    def run(self):
        for i in range(self.generation):
            self.measure()
            self.fitness()
            self.update()

    def get_beta(self):
        return self.beta

    def get_best(self):
        return self.best, self.best_solution