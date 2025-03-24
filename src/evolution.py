import random
from src.population import Population

class Evolution:
    def __init__(self, colors, code_length, population_size, max_generations, mutation_rate, secret_code):
        self.colors = colors
        self.code_length = code_length
        self.population_size = population_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.secret_code = secret_code
        self.population = Population(colors, code_length, population_size)
    
    def fitness_score(self, individual):
        """ Evalúa cuántos colores están bien colocados (orden correcto) """
        score = 0
        for a, b in zip(individual, self.secret_code):
            if a == b:
                score += 1
            else:
                score -= 1
        return score
    
    def select_parents(self):
        """ Selección por ruleta: mayor fitness, mayor probabilidad de ser elegido """
        scores = [self.fitness_score(ind) for ind in self.population.individuals]
        min_score = min(scores)
        adjusted_scores = [score - min_score + 1 for score in scores]
        total = sum(adjusted_scores)
        if total == 0:
            return random.sample(self.population.individuals, self.population_size // 2)
        return random.choices(self.population.individuals, weights=adjusted_scores, k=self.population_size // 2)
    
    def crossover(self, parents):
        """ Crossover de punto único en la posición 2 """
        offspring = []
        random.shuffle(parents)
        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                p1, p2 = parents[i], parents[i+1]
                child1 = p1[:2] + p2[2:]
                child2 = p2[:2] + p1[2:]
                offspring.extend([child1, child2])
        return offspring
    
    def mutate_population(self):
        """ Muta un porcentaje de la población cambiando un color aleatorio """
        self.population.mutate(self.mutation_rate)
    
    def select_next_generation(self):
        """ Selecciona los mejores individuos para la próxima generación """
        self.population.select(self.fitness_score, self.population_size)
    
    def check_solution(self):
        """ Verifica si se ha encontrado el código secreto """
        for ind in self.population.individuals:
            if self.fitness_score(ind) == self.code_length:
                return ind
        return None
