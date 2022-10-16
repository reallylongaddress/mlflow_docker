from pathlib import Path

import mlflow
# import mlflow_config
import os




PROJECT_ID = "lw-airbnb-mlflow"
EXPERIMENT_NAME = "DBD: Experiement 1"
# mlflow.setgcloud auth print-identity-token --impersonate-service-account="<service account email>"

# If mlflow if not deployed on the default app engine service, change it with the url of your service <!-- omit in toc -->
# tracking_uri = f"https://mlflow-dot-{PROJECT_ID}.ew.r.appspot.com"
# tracking_uri = f"https://lw-airbnb-mlflow-cloud-run-20221014-6b3rdahrya-uc.a.run.app:4180"
tracking_uri = f"https://lw-airbnb-mlflow-cloud-run-20221014-6b3rdahrya-uc.a.run.app/"

# mlflow.set_tracking_uri(tracking_uri)
print("MLflow Version:", mlflow.__version__)
mlflow.tracking.set_tracking_uri(tracking_uri)
print("~~Tracking URI:", mlflow.tracking.get_tracking_uri())
print(f'1')
with mlflow.start_run():
    print(f'2')
    mlflow.log_param("alpha", 1)
    mlflow.log_param("l1_ratio", 2)
    mlflow.log_metric("rmse", 3)
    mlflow.log_metric("r2", 4)
    mlflow.log_metric("mae", 5)
    print(f'3')
print(f'4')
    # tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
print('done')
