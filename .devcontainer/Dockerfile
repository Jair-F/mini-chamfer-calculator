FROM ubuntu:22.04

RUN apt update && apt upgrade -y

# dev container settings
RUN apt install -y git vim bash-completion fish curl wget iproute2 python3 python3-pip python3-pyqt5

USER root
RUN cp -R /etc/skel/.* /root/ ; echo " "
# RUN usermod -s /bin/fish root

#WORKDIR /workspaces

ENTRYPOINT [ "/bin/bash", "" ]
