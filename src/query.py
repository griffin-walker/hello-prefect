from sklearn.datasets import make_classification

from prefect import task, context

data_params = {
    "n_samples" : 10000,
    "n_features": 8,
    "n_informative": 4,
    "n_redundant" : 1,
    "n_classes" : 2,
    "class_sep": 0.9
}

def pretend_connection():
    conn = None
    return conn

@task(nout=2)
def get_training_data(conn, data_params=data_params):
    logger = context.get("logger")
    assert not conn
    X, y = make_classification(**data_params)
    logger.info(f"X shape : {X.shape}, y shape : {y.shape}")
    return X, y