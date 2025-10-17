open class Calculadora {
    protected var memoria: Double = 0.0
    protected var resultadoActual: Double = 0.0
    
    open fun sumar(a: Double, b: Double): Double = a + b
    open fun sumar(a: Int, b: Int): Int = a + b
    open fun sumar(a: Float, b: Float): Float = a + b
    
    open fun restar(a: Double, b: Double): Double = a - b
    open fun restar(a: Int, b: Int): Int = a - b
    open fun restar(a: Float, b: Float): Float = a - b
    
    open fun multiplicar(a: Double, b: Double): Double = a * b
    open fun multiplicar(a: Int, b: Int): Int = a * b
    open fun multiplicar(a: Float, b: Float): Float = a * b
    
    @Throws(ArithmeticException::class)
    open fun dividir(a: Double, b: Double): Double {
        if (b == 0.0) {
            throw ArithmeticException("Error: División por cero")
        }
        return a / b
    }
    
    @Throws(ArithmeticException::class)
    open fun dividir(a: Int, b: Int): Int {
        if (b == 0) {
            throw ArithmeticException("Error: División por cero")
        }
        return a / b
    }
    
    open fun memoriaSumar(valor: Double) {
        memoria += valor
    }
    
    open fun memoriaRestar(valor: Double) {
        memoria -= valor
    }
    
    open fun memoriaLimpiar() {
        memoria = 0.0
    }
    
    open fun memoriaObtener(): Double = memoria
    
    open fun memoriaGuardar(valor: Double) {
        memoria = valor
    }
    
    open fun obtenerResultado(): Double = resultadoActual
    open fun establecerResultado(valor: Double) {
        resultadoActual = valor
    }
}