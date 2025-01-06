FROM ubuntu:22.04 AS stage

ENV F4PGA_INSTALL_DIR=/opt/f4pga
ENV FPGA_FAM=xc7

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git \
    wget \
    xz-utils \
    && rm -rf /var/lib/apt/lists/*

    
WORKDIR /src
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O conda_installer.sh

RUN bash conda_installer.sh -u -b -p $F4PGA_INSTALL_DIR/$FPGA_FAM/conda;

RUN git clone https://github.com/chipsalliance/f4pga-examples
WORKDIR /src/f4pga-examples
RUN bash -c "source $F4PGA_INSTALL_DIR/$FPGA_FAM/conda/etc/profile.d/conda.sh && conda env create -f $FPGA_FAM/environment.yml"

WORKDIR /src
COPY download_packages.sh .
RUN bash download_packages.sh

FROM ubuntu:22.04
COPY --from=stage /opt /opt
COPY --from=stage /src /src
COPY entrypoint.sh /

ENV F4PGA_INSTALL_DIR=/opt/f4pga
ENV FPGA_FAM=xc7

RUN bash -c "source $F4PGA_INSTALL_DIR/$FPGA_FAM/conda/etc/profile.d/conda.sh && conda init"

ENTRYPOINT [ "/entrypoint.sh" ]
