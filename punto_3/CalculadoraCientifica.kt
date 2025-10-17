class CalculadoraCientifica : Calculadora() {
    companion object {
        const val PI = 3.141592653589793
    }
    
    private var modoGrados: Boolean = true
    
    fun establecerModoGrados() { modoGrados = true }
    fun establecerModoRadianes() { modoGrados = false }
    fun obtenerModo(): String = if (modoGrados) "Grados" else "Radianes"
    
    private fun gradosARadianes(grados: Double): Double = grados * PI / 180.0
    private fun radianesAGrados(radianes: Double): Double = radianes * 180.0 / PI
    
    fun seno(angulo: Double): Double {
        val radianes = if (modoGrados) gradosARadianes(angulo) else angulo
        return kotlin.math.sin(radianes)
    }
    
    fun coseno(angulo: Double): Double {
        val radianes = if (modoGrados) gradosARadianes(angulo) else angulo
        return kotlin.math.cos(radianes)
    }
    
    @Throws(ArithmeticException::class)
    fun tangente(angulo: Double): Double {
        val radianes = if (modoGrados) gradosARadianes(angulo) else angulo
        if (kotlin.math.cos(radianes) == 0.0) {
            throw ArithmeticException("Error: Tangente indefinida")
        }
        return kotlin.math.tan(radianes)
    }
    
    fun potencia(base: Double, exponente: Double): Double = kotlin.math.pow(base, exponente)
    
    @Throws(ArithmeticException::class)
    fun raizCuadrada(numero: Double): Double {
        if (numero < 0) {
            throw ArithmeticException("Error: Raíz cuadrada de número negativo")
        }
        return kotlin.math.sqrt(numero)
    }
    
    fun raizNesima(numero: Double, indice: Double): Double = kotlin.math.pow(numero, 1.0 / indice)
    
    @Throws(ArithmeticException::class)
    fun logaritmoNatural(numero: Double): Double {
        if (numero <= 0) {
            throw ArithmeticException("Error: Logaritmo de número no positivo")
        }
        return kotlin.math.ln(numero)
    }
    
    @Throws(ArithmeticException::class)
    fun logaritmoBase10(numero: Double): Double {
        if (numero <= 0) {
            throw ArithmeticException("Error: Logaritmo de número no positivo")
        }
        return kotlin.math.log10(numero)
    }
    
    fun exponencial(exponente: Double): Double = kotlin.math.exp(exponente)
    
    @Throws(IllegalArgumentException::class)
    fun factorial(n: Int): Long {
        if (n < 0) {
            throw IllegalArgumentException("Error: Factorial de número negativo")
        }
        if (n == 0 || n == 1) return 1
        var resultado: Long = 1
        for (i in 2..n) {
            resultado *= i
        }
        return resultado
    }
    
    fun decimalABinario(decimal: Int): String = Integer.toBinaryString(decimal)
    
    fun binarioADecimal(binario: String): Int {
        try {
            return Integer.parseInt(binario, 2)
        } catch (e: NumberFormatException) {
            throw IllegalArgumentException("Error: Cadena binaria no válida")
        }
    }
    
    fun sumarBinarios(bin1: String, bin2: String): String {
        val decimal1 = binarioADecimal(bin1)
        val decimal2 = binarioADecimal(bin2)
        return decimalABinario(decimal1 + decimal2)
    }
    
    fun restarBinarios(bin1: String, bin2: String): String {
        val decimal1 = binarioADecimal(bin1)
        val decimal2 = binarioADecimal(bin2)
        return decimalABinario(decimal1 - decimal2)
    }
    
    data class Matriz2x2(val a11: Double, val a12: Double, val a21: Double, val a22: Double)
    
    fun sumarMatrices(m1: Matriz2x2, m2: Matriz2x2): Matriz2x2 {
        return Matriz2x2(
            m1.a11 + m2.a11,
            m1.a12 + m2.a12,
            m1.a21 + m2.a21,
            m1.a22 + m2.a22
        )
    }
    
    fun multiplicarMatrices(m1: Matriz2x2, m2: Matriz2x2): Matriz2x2 {
        return Matriz2x2(
            m1.a11 * m2.a11 + m1.a12 * m2.a21,
            m1.a11 * m2.a12 + m1.a12 * m2.a22,
            m1.a21 * m2.a11 + m1.a22 * m2.a21,
            m1.a21 * m2.a12 + m1.a22 * m2.a22
        )
    }
    
    @Throws(IllegalArgumentException::class)
    fun evaluarExpresion(expresion: String): Double {
        try {
            return when {
                expresion.contains("sin") -> {
                    val valor = expresion.replace("sin", "").replace("(", "").replace(")", "").toDouble()
                    seno(valor)
                }
                expresion.contains("cos") -> {
                    val valor = expresion.replace("cos", "").replace("(", "").replace(")", "").toDouble()
                    coseno(valor)
                }
                expresion.contains("tan") -> {
                    val valor = expresion.replace("tan", "").replace("(", "").replace(")", "").toDouble()
                    tangente(valor)
                }
                expresion.contains("log") -> {
                    val valor = expresion.replace("log", "").replace("(", "").replace(")", "").toDouble()
                    logaritmoBase10(valor)
                }
                expresion.contains("ln") -> {
                    val valor = expresion.replace("ln", "").replace("(", "").replace(")", "").toDouble()
                    logaritmoNatural(valor)
                }
                else -> expresion.toDouble()
            }
        } catch (e: Exception) {
            throw IllegalArgumentException("Error: Expresión no válida: $expresion")
        }
    }
}