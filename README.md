# Parcial-Corte-2
Parcial de Paradigmas de Programación - Sebastián Chaux Palencia
# 1. Perceptrón Simple

Este proyecto implementa un modelo de **Perceptrón** —una de las primeras redes neuronales artificiales— para la clasificación binaria.  
El perceptrón aprende a separar datos en dos clases mediante un proceso iterativo de ajuste de pesos basado en el error.

---

## ¿Cómo funciona?

El perceptrón sigue los siguientes pasos principales:

1. **Inicialización:**  
   Se asignan valores aleatorios a los pesos y al sesgo (bias).  
   También se define una tasa de aprendizaje `α` (entre 0 y 1).

2. **Cálculo de salida:**  
   Para cada patrón de entrada `x`, se calcula la salida neta:
   
neta = Σ(w_i * x_i) + b

Luego se aplica una función de activación (umbral):


y_pred = 1 si neta ≥ 0
y_pred = 0 si neta < 0


3. **Actualización de pesos:**  
Si la salida obtenida (`y_pred`) no coincide con la deseada (`y`), se ajustan los pesos:


w_i = w_i + α * (y - y_pred) * x_i
b = b + α * (y - y_pred)

4. **Iteración:**  
El proceso se repite hasta que el error total del modelo sea mínimo o hasta alcanzar un número máximo de iteraciones.

---
## Diagrama de Flujo (Solución)

<img width="507" height="1234" alt="image" src="https://github.com/user-attachments/assets/97d8a055-3da5-4aa4-8680-6cea97f23ddd" />

## Cómo ejecutarlo

### Opción 1: Desde Python
1. Asegúrate de tener Python instalado (versión 3.8 o superior).
2. Crea un archivo `perceptron.py` con el pseudocódigo o la implementación correspondiente.
3. Ejecuta:
```bash
python perceptron.py
```

# 2. Calculadora con Agentes (MESA - Python)

Este punto implementa una **calculadora multiagente** usando el framework **[MESA](https://mesa.readthedocs.io/)** en Python.  
Cada agente tiene una responsabilidad específica (sumar, restar, multiplicar, etc.), y se comunican entre sí mediante un **modelo central** que coordina las operaciones.

---

## Diagrama de Flujo (Solución)

<img width="1375" height="576" alt="image" src="https://github.com/user-attachments/assets/8b2955fc-f6a2-4c6f-ae86-8d4a1520d0ad" />


## Funcionamiento

El sistema está compuesto por distintos **agentes especializados**:

- `AgenteEntradaSalida`: recibe la expresión del usuario, la analiza y decide a qué agente enviar la operación.  
- `AgenteSuma`, `AgenteResta`, `AgenteMultiplicacion`, `AgenteDivision`, `AgentePotencia`: realizan las operaciones aritméticas básicas.  
- `AgenteSeno` y `AgenteCoseno`: calculan funciones trigonométricas, pudiendo trabajar en **radianes o grados**.  

La comunicación se realiza internamente a través del **modelo principal (`ModeloCalculadora`)**, que contiene y coordina a todos los agentes.

### Flujo general del sistema

1. El usuario ingresa una expresión (por ejemplo: `5+3`, `sin(90)`, `cos(3.14)` o `/modo grados`).  
2. El `AgenteEntradaSalida` analiza el texto y:
   - Si es una **operación binaria**, delega la tarea al agente correspondiente.
   - Si es una **función trigonométrica**, envía el cálculo al agente adecuado.
   - Si es un **comando**, modifica el modo de trabajo o muestra ayuda.  
3. El resultado es procesado y mostrado al usuario en consola.

---

## Requisitos

- Python 3.9 o superior  
- Biblioteca MESA instalada  

Instalación de dependencias:
```bash
pip install mesa
```

# 3. Calculadora Científica en Kotlin

Este proyecto implementa una **Calculadora Científica** en Kotlin utilizando los principios de **Programación Orientada a Objetos (POO)**.  
El programa incluye operaciones básicas, funciones científicas, manejo de memoria y operaciones con matrices.

---

## Funcionamiento General

El sistema se compone de **tres clases principales**:

### `Calculadora`
Clase base que contiene:
- Operaciones básicas: `sumar`, `restar`, `multiplicar`, `dividir`.
- Manejo de memoria: guardar, sumar, restar, limpiar.
- Almacenamiento del resultado actual.

### `CalculadoraCientifica`
Hereda de `Calculadora` y añade:
- Funciones trigonométricas (`seno`, `coseno`, `tangente`).
- Potencias y raíces.
- Logaritmos y exponenciales.
- Cálculo de factoriales.
- Conversión entre binario y decimal.
- Operaciones con matrices 2x2 (suma y multiplicación).

### `Matriz2x2`
Clase de datos interna usada para representar matrices pequeñas y realizar operaciones matemáticas entre ellas.

---
## Diagrama de Flujo (Solución)

<img width="524" height="858" alt="image" src="https://github.com/user-attachments/assets/86c21c7f-9035-42f2-9c62-c754ccb209d3" />


## Cómo Ejecutarlo

### **1. Requisitos**
- Tener instalado **Kotlin** o usar un entorno como **IntelliJ IDEA** o **VS Code con el plugin de Kotlin**.
- Versión recomendada: Kotlin 1.9 o superior.

### **2. Clonar o descargar el proyecto**
```bash
git clone https://github.com/tu-usuario/calculadora-cientifica.git
cd calculadora-cientifica
```
### **3. Compilar el programa
kotlinc Calculadora.kt -include-runtime -d Calculadora.jar

### **4. Ejecutar
java -jar Calculadora.jar
