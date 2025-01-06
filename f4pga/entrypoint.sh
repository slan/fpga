#!/bin/bash
echo Hello
source $F4PGA_INSTALL_DIR/$FPGA_FAM/conda/etc/profile.d/conda.sh
exec conda run --no-capture-output -n $FPGA_FAM "$@"