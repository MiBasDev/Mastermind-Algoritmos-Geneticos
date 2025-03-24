import random

class Population:
    def __init__(self, colors, code_length, population_size):
        self.colors = colors
        self.code_length = code_length
        self.population_size = population_size
        self.individuals = self.initialize_population()
    
    def initialize_population(self):
        """ Genera la población inicial de combinaciones aleatorias """
        return [tuple(random.choices(self.colors, k=self.code_length)) for _ in range(self.population_size)]
    
    def mutate(self, mutation_rate):
        """ Muta un porcentaje de la población cambiando un color aleatorio """
        for _ in range(int(mutation_rate * len(self.individuals))):
            individual = list(random.choice(self.individuals))
            pos = random.randint(0, self.code_length - 1)
            new_color = random.choice([c for c in self.colors if c != individual[pos]])
            individual[pos] = new_color
            self.individuals.append(tuple(individual))
    
    def select(self, fitness_score, population_size):
        """ Selecciona los mejores individuos para la próxima generación """
        self.individuals = sorted(self.individuals, key=fitness_score, reverse=True)[:population_size]
