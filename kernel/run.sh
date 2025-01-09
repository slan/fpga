#!/bin/sh

set -xue

CC=/opt/homebrew/opt/llvm/bin/clang
CFLAGS="-std=c11 -O2 -g3 -Wall -Wextra --target=riscv32 -ffreestanding -nostdlib"

#$CC $CFLAGS -Wl,-Tfirmware.ld -Wl,-Map=firmware.map -o firmware.elf firmware.c
# /opt/homebrew/opt/llvm/bin/clang -march=rv32i -Wl,-Tfirmware.ld -Wl,-Map=firmware.map -o firmware.elf firmware.s

# /opt/homebrew/opt/llvm/bin/clang -ffreestanding -nostdlib --target=riscv32 -march=rv32i -Wl,-Tfirmware.ld -Wl,-Map=firmware.map firmware.s

/opt/homebrew/opt/llvm/bin/clang --target=riscv32 -march=rv32i -nostdlib -Wl,-Tfirmware.ld -Wl,-Map=firmware.map firmware.s -o firmware.elf
/opt/homebrew/opt/llvm/bin/llvm-objcopy --output-target binary firmware.elf firmware.bin

qemu-system-riscv32 -machine virt -bios none -nographic -serial mon:stdio --no-reboot -device loader,file=firmware.bin,force-raw=on,addr=0x80000000
# qemu-system-riscv32 -machine virt -bios none -nographic -serial mon:stdio --no-reboot -device loader,file=firmware.elf