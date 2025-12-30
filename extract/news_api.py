from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException

# Clase para la extracción 2 páginas del json de las noticias con sus
# respectivos parámetros de búsqueda y lenguage
# Inlcuye manejo de errores

class NewsApi:

    def __init__(self, api_key = "", arr_q = []):
        self.news_client = NewsApiClient(api_key)
        self.search_array = arr_q
    
    # Método que retornará el Article Response
    def get_all_articles(self, pages=2):
        try:
            search_result_dict = {}
            for search in self.search_array:
                all_articles = []
                for page in range(1,pages + 1):
                    response = self.news_client.get_everything(q=search, 
                                                               language='es', 
                                                               sort_by='relevancy', 
                                                               page=page)
                    all_articles.extend(response['articles'])
                search_result_dict[search] = all_articles
            return search_result_dict

        except NewsAPIException as e:
            print(f"Error de NewsAPI: {e}")
            print(search_result_dict)
        except Exception as e:
            print(f"Error inesperado: {e}")
            print(search_result_dict)
