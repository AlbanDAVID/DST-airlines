from sqlalchemy import Table, Column, Boolean, Time, DateTime, Integer, Float, String, ForeignKey, MetaData, create_engine, text, inspect

# CREATION BDD SQL :
engine = create_engine('sqlite:///dst_airlines.db', echo=True)
meta = MetaData()

# CREATION DES TABLES : 


# TABLE [airports]

airports = Table(
    'airports', meta,
    Column('iata_code', String, primary_key=True),
    Column('country_code', String),
    Column('icao_code', String),
    Column('lat', Float),
    Column('lng', Float),
    Column('name', String)

)
meta.create_all(engine)

# TABLE [countries]

countries = Table(
    'countries', meta,
    Column('country_code', String, primary_key=True),
    Column('name', String)

)
meta.create_all(engine)


# TABLE [cities]

cities = Table(
    'cities', meta,
    Column('city_code', String, primary_key=True),
    Column('country_code', String),
    Column('lat', Float),
    Column('lng', Float),
    Column('name', String),
    Column('country_code', String, ForeignKey("countries.country_code"))

)
meta.create_all(engine)


# TABLE [aircraft]

aircraft = Table(
    'aircraft', meta,
    Column('hex', String, primary_key=True),
    Column('iata', String),
    Column('icao', String),
    Column('airline_icao', String),
    Column('airline_iata', String)

)
meta.create_all(engine)


# TABLE [real_time_flights]

real_time_flights = Table(
    'real_time_flights', meta,
    Column('flight_number_date', String, primary_key=True),
    Column('aircraft_icao', String),
    Column('airline_iata', String),
    Column('airline_icao', String),
    Column('alt', Integer),
    Column('arr_iata', String),
    Column('arr_icao', String),
    Column('dep_icao', String),
    Column('dir', Integer),
    Column('date', String),
    Column('flag', String),
    Column('flight_icao', String),
    Column('flight_number', String),
    Column('hex', String),
    Column('lat', Float),
    Column('lng', Float),
    Column('reg_number', String),
    Column('speed', Integer),
    Column('status', String),
    Column('aircraft_hex', String, ForeignKey("aircraft.hex")),
    Column('dep_iata', String, ForeignKey("airports.iata_code")),
    Column('arr_iata', String, ForeignKey("airports.iata_code"))

)
meta.create_all(engine)




# TABLE [delays_flights]

delays_flights = Table(
    'delays_flights', meta,
    Column('id_delays', Integer, primary_key=True),
    Column('aircraft_icao', String),
    Column('airline_iata', String),
    Column('airline_icao', String),
    Column('arr_baggage', String),
    Column('arr_estimated', String),
    Column('arr_estimated_utc', String),
    Column('arr_gate', String),
    Column('arr_iata', String),
    Column('arr_icao', String),
    Column('arr_terminal', String),
    Column('arr_time', String),
    Column('arr_time_utc', String),
    Column('cs_airline_iata', String),
    Column('cs_flight_iata', String),
    Column('cs_flight_number', Integer),
    Column('delayed', Integer),
    Column('dep_estimated', String),
    Column('dep_estimated_utc', String),
    Column('dep_gate', String),
    Column('dep_iata', String),
    Column('dep_icao', String),
    Column('dep_terminal', String),
    Column('dep_time', String),
    Column('dep_time_utc', String),
    Column('duration', Integer),
    Column('flight_iata', String),
    Column('flight_icao', String),
    Column('flight_number', String),
    Column('status', String),
    Column('flight_number_date', String, ForeignKey("real_time_flights.flight_number_date")),
    Column('dep_iata', String, ForeignKey("airports.iata_code")),
    Column('arr_iata', String, ForeignKey("airports.iata_code"))
)
meta.create_all(engine)



# TABLE [test]

test = Table(
    'test', meta,
    Column('airline_iata', String, primary_key=True),
    Column('alt', Integer),
    Column('status', String)

)
meta.create_all(engine)
