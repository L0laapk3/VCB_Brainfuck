import sys


def compile(bf):
	references = []
	chars = list(bf)
	for i in range(len(chars)):
		char = chars[i]
		if char == '>':
			chars[i] = "0xfe"
		elif char == '<':
			chars[i] = "0xfd"
		elif char == '+':
			chars[i] = "0xfb"
		elif char == '-':
			chars[i] = "0xf7"
		elif char == '.':
			chars[i] = "0xef"
		elif char == ',':
			chars[i] = "0xdf"
		elif char == '[':
			chars[i] = "ERROR"
			references.append(i)
		elif char == ']':
			s = references.pop()
			chars[s] = f"{hex(i + 2)}bf"
			chars[i] = f"{hex(s + 2)}7f"

	chars.append("0xff")
	return '\n'.join(chars)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		bf = sys.argv[1]
	else:
		bf = input("Enter your brainfuck code: ")

	asm = compile(bf)

	print(asm)

