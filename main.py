# Import para la Extracción
from extract.news_api import NewsApi

# Import para la Transformación
from transform.news_transform import NewsTransform
from transform.clean_data import DataCleaner

# Import para la Carga(Load)
from load.SQL_Server import connection_to_NewsDB

# Variables de entorno
from utils.config import env_variables

# Top búsquedas en el último mes en Perú
from external.google_trends import load_search_array

if __name__ == '__main__':

    # Conexión a la base de datos NewsDB de SQL Server
    print("Conectando a SQL Server ...")
    engine = connection_to_NewsDB()

    # Carga de búsquedas brindadas por Google Trends
    print("Cargando términos de búsqueda ...")
    queries = load_search_array()

    # Extracción de las noticias con las queries de búsqueda más concurrentes
    print("Extrayendo el archivo JSON de NewsApi ...")
    news_api_extract = NewsApi(env_variables["newsApiKey"], queries)
    news_response = news_api_extract.get_all_articles()

    # Transformación del article response a los dataframes de article, sources, queries y countries
    print("Transformando el response obtenido de NewsApi ...")
    news_transform = NewsTransform(news_response,env_variables["logoBaseUrl"], env_variables["logoApiKey"])
    articles_df, sources_df, queries_df, countries_df = news_transform.transform_articles()

    # Limpieza del Dataframe: article_df
    print("Limpieza de datos ...")
    articles_df = DataCleaner.clean_articles(articles_df)

    # Carga de datos a la base de datos de SQL Server
    print("Cargando datos en SQL Server ...")
    articles_df.to_sql("Articles", engine, if_exists="replace",index=False)
    sources_df.to_sql("Sources", engine, if_exists="replace",index=False)
    queries_df.to_sql("Queries", engine, if_exists="replace",index=False)
    countries_df.to_sql("Countries", engine, if_exists="replace",index=False)

    print("Proceso ETL terminado con éxito")