import datetime
import streamlit as st


# Obtener la fecha de hoy
today = datetime.date.today()
# print("La fecha de hoy es:", today)
#2025-09-30

#st_input para hacer stream en la web

bornyear = st.text_input('Añade tu fecha de nacimiento (dd/mm/aa): ')
#if len(bornyear) < 1: 
#    bornyear = '31/10/2001'

date = bornyear.split('/')

try:
    day = date[0]
    month = date[1]
    year = date[2]
    
    day = int(day)
    month = int(month)
    year = int(year)
    
except:
    print('Formato no soportado')
    quit()

name = st.text_input('Añade tu nombre: ')
#if len(name) < 1: 
#    name = 'Gil'


age = today.year - year

if month > today.month:
    age = age - 1

elif month == today.month:
    if day > today.day:
        age = age - 1
    

#st.write es como print()

st.write('Hola', name, 'tienes', age, 'años')

#streamlit run tu_programa.py