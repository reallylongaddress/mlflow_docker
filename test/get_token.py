from google.cloud import iam_credentials
import requests
client = iam_credentials.IAMCredentialsClient()
sa = "mlflow-cli-service-client@lw-airbnb-mlflow.iam.gserviceaccount.com"
client_id = "1067873445055-f5i2f5mis5i9sak637eop1blg81hpe17.apps.googleusercontent.com"
token = client.generate_id_token(
            name=f"projects/-/serviceAccounts/{sa}",
            audience=client_id,
            include_email=True,
).token
print(f'token-->{token}')

api_url = "https://lw-airbnb-mlflow-cloud-run-20221014-6b3rdahrya-uc.a.run.app/api/2.0/mlflow/experiments/list"
api_url = "https://lw-airbnb-mlflow-cloud-run-20221014-6b3rdahrya-uc.a.run.app/api/2.0/mlflow/experiments/list"
# api_url = "https://lw-airbnb-mlflow-cloud-run-20221014-6b3rdahrya-uc.a.run.app/api/2.0/mlflow/experiments/list
result = requests.get(api_url,
                     headers={"Authorization": f"Bearer {token}"})
print(f'-->{result}')
