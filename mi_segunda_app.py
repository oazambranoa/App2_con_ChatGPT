import streamlit as st

# Título y autor
st.title("Conversor de Unidades")
st.write("Autor: Esta app fue elaborada por Omar Zambrano")

# Conversiones de temperatura
st.header("Conversiones de temperatura")

# Celsius a Fahrenheit
celsius = st.number_input("Grados Celsius", value=0.0)
fahrenheit = (celsius * 9/5) + 32
st.write(f"{celsius} °C son equivalentes a {fahrenheit:.2f} °F")

# Fahrenheit a Celsius
fahrenheit = st.number_input("Grados Fahrenheit", value=32.0)
celsius = (fahrenheit - 32) * 5/9
st.write(f"{fahrenheit} °F son equivalentes a {celsius:.2f} °C")

# Celsius a Kelvin
celsius = st.number_input("Grados Celsius", value=0.0)
kelvin = celsius + 273.15
st.write(f"{celsius} °C son equivalentes a {kelvin:.2f} K")

# Kelvin a Celsius
kelvin = st.number_input("Kelvin", value=273.15)
celsius = kelvin - 273.15
st.write(f"{kelvin} K son equivalentes a {celsius:.2f} °C")
