# 🏗️ Binary Build System
# The Most Low-Level Build Process!

all: abyss-binary abyss-hex

abyss-binary: abyss.asm
	@echo "🔮 Compiling quantum assembly..."
	nasm -f elf32 abyss.asm -o abyss.o
	ld -m elf_i386 abyss.o -o abyss-binary
	@echo "🎉 Pure binary executable created!"

abyss-hex: abyss.bin
	@echo "🔢 Generating hex machine code..."
	xxd abyss.bin > abyss.hex
	@echo "🎉 Hex dump created!"

clean:
	rm -f abyss.o abyss-binary abyss.hex
	@echo "🧹 Binary artifacts cleaned!"

quantum: all
	@echo "🌌 Executing quantum binary..."
	./abyss-binary

.PHONY: all clean quantum
