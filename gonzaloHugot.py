import streamlit as st
import math

# Título de la aplicación
st.title("Alerta de Navegación")

# Descripción
st.write("Utiliza el slider para seleccionar un número. Calcularemos su cuadrado y su raíz cuadrada.")

# Slider
numero = st.slider("Selecciona un número entre 0 y 100", 0, 100, 0)

# Cálculos
cuadrado = numero ** 2
raiz_cuadrada = math.sqrt(numero)

# Resultados
st.write(f"El número seleccionado es: {numero}")
st.write(f"El cuadrado de {numero} es: {cuadrado}")
st.write(f"La raíz cuadrada de {numero} es: {raiz_cuadrada:.2f}")