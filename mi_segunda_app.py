import streamlit as st

# Título y autor
st.title("Conversor de Unidades")
st.write("Autor: Esta app fue elaborada por Omar Zambrano")

# Conversiones de temperatura
st.header("Conversiones de temperatura")

# Celsius a Fahrenheit
celsius_to_fahrenheit = st.number_input("Grados Celsius a Fahrenheit", key="c_to_f", value=0.0)
fahrenheit_to_celsius = st.number_input("Grados Fahrenheit a Celsius", key="f_to_c", value=32.0)
celsius_to_kelvin = st.number_input("Grados Celsius a Kelvin", key="c_to_k", value=0.0)
kelvin_to_celsius = st.number_input("Kelvin a Celsius", key="k_to_c", value=273.15)

# Realizar conversiones
fahrenheit_converted = (celsius_to_fahrenheit * 9/5) + 32
celsius_converted = (fahrenheit_to_celsius - 32) * 5/9
kelvin_converted = celsius_to_kelvin + 273.15
celsius_k_converted = kelvin_to_celsius - 273.15

# Mostrar resultados
st.write(f"{celsius_to_fahrenheit} °C son equivalentes a {fahrenheit_converted:.2f} °F")
st.write(f"{fahrenheit_to_celsius} °F son equivalentes a {celsius_converted:.2f} °C")
st.write(f"{celsius_to_kelvin} °C son equivalentes a {kelvin_converted:.2f} K")
st.write(f"{kelvin_to_celsius} K son equivalentes a {celsius_k_converted:.2f} °C")
