import os
from amaranth.back import verilog
from LEDBlinker import LEDBlinker
from amaranth_boards.arty_a7 import ArtyA7_35Platform

top = LEDBlinker()

os.environ['SYMBIFLOW_SYNTH'] = '/workspaces/fpga/amaranth/bin/symbiflow_synth.sh'
os.environ['SYMBIFLOW_PACK'] = '/bin/false'
os.environ['SYMBIFLOW_PLACE'] = '/bin/false'
os.environ['SYMBIFLOW_ROUTE'] = '/bin/false'
os.environ['SYMBIFLOW_WRITE_FASM'] = '/bin/false'
os.environ['SYMBIFLOW_WRITE_BITSTREAM'] = '/bin/false'

ArtyA7_35Platform(toolchain="Symbiflow").build(top)

# with open("led_blinker.v", "w") as f:
#     f.write(verilog.convert(top))
