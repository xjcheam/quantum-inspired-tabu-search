from .QTS import QTS

class NQTS(QTS):
    def __init__(self, generation, n_solution, n_choice, fitness_function, optimization="max", theta=0.0004):
        QTS.__init__(self, generation, n_solution, n_choice, fitness_function, optimization, theta)

    def update(self):
        for i in range(self.n_choice):
            if self.beta[i] > 0.5 and self.best_solution[i] == 0 and self.worst_solution[i] == 1:
                self.beta[i] = 1 - self.beta[i]
            elif self.beta[i] < 0.5 and self.best_solution[i] == 1 and self.worst_solution[i] == 0:
                self.beta[i] = 1 - self.beta[i]

        for i in range(self.n_choice):
            if self.best_solution[i] == 1 and self.worst_solution[i] == 0:
                self.beta[i] += self.theta
            elif self.best_solution[i] == 0 and self.worst_solution[i] == 1:
                self.beta[i] -= self.theta
