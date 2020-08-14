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


# Make entrypoint.sh
RUN echo '#!/bin/bash -e \n\
\n\
# create group \n\
if [ x"$GROUP_ID" != x"0" ]; then \n\
    groupadd -g $GROUP_ID $USER_NAME \n\
fi \n\
\n\
# create user \n\
if [ x"$USER_ID" != x"0" ]; then \n\
    useradd -d /home/$USER_NAME -m -s /bin/bash -u $USER_ID -g $GROUP_ID $USER_NAME \n\
fi \n\
\n\
su $USER_NAME -c "exec $@" \n\
' > /entrypoint.sh
# exec --- execに指定したコマンドを実行する。このコマンドを実行する際に，新しいプロセスを作成せずに，現在のジョブと置き換えて実行される。
# $@ --- 実行時に与えられたすべての引数. 引数一つ一つが"で囲まれている

RUN chmod a+x /entrypoint.sh 

ENTRYPOINT [ "/entrypoint.sh" ]

# docekr run の実行コマンドで、コマンドを指定することで
# entrypoint.sh内で作成したユーザでログインした状態で、コマンドを実行
