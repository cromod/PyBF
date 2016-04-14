# -*- coding: utf-8 -*-

import sys

byte_array = [0] # array of bytes
data_ptr = 0 # data pointer

def read_no_loop(char):
    global data_ptr
    # Increment/Decrement the byte at the data pointer
    if char == '+':
        byte_array[data_ptr] += 1
    elif char == '-':
        byte_array[data_ptr] -= 1
        if byte_array[data_ptr] < 0:
            raise ValueError("Negative value in array")
    # Increment/Decrement the data pointer
    elif char == '>':
        data_ptr += 1
        while data_ptr >= len(byte_array)-1:
            byte_array.append(0)
    elif char == '<':
        data_ptr -= 1
        if data_ptr < 0:
            raise ValueError("Negative value of pointer")
    # Output the byte at the data pointer
    elif char == '.':
        sys.stdout.write(chr(byte_array[data_ptr]))
    # Store one byte of input in the byte at the data pointer
    elif char == ',':
        byte_array[data_ptr] = ord(sys.stdin.read(1))
    #print data_ptr, byte_array
      
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
