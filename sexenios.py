# Importar las librerias
from sqlalchemy import Column, Date, Float, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd

# Informacion de la conexión a la base de datos de postgreSQL
USER = "examen"
PASSWORD = "12345"
HOST = "localhost"
PORT = "5432"
DB_NAME = "paloma"

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

# Declarar la base para los modelos
Base = declarative_base()


#  Definir la clase (tabla 'sexenio1')
class Sexenio1(Base):
    __tablename__ = "sexenio1"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    cotizacion = Column(Float)


#  Definir la clase (tabla 'sexenio2')
class Sexenio2(Base):
    __tablename__ = "sexenio2"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    cotizacion = Column(Float)


# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

#  Crear una sesión para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Consultas (sin filtro de fechas: toda la tabla)
mi_query1 = session.query(Sexenio1)
df1 = pd.read_sql(mi_query1.statement, session.bind)

mi_query2 = session.query(Sexenio2)
df2 = pd.read_sql(mi_query2.statement, session.bind)

# Cerrar sesión
session.close()

# ---------- SEXENIO 1 ----------
media = df1['cotizacion'].astype(float).mean()
varianza = df1['cotizacion'].astype(float).var()
desviacion_estandar = df1['cotizacion'].astype(float).std()
minimo = df1['cotizacion'].astype(float).min()
maximo = df1['cotizacion'].astype(float).max()
rango = maximo - minimo

print("Sexenio 1")
print("Media:", media)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion_estandar)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Rango:", rango)

# ---------- SEXENIO 2 ----------
media2 = df2['cotizacion'].astype(float).mean()
varianza2 = df2['cotizacion'].astype(float).var()
desviacion_estandar2 = df2['cotizacion'].astype(float).std()
minimo2 = df2['cotizacion'].astype(float).min()
maximo2 = df2['cotizacion'].astype(float).max()
rango2 = maximo2 - minimo2

print("\nSexenio 2")
print("Media:", media2)
print("Varianza:", varianza2)
print("Desviación estándar:", desviacion_estandar2)
print("Mínimo:", minimo2)
print("Máximo:", maximo2)
print("Rango:", rango2)
