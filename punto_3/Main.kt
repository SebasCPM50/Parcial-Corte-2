fun main() {
    val calcCientifica = CalculadoraCientifica()
    
    println("Operaciones básicas:")
    println("5 + 3 = ${calcCientifica.sumar(5.0, 3.0)}")
    println("10 - 4 = ${calcCientifica.restar(10.0, 4.0)}")
    println("6 * 7 = ${calcCientifica.multiplicar(6.0, 7.0)}")
    println("15 / 3 = ${calcCientifica.dividir(15.0, 3.0)}")
    
    println("Funciones científicas:")
    calcCientifica.establecerModoGrados()
    println("Modo actual: ${calcCientifica.obtenerModo()}")
    println("sin(30°) = ${calcCientifica.seno(30.0)}")
    println("cos(60°) = ${calcCientifica.coseno(60.0)}")
    println("tan(45°) = ${calcCientifica.tangente(45.0)}")
    
    calcCientifica.establecerModoRadianes()
    println("Modo actual: ${calcCientifica.obtenerModo()}")
    println("sin(π/6) = ${calcCientifica.seno(Math.PI / 6)}")
    
    println("Potencias y raíces:")
    println("2^8 = ${calcCientifica.potencia(2.0, 8.0)}")
    println("√64 = ${calcCientifica.raizCuadrada(64.0)}")
    println("∛27 = ${calcCientifica.raizNesima(27.0, 3.0)}")
    
    println("Logaritmos:")
    println("ln(e) = ${calcCientifica.logaritmoNatural(Math.E)}")
    println("log(100) = ${calcCientifica.logaritmoBase10(100.0)}")
    
    println("Operaciones binarias:")
    println("1010 (binario) = ${calcCientifica.binarioADecimal("1010")} (decimal)")
    println("15 (decimal) = ${calcCientifica.decimalABinario(15)} (binario)")
    println("1010 + 1100 = ${calcCientifica.sumarBinarios("1010", "1100")}")
    
    println("Funciones de memoria:")
    calcCientifica.memoriaGuardar(42.0)
    println("Memoria guardada: ${calcCientifica.memoriaObtener()}")
    calcCientifica.memoriaSumar(8.0)
    println("Memoria después de M+: ${calcCientifica.memoriaObtener()}")
    
    println("Manejo de excepciones:")
    try {
        calcCientifica.dividir(10.0, 0.0)
    } catch (e: ArithmeticException) {
        println("Excepción capturada: ${e.message}")
    }
    
    try {
        calcCientifica.raizCuadrada(-4.0)
    } catch (e: ArithmeticException) {
        println("Excepción capturada: ${e.message}")
    }
    
    println("Polimorfismo:")
    println("Suma de enteros: ${calcCientifica.sumar(5, 3)}")
    println("Suma de doubles: ${calcCientifica.sumar(5.5, 3.2)}")
    println("Suma de floats: ${calcCientifica.sumar(5.5f, 3.2f)}")
    
    println("Operaciones con matrices:")
    val matriz1 = CalculadoraCientifica.Matriz2x2(1.0, 2.0, 3.0, 4.0)
    val matriz2 = CalculadoraCientifica.Matriz2x2(5.0, 6.0, 7.0, 8.0)
    val sumaMatrices = calcCientifica.sumarMatrices(matriz1, matriz2)
    println("Suma de matrices: [[${sumaMatrices.a11}, ${sumaMatrices.a12}], [${sumaMatrices.a21}, ${sumaMatrices.a22}]]")
}