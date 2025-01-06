from UpCounter import UpCounter
from amaranth.sim import Simulator, Period

dut = UpCounter(25)

async def bench(ctx):
    # Disabled counter should not overflow.
    ctx.set(dut.en, 0)
    for _ in range(30):
        await ctx.tick()
        assert not ctx.get(dut.ovf)

    # Once enabled, the counter should overflow in 25 cycles.
    ctx.set(dut.en, 1)
    for _ in range(24):
        await ctx.tick()
        assert not ctx.get(dut.ovf)

    await ctx.tick()
    assert ctx.get(dut.ovf)

    # The overflow should clear in one cycle.

    await ctx.tick()
    assert not ctx.get(dut.ovf)

sim = Simulator(dut)
sim.add_clock(Period(MHz=1))
sim.add_testbench(bench)

with sim.write_vcd("up_counter.vcd"):
    sim.run()
