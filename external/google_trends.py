import os

# Creando la función exportable para obtener el arreglo de 
# las búsquedas de noticias más realizadas en Perú los últimos 30 días.
# Fuente: Google Trends

def load_search_array():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'final/relatedQueries.csv')

    with open(file_path,'r',encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    top_index = lines.index('TOP') + 1
    rising_index = lines.index('RISING')

    top_lines = lines[top_index:rising_index]
    rising_lines = lines[rising_index + 1:]
    
    search_array = top_lines + rising_lines
    search_array = [e.split(",")[0] for e in search_array]

    return search_array


