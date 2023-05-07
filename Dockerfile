# Use uma imagem Ubuntu como base
FROM ubuntu:latest

RUN apt-get update
RUN apt-get clean

RUN apt-get install -y git

# Instale as dependências necessárias para instalar o Miniconda
RUN apt-get install -y wget bzip2 ca-certificates curl libglib2.0-0 libxext6 libsm6 libxrender1

# Baixe o arquivo .sh do Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Instale o Miniconda em /opt/conda
RUN /bin/bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Adicione o diretório bin do Miniconda ao PATH
SHELL ["/bin/bash", "-c"]
ENV PATH="/opt/conda/bin:$PATH"

# Instale as dependências do Graph Tool e Pygame
RUN apt-get install -y libcairo2-dev libgraphicsmagick++-dev libboost-all-dev libxml2-dev libcairomm-1.0-dev 
RUN conda install -y -c conda-forge graph-tool 
RUN conda install -y -c conda-forge pygame
RUN conda install -y numpy

ENV DISPLAY=host.docker.internal:0.0

RUN git clone https://github.com/NathanaelSantos/AI-Maze-Game.git
