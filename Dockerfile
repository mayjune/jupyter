
FROM continuumio/anaconda3
RUN pip install --upgrade pip
RUN pip install jupyter_contrib_nbextensions
RUN pip install ipywidgets
RUN pip install qgrid

RUN jupyter contrib nbextension install --user
WORKDIR /jupyter
