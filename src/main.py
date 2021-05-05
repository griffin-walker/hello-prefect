from prefect import Flow
from prefect.executors import LocalDaskExecutor
from query import get_initial_data, get_secondary_data, get_tertiary_data, pretend_connection

with Flow('example') as flow:
    flow.executor = LocalDaskExecutor()
    conn = pretend_connection()
    X_initial, y_initial = get_initial_data(conn)
    X_secondary, y_secondary = get_secondary_data(conn)
    X_tertiary, y_tertiary = get_tertiary_data(conn)
    flow.run()