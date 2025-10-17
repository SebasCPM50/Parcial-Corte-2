import mesa
import math

class AgenteSuma(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    def operar(self, a, b): return a + b

class AgenteResta(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    def operar(self, a, b): return a - b

class AgenteMultiplicacion(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    def operar(self, a, b): return a * b

class AgenteDivision(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    def operar(self, a, b): 
        if b == 0: raise ValueError("División por cero")
        return a / b

class AgentePotencia(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    def operar(self, a, b): return a ** b

class AgenteSeno(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.modo = "radianes"
    def operar(self, a): 
        if self.modo == "grados": a = math.radians(a)
        return math.sin(a)

class AgenteCoseno(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.modo = "radianes"
    def operar(self, a): 
        if self.modo == "grados": a = math.radians(a)
        return math.cos(a)

class AgenteEntradaSalida(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.modo_trig = "radianes"
    
    def procesar(self, expresion):
        expresion = expresion.replace(" ", "")
        
        if expresion.startswith("/"):
            return self._procesar_comando(expresion)
        
        for op in ['+', '-', '*', '/', '^']:
            if op in expresion:
                partes = expresion.split(op)
                if len(partes) == 2:
                    try:
                        a, b = float(partes[0]), float(partes[1])
                        return self._operacion_binaria(op, a, b)
                    except: pass
        
        if expresion.startswith("sin(") and expresion.endswith(")"):
            try:
                valor = float(expresion[4:-1])
                return self.model.agente_seno.operar(valor)
            except: pass
        elif expresion.startswith("cos(") and expresion.endswith(")"):
            try:
                valor = float(expresion[4:-1])
                return self.model.agente_coseno.operar(valor)
            except: pass
        
        return "Error: Expresión no válida"
    
    def _operacion_binaria(self, operador, a, b):
        agentes = {
            '+': self.model.agente_suma,
            '-': self.model.agente_resta,
            '*': self.model.agente_multiplicacion,
            '/': self.model.agente_division,
            '^': self.model.agente_potencia
        }
        return agentes[operador].operar(a, b)
    
    def _procesar_comando(self, comando):
        if comando == "/modo radianes":
            self.modo_trig = "radianes"
            self.model.agente_seno.modo = "radianes"
            self.model.agente_coseno.modo = "radianes"
            return "Modo cambiado a radianes"
        elif comando == "/modo grados":
            self.modo_trig = "grados"
            self.model.agente_seno.modo = "grados"
            self.model.agente_coseno.modo = "grados"
            return "Modo cambiado a grados"
        elif comando == "/help":
            return "Comandos: /modo radianes, /modo grados, /help\nOperaciones: + - * / ^ sin() cos()"
        return "Comando no reconocido"

class ModeloCalculadora(mesa.Model):
    def __init__(self):
        super().__init__()
        self.agente_entrada = AgenteEntradaSalida("entrada", self)
        self.agente_suma = AgenteSuma("suma", self)
        self.agente_resta = AgenteResta("resta", self)
        self.agente_multiplicacion = AgenteMultiplicacion("multiplicacion", self)
        self.agente_division = AgenteDivision("division", self)
        self.agente_potencia = AgentePotencia("potencia", self)
        self.agente_seno = AgenteSeno("seno", self)
        self.agente_coseno = AgenteCoseno("coseno", self)
        
        self.schedule = mesa.time.RandomActivation(self)
        for attr in dir(self):
            if attr.startswith('agente_'):
                self.schedule.add(getattr(self, attr))
    
    def evaluar(self, expresion):
        return self.agente_entrada.procesar(expresion)

def main():
    calc = ModeloCalculadora()
    print("Calculadora con Agentes - Comandos: /help")
    
    while True:
        expr = input("> ")
        if expr.lower() == 'salir': break
        resultado = calc.evaluar(expr)
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()