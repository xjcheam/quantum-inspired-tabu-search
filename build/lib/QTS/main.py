from ANGQTS import ANGQTS

class Fitness:
    def __init__(self):
        self.solution = None
        self.fitness = 0

    def calFitness(self):
        i = 0
        self.fitness = 0
        for item in reversed(self.solution):
            self.fitness += item * (2 ** (i))
            i += 1

    def get_fitness(self, solution):
        self.solution = solution
        self.calFitness()
        return self.fitness

fitness_function = Fitness()
qts = ANGQTS(50, 10, 10, fitness_function, "max")
qts.run()
best, best_solution = qts.get_best()
print(best, best_solution)
