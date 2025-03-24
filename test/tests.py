import os
from src.evolution import Evolution
from src.plotter import Plotter

# Definir un código secreto para las pruebas
SECRET_CODE = ['🔴', '🟢', '🔵', '🟡']

# 1. Test Fitness Score
def test_fitness_score():
    colors = ['🔴', '🟢', '🔵', '🟡', '🟠', '🟣']
    evolution = Evolution(colors, 4, 10, 12, 0.1, SECRET_CODE)
    
    # Individuo con 3 colores correctos
    individual = ['🔴', '🟢', '🔵', '🟡']
    assert evolution.fitness_score(individual) == 4  # Todos los colores deben ser correctos
    
    # Individuo con 1 color correcto
    individual = ['🔴', '🟠', '🟣', '🔵']
    assert evolution.fitness_score(individual) == -2  # Solo 1 color correcto

# 2. Test Verificación de la Solución
def test_check_solution():
    colors = ['🔴', '🟢', '🔵', '🟡', '🟠', '🟣']
    evolution = Evolution(colors, 4, 10, 12, 0.1, SECRET_CODE)
    
    # Simular que la población ha encontrado el código secreto
    evolution.population.individuals = [SECRET_CODE]  # Establecer la población con el código secreto
    winner = evolution.check_solution()
    
    # Asegurarse de que la solución es la correcta
    assert winner == SECRET_CODE

# 3. Test Generación del Gráfico
def test_plotter():
    # Suponemos que `history_scores` es una lista de puntuaciones de generaciones anteriores.
    history_scores = [[1, 2, 3, 4, 5]] * 5  # Puntuaciones simuladas
    
    plotter = Plotter(history_scores)
    
    # Probar si el gráfico se guarda sin errores
    plotter.plot(output_dir="./test_plots")
    
    # Verificar si el archivo fue generado
    assert os.path.exists("./test_plots/evolution_plot_all_scores_colored.png")

