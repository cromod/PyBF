# -*- coding: utf-8 -*-

import sys

byte_array = [0] # array of bytes
data_ptr = 0 # data pointer

# Basic instructions except loop
def increment_byte():
    """Increment the byte at the data pointer."""
    byte_array[data_ptr] += 1

def decrement_byte():
    """Decrement the byte at the data pointer."""
    byte_array[data_ptr] -= 1

def increment_ptr():
    """Increment the data pointer."""
    global data_ptr
    data_ptr += 1
    if data_ptr == len(byte_array):
        byte_array.append(0)

def decrement_ptr():
    """Decrement the data pointer.

    Raises:
        ValueError: if pointer is negative
    """
    global data_ptr
    data_ptr -= 1
    if data_ptr < 0:
        raise ValueError("Negative value of pointer")

def output():
    """Output the byte at the data pointer."""
    sys.stdout.write(chr(byte_array[data_ptr]))

def store():
    """Output the byte at the data pointer."""
    save = sys.stdin.read(1)
    if save:
        byte_array[data_ptr] = ord(save)

# Dictionary to call instructions except loop
instructions = {
    '+': increment_byte,
    '-': decrement_byte,
    '>': increment_ptr,
    '<': decrement_ptr,
    '.': output,
    ',': store
}

# Interpreter
def interpret(char_chain):
    """Interpret brainfuck code."""
    skip = 0
    for it, char in enumerate(char_chain):
        if skip:
            # Increment the level of nested loops to skip
            if char == '[': skip += 1
            # Decrement the level of nested loops to skip
            if char == ']': skip -= 1
            # Skip that character
            continue
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
            # Read instructions except loop
            instructions.get(char, lambda: None)()
    # Display a warning if there is no closing bracket
    if skip > 0:
        print "\nWarning: No closing bracket"

# Main
if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        with open(file_name,'r') as file:
            cmd = file.read()
            interpret(cmd)
    except IndexError:
        print "Error: provide a source file as first argument"
