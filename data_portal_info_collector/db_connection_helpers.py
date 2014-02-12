import psycopg2
import os
import urlparse

def get_db_connection():
  urlparse.uses_netloc.append("postgres")
  local_url = "postgres://data-portal-info-collector@localhost:5432/data-portal-info-collector-database"
  url = urlparse.urlparse(os.environ.get("DATABASE_URL", local_url))
  conn = psycopg2.connect(database=url.path[1:], user=url.username, password=url.password,
                          host=url.hostname, port=url.port)
  return conn