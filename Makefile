
DOCKER_BUILD_VERSION=0.48

GCP_PROJECT_ID=lw-airbnb-mlflow
DOCKER_IMAGE_NAME=lw_airbnb_mlflow_20221014
DOCKER_REPO_URL=gcr.io

docker_build:
#copy the model before docker-compose because Docker can not go 'up' directories easily to copy files
	@docker build -t ${DOCKER_IMAGE_NAME} .

docker_tag:
	docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_REPO_URL}/${GCP_PROJECT_ID}/${DOCKER_IMAGE_NAME}:${DOCKER_BUILD_VERSION}

docker_run:
	@docker run -p 8080:8080 ${DOCKER_IMAGE_NAME}

docker_run_i:
	@docker run -it ${DOCKER_IMAGE_NAME} sh

# docker_build_gcp_local:
# @docker buildx build --platform linux/amd64 -t ${DOCKER_REPO_URL}/${GCP_PROJECT}/${IMAGE_NAME} .

#upload image info and build on GCloud
docker_build_gcp_in_cloud:
	@gcloud builds submit -t ${DOCKER_REPO_URL}/${GCP_PROJECT_ID}/${DOCKER_IMAGE_NAME}:${DOCKER_BUILD_VERSION} .

#have to run docker_build_gcp_in_cloud first (or docker_build_gcp_local and upload)
run_gcp:
	gcloud run deploy --image ${DOCKER_REPO_URL}/${GCP_PROJECT_ID}/${DOCKER_IMAGE_NAME} --platform managed --region us-central-1



push:
        docker push "${DOCKER_REPO_URL}/${GCP_PROJECT}/${IMAGE_NAME}:${DOCKER_BUILD_VERSION}"

run_gcp:
        gcloud run deploy --image ${DOCKER_REPO_URL}/${GCP_PROJECT}/${IMAGE_NAME}:${DOCKER_BUILD_VERSION} --platform managed --region us-central1





# # ----------------------------------
# #          INSTALL & TEST
# # ----------------------------------
# install_requirements:
# 	@pip install -r requirements.txt

# check_code:
# 	@flake8 scripts/* mlflow/*.py

# black:
# 	@black scripts/* mlflow/*.py

# test:
# 	@coverage run -m pytest tests/*.py
# 	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

# ftest:
# 	@Write me

# clean:
# 	@rm -f */version.txt
# 	@rm -f .coverage
# 	@rm -fr */__pycache__ */*.pyc __pycache__
# 	@rm -fr build dist
# 	@rm -fr mlflow-*.dist-info
# 	@rm -fr mlflow.egg-info

# install:
# 	@pip install . -U

# all: clean install test black check_code

# count_lines:
# 	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
#         '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
# 	@echo ''
# 	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
# 		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
# 	@echo ''
# 	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
#         '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
# 	@echo ''

# # ----------------------------------
# #      UPLOAD PACKAGE TO PYPI
# # ----------------------------------
# PYPI_USERNAME=<AUTHOR>
# build:
# 	@python setup.py sdist bdist_wheel

# pypi_test:
# 	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

# pypi:
# 	@twine upload dist/* -u $(PYPI_USERNAME)
