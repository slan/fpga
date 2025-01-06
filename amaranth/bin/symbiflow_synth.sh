#!
docker run --rm -it -w /build --mount type=bind,src=/h/src/fpga/amaranth/src/build,dst=/build f4pga /opt/f4pga/xc7/conda/envs/xc7/bin/symbiflow_synth $@