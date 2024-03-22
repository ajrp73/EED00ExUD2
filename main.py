# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("Hello World...")

L0=[[1,2,3],['A','B','C'], "EED", "DAM"]

#1. Obtener L1 de manera que L1=[[1,2,3,3,2,1],['ABCCBA'], "EEDDAM", "MADDEE"] (2 Ptos.)
L1=[ L0[0]+L0[0][::-1], [''.join(L0[1] + L0[1][::-1]) ], [L0[2]+L0[3]], [''.join(reversed([L0[2]+L0[3]]))] ]

print("L1:",L1)