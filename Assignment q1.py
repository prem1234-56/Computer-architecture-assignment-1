
# Addressing Modes

address = 200
R1 = 40

memory = {
    200: 500,
    240: 900
}

# a) Immediate Addressing
immediate = 25
print("Immediate Addressing:")
print("Operand Value =", immediate)

# b) Direct Addressing
direct_EA = address
print("\nDirect Addressing:")
print("Effective Address =", direct_EA)
print("Operand Value =", memory[direct_EA])

# c) Indirect Addressing
indirect_EA = memory[address]
print("\nIndirect Addressing:")
print("Effective Address =", indirect_EA)
print("Operand Value = Not available")

# d) Indexed Addressing
indexed_EA = address + R1
print("\nIndexed Addressing:")
print("Effective Address =", indexed_EA)
print("Operand Value =", memory[indexed_EA])
