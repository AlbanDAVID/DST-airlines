from sqlalchemy import Table, Column, Boolean, Time, DateTime, Integer, String, ForeignKey, MetaData, create_engine, text, inspect
import sqlite3

engine = sqlite3.connect("dst_airlines.db")    
cursor = engine.cursor()

# FONCTION POUR INJECTER DES DONNEES DANS LA TABLE [real_time_flights]


inject_real_time_flights = """ INSERT INTO real_time_flights
                          (flight_number_date, aircraft_icao, 
                          airline_iata, airline_icao, alt, 
                          arr_iata, arr_icao, dep_icao, dir, 
                          date, flag, flight_icao, flight_number, 
                          hex, lat, lng, reg_number, speed, status, 
                          aircraft_hex, dep_iata, arr_iata) 
                        VALUES 
                          ("1", "E195", "LH", 
                          'DLH', 6461, 'MUC', 'EDDM',
                          'LSGG', 64, '04-08-2022', 'DE',
                          'DLH4EF', '4EF', '30055B', 46.596321,
                          6.744095, 'I-ADJS', 751, 'en-route',
                          '3003AE', "EWL", "DEL") """


cursor.execute(inject_real_time_flights)

engine.commit()



# FONCTION POUR INJECTER DES DONNEES DANS LA TABLE [delays_flights]


inject_delays_flights = """ INSERT INTO delays_flights
                          (id_delays, aircraft_icao, 
                          airline_iata, airline_icao, arr_baggage, 
                          arr_estimated, arr_estimated_utc, arr_gate, arr_iata, 
                          arr_icao, arr_terminal, arr_time, arr_time_utc,
                          cs_airline_iata, cs_flight_iata, cs_flight_number,
                          delayed, dep_estimated, 
                          dep_estimated_utc, dep_gate, dep_iata,
                          dep_icao, dep_terminal, dep_time, dep_time_utc,
                          duration, flight_iata, flight_icao, flight_number, 
                          status, flight_number_date, dep_iata, arr_iata) 
                        VALUES 
                          (1, "None", 'LH', 'DLH', 'None',
                          '2022-08-03 21:40', '2022-08-04 01:40',
                          'None', 'YQT', 'CYQT', 'None', 
                          '2022-08-03 20:05', '2022-08-04 00:05',
                          'QK', 'QK8559', 8559, 95, '2022-08-03 19:35', 
                          '2022-08-03 23:35', 'D3', 'YYZ',
                          'CYYZ', '2', '2022-08-03 20:23', '2022-08-04 01:23',
                          108, 'LH7920', 'DLH7920', '7920', 'landed',
                          "1", "EWL", "DEL") """


cursor.execute(inject_delays_flights)

engine.commit()


# FONCTION POUR INJECTER DES DONNEES DANS LA TABLE [aircraft]


inject_aircraft= """ INSERT INTO aircraft
                          (hex, iata, 
                          icao, airline_icao, airline_iata) 
                        VALUES 
                          ('3003AE', "E95", 'E195', 'DLA', 'LH') """


cursor.execute(inject_aircraft)

engine.commit()


# FONCTION POUR INJECTER DES DONNEES DANS LA TABLE [cities]


inject_cities= """ INSERT INTO cities
                          (city_code, country_code, 
                          lat, lng, name, country_code) 
                        VALUES 
                          ('WCC', 'US', 37.25, -119.75, 'California', 'US') """


cursor.execute(inject_cities)

engine.commit()


# FONCTION POUR INJECTER DES DONNEES DANS LA TABLE [countries]


inject_countries = """ INSERT INTO countries
                          (country_code, name) 
                        VALUES 
                          ('AND', 'Andorra') """


cursor.execute(inject_countries)

engine.commit()


# FONCTION POUR INJECTER DES DONNEES DANS LA TABLE [airports]


inject_airports = """ INSERT INTO airports
                          (iata_code, country_code, icao_code, lat, lng, name) 
                        VALUES 
                          ('MIA', 'US', 'KMIA', 25.79, -80.29, 'Miami International Airport') """


cursor.execute(inject_airports)

engine.commit()





