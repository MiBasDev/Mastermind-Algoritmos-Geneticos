import random
from src.evolution import Evolution
from src.plotter import Plotter

# Definimos los parámetros
COLORS = ['🔴', '🟢', '🔵', '🟡', '🟠', '🟣']
CODE_LENGTH = 4
POPULATION_SIZE = 60
MAX_GENERATIONS = 12
MUTATION_RATE = 0.1

# Código secreto aleatorio
secret_code = [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def main():
    print(f"*******************")
    print(f"* CÓDIGO OBJETIVO *")
    print(f"*   {' '.join(secret_code)}   *")
    print(f"*******************")
    
    # Crear objeto de evolución
    evolution = Evolution(COLORS, CODE_LENGTH, POPULATION_SIZE, MAX_GENERATIONS, MUTATION_RATE, secret_code)
    history_scores = []  # Almacenar las puntuaciones por generación
    
    for generation in range(MAX_GENERATIONS):
        print(f"\n-------------------")
        print(f"|  Generación {generation + 1}   |")
        scores = [evolution.fitness_score(ind) for ind in evolution.population.individuals]
        
        # Imprimir solo la mejor puntuación de la generación
        max_score = max(scores)
        best_individual = evolution.population.individuals[scores.index(max_score)]
        print(f"| {' '.join(best_individual)} ➔ {max_score} |")
        print(f"-------------------")
        
        winner = evolution.check_solution()
        if winner:
            print(f"\n***************************")
            print(f"*** DESCUBIERTO EN GEN{generation + 1} ***")
            print(f"***     {' '.join(winner)}     ***")
            print(f"***************************")
            break
        
        parents = evolution.select_parents()
        offspring = evolution.crossover(parents)
        evolution.population.individuals.extend(offspring)
        evolution.mutate_population()
        evolution.select_next_generation()

        # Guardar la puntuación de esta generación
        history_scores.append(scores)

    # Guardar la puntuación de la última generación (aunque se haya encontrado el código)
    history_scores.append([evolution.fitness_score(ind) for ind in evolution.population.individuals])

    if not winner:
        print("\nNo se encontró el código en el número máximo de generaciones.")
        print(f"El código era: {' '.join(secret_code)}")
    
    # Graficar los resultados
    plotter = Plotter(history_scores)
    plotter.plot()

if __name__ == "__main__":
    main()
