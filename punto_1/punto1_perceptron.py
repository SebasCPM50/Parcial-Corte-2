import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Punto:
    def __init__(self, x, y, etiqueta):
        self.x = x
        self.y = y
        self.etiqueta = etiqueta
        self.prediccion = 0
        self.color = "skyblue" if etiqueta == -1 else "salmon"

    def actualizar_color(self, correcto):
        if correcto:
            self.color = "palegreen" if self.etiqueta == -1 else "lightcoral"
        else:
            self.color = "royalblue" if self.etiqueta == -1 else "crimson"


class Perceptron:
    def __init__(self, tasa=0.1, max_epocas=100):
        self.tasa = tasa
        self.max_epocas = max_epocas
        self.pesos = np.random.uniform(-1, 1, 2)
        self.bias = np.random.uniform(-1, 1)
        self.epoca = 0
        self.errores = []
        self.finalizado = False

    def predecir(self, x):
        act = np.dot(self.pesos, x) + self.bias
        return 1 if act >= 0 else -1

    def entrenar(self, puntos):
        error_total = 0
        for p in puntos:
            salida = self.predecir([p.x, p.y])
            diferencia = p.etiqueta - salida
            if diferencia != 0:
                self.pesos += self.tasa * diferencia * np.array([p.x, p.y])
                self.bias += self.tasa * diferencia
                error_total += abs(diferencia)
            p.actualizar_color(diferencia == 0)

        self.errores.append(error_total)
        self.epoca += 1
        if error_total == 0 or self.epoca >= self.max_epocas:
            self.finalizado = True

    def frontera(self, limite):
        if abs(self.pesos[1]) > 1e-10:
            xs = np.linspace(limite[0], limite[1], 100)
            ys = -(self.pesos[0] * xs + self.bias) / self.pesos[1]
        else:
            xs = np.full(100, -self.bias / self.pesos[0])
            ys = np.linspace(limite[0], limite[1], 100)
        return xs, ys


class SimuladorPerceptron:
    def __init__(self, n=60, tasa=0.1, max_epocas=100, rango=10):
        self.rango = rango
        self.puntos = []
        self.modelo = Perceptron(tasa, max_epocas)
        self.generar_datos(n)

    def generar_datos(self, n):
        m = random.uniform(-1, 1)
        b = random.uniform(-self.rango / 4, self.rango / 4)
        for _ in range(n):
            x = random.uniform(-self.rango, self.rango)
            y = random.uniform(-self.rango, self.rango)
            etiqueta = 1 if y > m * x + b else -1
            self.puntos.append(Punto(x, y, etiqueta))

    def paso(self):
        if not self.modelo.finalizado:
            self.modelo.entrenar(self.puntos)

