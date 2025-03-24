import os
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, history_scores):
        self.history_scores = history_scores
    
    def plot(self, output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'doc')):
        """ Grafica todas las puntuaciones de cada generación con un color diferente """
        # Definir una lista de colores únicos para cada generación
        generation_colors = plt.cm.tab20.colors  # Tab20 tiene 20 colores únicos

        plt.figure(figsize=(10, 6))
        
        # Asignar colores diferentes para cada generación
        for gen in range(len(self.history_scores)):
            gen_scores = self.history_scores[gen]  # Puntuaciones de la generación
            color = generation_colors[gen % len(generation_colors)]  # Obtener un color único para cada generación
            plt.scatter([i+1 for i in range(len(gen_scores))], gen_scores, color=color)  # Graficar como puntos
        
        plt.xlabel("Iteración")
        plt.ylabel("Puntuación")
        plt.title("Evolución de las puntuaciones por generación")
        
        # Añadir leyenda
        plt.legend([f"Generación {i + 1}" for i in range(len(self.history_scores))], loc="upper right", fontsize=8)
        
        # Añadir grid
        plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5, zorder=1)

        # Establecer los ticks del eje X en cada iteración
        iterations = [i + 1 for i in range(len(self.history_scores[0]))]  # Todas las iteraciones
        plt.xticks(iterations, fontsize=8)

        # Asegurar que la carpeta exista antes de guardar el archivo
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "evolution_plot_all_scores_colored.png")
        
        # Guardar gráfico
        plt.savefig(output_path, bbox_inches='tight')
        plt.show()
