# -*- coding: utf-8 -*-

import sys

array = [0] # byte array
ptr = 0 # data pointer

def readNoLoop(char):
  global ptr
  # Increment/Decrement the byte at the data pointer
  if char=='+':
    array[ptr] += 1
  elif char=='-':
    array[ptr] -= 1
    if array[ptr] < 0:
      raise ValueError("Negative value in array")
  # Increment/Decrement the data pointer
  elif char=='>':
    ptr += 1
    while(ptr>=len(array)-1):
      array.append(0)
  elif char=='<':
    ptr -= 1
    if ptr < 0:
      raise ValueError("Negative value of pointer")
  # Output the byte at the data pointer
  elif char=='.':
    sys.stdout.write(chr(array[ptr]))
  # Store one byte of input in the byte at the data pointer 
  elif char==',':
    array[ptr] = ord(sys.stdin.read(1))
  #print ptr, array
      
def interpret(charChain):
  it = 0
  loopBegin = []
  while(it<len(charChain)):
    if charChain[it]=='[':
      loopBegin.append(it)
    elif charChain[it]==']':
      subChain = charChain[loopBegin[-1]+1:it]
      while(array[ptr]>0):
        interpret(subChain)
      loopBegin.pop()
    else:
      readNoLoop(charChain[it])
    it+=1

if __name__ == "__main__":
  # Brainfuck program to print "Hello World!"
  cmd = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
  try:
    interpret(cmd)
  except:
    raise