class InterfazPerceptron:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Simulación del Perceptrón — Visual Studio Layout")
        self.ventana.geometry("1200x700")
        self.ventana.configure(bg="#1e1e1e")

        self.simulador = None
        self.ejecutando = False

        self._crear_ui()
        self.ventana.mainloop()

    def _crear_ui(self):
        panel = tk.Frame(self.ventana, bg="#252526", width=250)
        panel.pack(side=tk.LEFT, fill=tk.Y)
        panel.pack_propagate(False)

        titulo = tk.Label(panel, text="⚙️ Control del Modelo", bg="#252526", fg="white", font=("Segoe UI", 11, "bold"))
        titulo.pack(pady=10)

        tk.Label(panel, text="Tasa de aprendizaje", bg="#252526", fg="white").pack(pady=(10, 0))
        self.tasa_var = tk.DoubleVar(value=0.1)
        tk.Scale(panel, from_=0.01, to=1, resolution=0.01, orient="horizontal",
                 variable=self.tasa_var, bg="#252526", fg="white", troughcolor="#0078D7",
                 highlightthickness=0).pack(padx=10, fill=tk.X)

        tk.Label(panel, text="Iteraciones máximas", bg="#252526", fg="white").pack(pady=(10, 0))
        self.it_var = tk.IntVar(value=100)
        tk.Scale(panel, from_=10, to=500, orient="horizontal",
                 variable=self.it_var, bg="#252526", fg="white", troughcolor="#0078D7",
                 highlightthickness=0).pack(padx=10, fill=tk.X)

        tk.Button(panel, text="▶ Iniciar", bg="#0078D7", fg="white", font=("Segoe UI", 10, "bold"),
                  command=self.iniciar).pack(pady=(20, 5), fill=tk.X, padx=10)
        tk.Button(panel, text="⟳ Reiniciar", bg="#3A3D41", fg="white", font=("Segoe UI", 10),
                  command=self.reiniciar).pack(pady=5, fill=tk.X, padx=10)

        self.estado = tk.Label(panel, text="Listo para iniciar", bg="#252526", fg="#CCCCCC", wraplength=200, justify="left")
        self.estado.pack(pady=15, padx=10)

        contenedor = tk.Frame(self.ventana, bg="#1e1e1e")
        contenedor.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.figura = Figure(figsize=(6, 4), facecolor="#1e1e1e")
        self.ax_datos = self.figura.add_subplot(121)
        self.ax_error = self.figura.add_subplot(122)
        self.figura.subplots_adjust(wspace=0.3)

        for ax in [self.ax_datos, self.ax_error]:
            ax.set_facecolor("#2D2D30")
            ax.tick_params(colors="white")
            for spine in ax.spines.values():
                spine.set_color("white")

        self.canvas = FigureCanvasTkAgg(self.figura, contenedor)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Barra inferior de estado
        self.barra = tk.Label(self.ventana, text="Esperando acción...", bg="#0078D7", fg="white", anchor="w")
        self.barra.pack(fill=tk.X, side=tk.BOTTOM)

    def iniciar(self):
        if self.ejecutando:
            self.ejecutando = False
            return

        self.simulador = SimuladorPerceptron(
            n=60,
            tasa=self.tasa_var.get(),
            max_epocas=self.it_var.get(),
            rango=10
        )
        self.ejecutando = True
        self.barra.config(text="Entrenando perceptrón...")
        threading.Thread(target=self._entrenar, daemon=True).start()

    def reiniciar(self):
        self.ejecutando = False
        self.ax_datos.clear()
        self.ax_error.clear()
        self.canvas.draw()
        self.barra.config(text="Reiniciado correctamente.")
        self.estado.config(text="Modelo reiniciado, listo para ejecutar nuevamente.")

    def _entrenar(self):
        while self.ejecutando and not self.simulador.modelo.finalizado:
            self.simulador.paso()
            self._actualizar()
            time.sleep(0.1)
        self.ejecutando = False
        self.barra.config(text="Entrenamiento finalizado.")

    def _actualizar(self):
        modelo = self.simulador.modelo
        puntos = self.simulador.puntos

        self.ax_datos.clear()
        self.ax_error.clear()

        for ax in [self.ax_datos, self.ax_error]:
            ax.set_facecolor("#2D2D30")
            ax.tick_params(colors="white")
            for spine in ax.spines.values():
                spine.set_color("white")

        for p in puntos:
            marcador = "o" if p.etiqueta == -1 else "^"
            self.ax_datos.scatter(p.x, p.y, c=p.color, marker=marcador)

        xs, ys = modelo.frontera((-self.simulador.rango, self.simulador.rango))
        self.ax_datos.plot(xs, ys, color="lime", linewidth=1.5)
        self.ax_datos.set_title(f"Época {modelo.epoca}", color="white")

        self.ax_error.plot(range(len(modelo.errores)), modelo.errores, color="tomato", linewidth=2)
        self.ax_error.set_title("Error por Época", color="white")

        self.canvas.draw()

        error_actual = modelo.errores[-1] if modelo.errores else 0
        self.estado.config(text=f"Época: {modelo.epoca}\nError total: {error_actual}")

if __name__ == "__main__":
    InterfazPerceptron()

