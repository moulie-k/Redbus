import pandas as pd
import pymysql
from sqlalchemy import create_engine
 
host = "localhost"
port = "3306"
username = "root"
password = "99946%40abd"
database = "redbus"
 
engine_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(engine_string)
 
table_name = "bus_details2"
df = pd.read_csv('kerala.csv')
df.to_sql(table_name, engine,if_exists="replace", index=False)
print("success")
