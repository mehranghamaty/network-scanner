FROM continuumio/miniconda3

ENV APP_PATH /APP_PATH
WORKDIR ${APP_PATH}
COPY . $APP_PATH

RUN conda update --name base conda 
RUN conda env create --file environment.yaml
#RUN conda activate network-scanner

SHELL ["conda", "run", "--name", "network-scanner", "/bin/bash", "-c"]

ENTRYPOINT [ "conda", "run", "--name", "network-scanner", "python", "main.py" ]