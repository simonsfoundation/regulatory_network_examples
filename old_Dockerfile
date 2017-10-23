FROM andrewosh/binder-base

MAINTAINER Aaron Watters <awatters@simonsfoundation.org>

USER main

# see https://github.com/aadm/avo_explorer/blob/master/Dockerfile


RUN mkdir $HOME/.jupyter
RUN echo "c.NotebookApp.token = ''" >> $HOME/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.password=''" >> $HOME/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.password_required=False" >> $HOME/.jupyter/jupyter_notebook_config.py

RUN git clone https://github.com/simonsfoundation/regulatory_network_examples.git repo
RUN cd repo; pip install -r requirements.txt
# RUN cd repo; python setup.py install
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension