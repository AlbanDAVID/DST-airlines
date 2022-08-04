from sqlalchemy import Table, Column, Boolean, Time, DateTime, Integer, String, ForeignKey, MetaData, create_engine, text, inspect
import sqlite3

engine = sqlite3.connect("dst_airlines.db")   
cursor = engine.cursor()


# queries pour la table real_time_flights
results = cursor.execute("SELECT * FROM real_time_flights;")
print(results.fetchall())


# queries pour la table delays_flights
results = cursor.execute("SELECT * FROM delays_flights;")
print(results.fetchall())


# queries pour la table aircraft
results = cursor.execute("SELECT * FROM aircraft;")
print(results.fetchall())


# queries pour la table cities
results = cursor.execute("SELECT * FROM cities;")
print(results.fetchall())

# queries pour la table countries
results = cursor.execute("SELECT * FROM countries;")
print(results.fetchall())

# queries pour la table airports
results = cursor.execute("SELECT * FROM airports;")
print(results.fetchall())