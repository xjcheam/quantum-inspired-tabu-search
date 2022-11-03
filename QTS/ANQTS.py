from .NQTS import NQTS

class ANQTS(NQTS):
    def __init__(self, generation, n_solution, n_choice, fitness_function, optimization, theta_upper=0.00125, theta_lower=0.00045):
        NQTS.__init__(self, generation, n_solution, n_choice, fitness_function, optimization)
        self.theta_upper = theta_upper
        self.theta_lower = theta_lower

    def update(self):
        for i in range(self.n_choice):
            if self.beta[i] > 0.5 and self.best_solution[i] == 0 and self.worst_solution[i] == 1:
                self.beta[i] = 1 - self.beta[i]
            elif self.beta[i] < 0.5 and self.best_solution[i] == 1 and self.worst_solution[i] == 0:
                self.beta[i] = 1 - self.beta[i]

        for i in range(self.n_choice):
            self.theta = self.theta_lower + self.theta_upper * (1 - (2 * abs(self.beta[i]) - 0.5))
            print(self.theta)
            if self.best_solution[i] == 1 and self.worst_solution[i] == 0:
                self.beta[i] += self.theta
            elif self.best_solution[i] == 0 and self.worst_solution[i] == 1:
                self.beta[i] -= self.theta
