import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1234@localhost:5432/crud_python')

connection = pg.connect(user = "postgres", password = "1234", host = "localhost", port="5432", database = "crud_python")
curs = connection.cursor()