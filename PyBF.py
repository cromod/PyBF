# -*- coding: utf-8 -*-

import sys

byte_array = [0] # array of bytes
data_ptr = 0 # data pointer

# Increment the byte at the data pointer
def increment_byte():
    byte_array[data_ptr] += 1

# Decrement the byte at the data pointer
def decrement_byte():
    byte_array[data_ptr] -= 1
    if byte_array[data_ptr] < 0:
        raise ValueError("Negative value in array")

# Increment the data pointer
def increment_ptr():
    global data_ptr
    data_ptr += 1
    if data_ptr == len(byte_array):
        byte_array.append(0)

# Decrement the data pointer
def decrement_ptr():
    global data_ptr
    data_ptr -= 1
    if data_ptr < 0:
        raise ValueError("Negative value of pointer")

# Output the byte at the data pointer
def output():
    sys.stdout.write(chr(byte_array[data_ptr]))

# Store one byte of input in the byte at the data pointer
def store():
    byte_array[data_ptr] = ord(sys.stdin.read(1))

# Read instructions except loop
instructions = {
    '+': increment_byte,
    '-': decrement_byte,
    '>': increment_ptr,
    '<': decrement_ptr,
    '.': output,
    ',': store
}
def read_no_loop(char):
    func = instructions[char]
    func()

# Interpret brainfuck code
def interpret(char_chain):
    it = 0
    loop_begin = []
    while it < len(char_chain):
        if char_chain[it] == '[':
            loop_begin.append(it)
        elif char_chain[it] == ']':
            sub_chain = char_chain[loop_begin[-1]+1:it]
            while byte_array[data_ptr] > 0:
                interpret(sub_chain)
            loop_begin.pop()
        else:
            read_no_loop(char_chain[it])
        it += 1

if __name__ == "__main__":
    # Brainfuck program to print "Hello World!"
    cmd = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    try:
        interpret(cmd)
    except:
        raise
