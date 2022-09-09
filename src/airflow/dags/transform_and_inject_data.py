import get_rt_data
import get_aircrafts_preprocessed
import get_flights_preprocessed
import inject_sql_flights_metrics
import inject_sql_flights_summary
import inject_sql_aircrafts

def launch_etl():
    json_flights = get_rt_data.get_rt_flights()
    api_flights_df = get_rt_data.get_dataframe_flights(json_flights)
    list_missing_air2 = get_rt_data.get_missing_airports(api_flights_df)
    api_fleets_response2 = get_rt_data.get_missing_aircraft(api_flights_df)
    df_flights = get_flights_preprocessed.get_flights_preprocessed()
    if api_fleets_response2 != None:
        AIRCRAFT = get_aircrafts_preprocessed.get_aircrafts_preprocessed()
        inject_sql_aircrafts.inject_AIRCRAFT(AIRCRAFT, 'airlines5')
        
    FLIGHTS_SUMMARY = df_flights[['hex','flight_icao','flight_iata','status','status_lufthansa','flag','dep_iata','arr_iata','schedule_date_deps','schedule_date_arrs',
                                    'schedule_time_deps','schedule_time_arrs','actual_date_deps','actual_date_arrs','actual_time_deps','actual_time_arrs','terminal_names_dep','gates_dep',
                                    'terminal_names_arr','gates_arr','date_retrieve','time_retrieve']]
    inject_sql_flights_summary.inject_sql_flights_summary(FLIGHTS_SUMMARY, 'airlines5')
    FLIGHTS_METRICS = df_flights[['hex','flight_icao','flight_iata','lat','lng','alt','dir','speed','date_retrieve','time_retrieve']]
    FLIGHTS_METRICS['v_speed'] = -1
    inject_sql_flights_metrics.inject_sql_flights_metrics(FLIGHTS_METRICS, 'airlines5')
    message_end = "Process tranform and inject data finished"

    return message_end


    