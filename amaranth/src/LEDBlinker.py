from amaranth import *
from amaranth.lib import wiring
from amaranth.lib.wiring import In, Out


class LEDBlinker(wiring.Component):

    led: Out(1)

    def elaborate(self, platform):
        print(platform)
        m = Module()
        # led = platform.request("led")
        half_freq = int(platform.default_clk_frequency // 2)
        timer = Signal(range(half_freq + 1))

        with m.If(timer == half_freq):
            m.d.sync += self.led.eq(~self.led)
            m.d.sync += timer.eq(0)

        with m.Else():
            m.d.sync += timer.eq(timer + 1)

        return m
