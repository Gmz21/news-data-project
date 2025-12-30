import pandas as pd

# Clase para limpiar los datos del Dataframe articles_df
class DataCleaner:
    @staticmethod
    def clean_articles(df: pd.DataFrame) -> pd.DataFrame:
        # Eliminar duplicados por título y fuente
        df = df.drop_duplicates(subset=["title", "idSource"])
        
        # Eliminar filas sin título o descripción
        df = df.dropna(subset=["title", "description"])
        
        # Formatear el título
        df["title"] = df["title"].str.strip().str.title()
        
        return df
