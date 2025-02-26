import pandas as pd

# Crear la serie correctamente
good_student_qualities = pd.Series([
    'Self-Discipline', 'Self-discipline', 'Goal-Oriented', 'Punctuality',
    'Diligence and Hard Work', 'Respectful', 'Password'
])

print(good_student_qualities)

# El tamaño de la serie
print(f'El tamaño de la serie es el siguiente: {good_student_qualities.size}')

# La serie tiene valores duplicados
print(f'La serie tiene valores duplicados: {not good_student_qualities.is_unique}')

# Información de los índices
print(f'Este atributo muestra información de los índices: {good_student_qualities.index}')

# Información del almacenamiento de los valores de la serie
print(f'Información de los valores de la serie: {good_student_qualities.values}')

# Información del tipo de datos que se utilizan para almacenar los valores de la serie
print(f'Tipo de datos: {good_student_qualities.dtype}')
