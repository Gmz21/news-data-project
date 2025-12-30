from sqlalchemy import create_engine
import urllib
from utils.config import env_variables

# Función que conecta con la base de datos NewsDB
# Conexión realizada con SQL Server
def connection_to_NewsDB():
    server = env_variables["SQL_SERVER_HOST"]
    database = env_variables["SQL_SERVER_DB"]
    driver = env_variables["SQL_SERVER_DRIVER"]
    trusted = env_variables["SQL_SERVER_TRUSTED"]

    params = urllib.parse.quote_plus(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection={trusted};"
        "Encrypt=no;"
    )

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    return engine