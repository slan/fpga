FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

#WORKDIR /amaranth
#RUN pip3 install 'amaranth[builtin-yosys] @ git+https://github.com/amaranth-lang/amaranth.git'
RUN pip3 install 'amaranth-boards @ git+https://github.com/amaranth-lang/amaranth-boards.git'
USER vscode
WORKDIR /home/vscode
RUN git clone https://github.com/amaranth-lang/amaranth
WORKDIR /home/vscode/amaranth
RUN pip3 install --user --editable '.[builtin-yosys]'
