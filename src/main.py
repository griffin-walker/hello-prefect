from prefect import Flow
from query import get_training_data, pretend_connection

with Flow('example') as flow:
    X_train, y_train = get_training_data(conn = pretend_connection())
    flow.run()