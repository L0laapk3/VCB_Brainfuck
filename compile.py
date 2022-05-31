import sys

def compile(bf):

	asm = []
	references = []
	for char in bf:
		if char == '>':
			asm.append("0xfe")
		elif char == '<':
			asm.append("0xfd")
		elif char == '+':
			asm.append("0xfb")
		elif char == '-':
			asm.append("0xf7")
		elif char == '.':
			asm.append("0xef")
		elif char == ',':
			asm.append("0xdf")
		elif char == '[':
			references.append(len(asm))
			asm.append("ERROR")
		elif char == ']':
			s = references.pop()
			asm[s] = f"{hex(len(asm) + 2)}bf"
			asm.append(f"{hex(s + 2)}7f")

	asm.append("0xff")
	assert(len(asm) < 2**16)

	return '\n'.join(asm)


if __name__ == '__main__':
	to_file = False
	if len(sys.argv) > 1:
		bf = sys.argv[1]
	else:
		bf_file = input("input file: ")
		with open(bf_file, 'r') as f:
			bf = f.read()
			to_file = True

	asm = compile(bf)

	if to_file:
		with open(bf_file + ".asm", 'w') as f:
			f.write(asm)
	else:
		print(asm)

