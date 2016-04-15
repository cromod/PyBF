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
    save = sys.stdin.read(1)
    if save:
        byte_array[data_ptr] = ord(save)

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
    skip = 0
    for it, char in enumerate(char_chain):
        if skip:
            if char == '[': skip += 1 # Increment the level of nested loops to skip
            if char == ']': skip -= 1 # Decrement the level of nested loops to skip
            continue # Actually skip that character
        if char == '[':
            while byte_array[data_ptr]:
                # Recurse to interpret the loop
                interpret(char_chain[it+1:])
            # Skip the loop when the current cell is 0
            skip = 1
        elif char == ']':
            # End the recursion when reaching the end of the loop
            return
        else:
            read_no_loop(char)

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        with open(file_name,'r') as file:
            cmd = file.read()
            interpret(cmd)
    except IndexError:
        print "Error: provide a source file as first argument"
