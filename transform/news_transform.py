import pandas as pd
import tldextract

# Clase que permitirá transformar el article response en los dataframes necesarios
class NewsTransform:
    def __init__(self, news_response = {}, logo_api_url = "", logo_api_key=""):
        self.news_response = news_response
        self.logo_api_url = logo_api_url
        self.logo_api_key = logo_api_key
    
    # Método que permite obtener la url del logo del medio que publica la noticia
    def get_source_logo_url(self, article_url):
        source_ext = tldextract.extract(article_url)
        source_url = (f"{self.logo_api_url}/{source_ext.domain}.{source_ext.suffix}?token={self.logo_api_key}")
        return source_url
    
    # Método que retorna los dataframes de: article, source, queries y country
    def transform_articles(self):
        articles_list = []
        sources_list = []
        queries_list = []
        country_list = [{"idCountry": "PER", "country": "Peru"}]

        source_map = {}
        source_id_counter = 1

        for q_id, (query, articles) in enumerate(self.news_response.items(), start=1):
            queries_list.append({"idQuery": q_id, 
                                "query": query, 
                                "idCountry": country_list[0]["idCountry"]})

            for art in articles:
                source_name = art["source"]["name"]
                source_logo = self.get_source_logo_url(art["url"])

                if source_name not in source_map:
                        source_map[source_name] = source_id_counter
                        sources_list.append({
                            "idSource": source_id_counter,
                            "source": source_name,
                            "logo": source_logo
                        })
                        source_id_counter += 1

                articles_list.append({
                    "idArticle": len(articles_list) + 1,
                    "idSource": source_map[source_name],
                    "idQuery": q_id,
                    "title": art["title"],
                    "author": art["author"],
                    "description": art["description"],
                    "url": art["url"],
                    "publishedAt": art["publishedAt"],
                    "articleContent": art["content"]
                })

        return (
            pd.DataFrame(articles_list),
            pd.DataFrame(sources_list),
            pd.DataFrame(queries_list),
            pd.DataFrame(country_list)
        )

    
        
