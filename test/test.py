import time
import platform
import shortuuid

import numpy as np

import mlflow
import mlflow.sklearn
from mlflow.entities import Param, Metric, RunTag
from mlflow.models.signature import infer_signature

import sklearn
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

TRACKING_URI = f"https://lw-airbnb-mlflow-cloud-run-20221014-6b3rdahrya-uc.a.run.app/"

# YOUR EXPERIMENT NAME,
# EX: 'CNN_transfer_learning'
EXPERIMENT_NAME_1 = "initial_experiments_1"
EXPERIMENT_NAME_2 = "initial_experiments_2"
EXPERIMENT_NAME_3 = "initial_experiments_3"

mlflow.tracking.set_tracking_uri(TRACKING_URI)
mlflow.set_experiment(EXPERIMENT_NAME_1)

#simple example logging param and metric
with mlflow.start_run():
    mlflow.log_param("alpha", .1)
    mlflow.log_metric("rmse", .3)


#more complex example with
# param, metric & tags
# Artifact upload (images, text files, other relevant 'files')
mlflow.set_experiment(EXPERIMENT_NAME_2)
with mlflow.start_run(run_name='dbd run name 2') as run:
    print("runId:", run.info.run_uuid)

    mlflow.log_param("alpha", .1)
    mlflow.log_metric("rmse", 0.789)

    now = round(time.time())
    metrics = [ Metric("m1",0.1,now,0), Metric("m2",0.2,now,0) ]
    params = [ Param("p1","0.1"), Param("p2","0.2") ]
    tags = [ RunTag("t1","hi1"), RunTag("t2","hi2") ]

    with open("info.txt", "w") as f:
        f.write("Hi artifact")
    mlflow.log_artifact("info.txt")
    print("artifact_uri:", mlflow.get_artifact_uri())

    mlflow.tracking.MlflowClient().log_batch(run.info.run_uuid, metrics, params, tags)

# ----------------------------
# most complex example with
# param, metric & tags
# Model upload (SAVE YOUR MODELS, DON'T LOOSE THE BEST!)
start = round(time.time(),0)
run_name = f'run_name_{start}'
model_name = f'model_name_{start}'

mlflow.set_experiment(EXPERIMENT_NAME_3)
client = mlflow.tracking.MlflowClient()
with mlflow.start_run(run_name=run_name) as run:

    run_id = run.info.run_id
    experiment_id = run.info.experiment_id
    print("MLflow:")
    print("  run_id:", run_id)
    print("  runId:", run.info.run_uuid)
    print("  experiment_id:", experiment_id)
    client.set_experiment_tag(experiment_id,"version_mlflow",mlflow.__version__)
    print("  experiment_name:", client.get_experiment(experiment_id).name)

    # MLflow tags
    mlflow.set_tag("run_name", run_name)
    mlflow.set_tag("version.mlflow", mlflow.__version__)
    mlflow.set_tag("version.sklearn", sklearn.__version__)
    mlflow.set_tag("version.platform", platform.platform())
    mlflow.set_tag("version.python", platform.python_version())
    mlflow.set_tag("model_name",model_name)
    mlflow.set_tag("uuid",shortuuid.uuid())

    mlflow.log_param("alpha", .1)
    mlflow.log_metric("rmse", 0.789)

    X_train = np.array([1.0, 2.0, 3.0, 4.0])
    y_train = np.array([2.0, 3.0, 5.0, 10.0])

    X_test = np.array([1.1, 2.2, 3.9, 4.5])
    y_test = np.array([2.0, 3.1, 6.2, 11.0])

    dummy_model = DummyRegressor(strategy="mean")
    dummy_model.fit(X_train, y_train)
    predictions = dummy_model.predict(X_test)
    score = dummy_model.score(X_test, y_test)

    signature = infer_signature(X_train, predictions)
    print("signature:",signature)

    # MLflow params
    mlflow.log_param("param_1", 1.2)
    mlflow.log_param("param_2", 2.4)

    # MLflow metrics
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print("Metrics:")
    print("  rmse:", rmse)
    print("  mae:", mae)
    print("  r2:", r2)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)
    mlflow.log_metric("mae", mae)

    # MLflow log model
    mlflow.sklearn.log_model(dummy_model, "model", registered_model_name=model_name, signature=signature)
