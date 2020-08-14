#Install base image
ARG cuda_version=10.1
ARG cudnn_version=7
ARG ubuntu_version=18.04
#FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04
FROM nvidia/cuda:${cuda_version}-cudnn${cudnn_version}-devel-ubuntu${ubuntu_version}


#Install apt package && reduce image size
#Install on noninteracticve mode
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3-dev \
      python3-pip \
      libopencv-dev && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*


# Upgrade pip and setuptools
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade setuptools
# pip install
RUN pip install --no-cache-dir \
    numpy \
    tensorflow \
    opencv-python

#################################################
# README #
#################################################
#entrypointないバージョン（あるのは、keras-tf22-v1/Dockerfile）

#実行ユーザ指定する場合は、run時に-uオプションでuid, gid指定
#その際、ユーザ名は命名されずno name状態となる。ことに注意

