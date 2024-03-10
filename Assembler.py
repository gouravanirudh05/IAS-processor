memory = []
code = []                              # temp variable used to store the processed data from the assembly code file
opcodes = {
    "LOAD ": ["00000001", "00001010"],  # LOAD M(X) and LOAD MQ
    'STOR ': ["00100001", "00010011"],  # STOR M(X) and STOR M(X,28:39)
    "ADD ": "00000101",                 # ADD M(X)
    "SUB ": "00000110",                 # SUB M(X)
    "JUMP+ ": "00001101",               # JUMP+ M(X,0:19)
    "DEC": "01111111",                  # Special instruction that decrements the value in AC
    "SQUARE ": "10101010",              # Special instruction that loads a M(X) value into AC, squares it and puts it back into AC
    "SQRT": "11111110",                 # Special instruction that calculates the root of AC and saves the integer part of it in AC and first two decimal places in MQ
    "NOP": "00000000",                  # No operation
    "HALT": "11111111"                  # The exit for the program
}

with open(r"ASSEMBLY_CODE.txt", 'r') as f:
    for line in f:        # Just some file I/O and then making each line of assembly into cleaner text(remove comments, remove the number preceeding the memory location)
        code.append(line.lstrip().split(' ', maxsplit=1)[1].split('//', 1)[0].strip())
    for i in code[:30]:
        x = (bin(int(i))[2:].zfill(40) if i[0] != '-' else '1' + bin(int(i))[3:].zfill(39))
        memory.append(x)
    for line in code[30:]:
        ops = line.split(', ')
        for i in opcodes:
            for j in range(2):
                if i in ops[j]:
                    if i == "LOAD ":
                        if ops[j] == "LOAD MQ":
                            ops[j] = ops[j].replace("LOAD MQ", opcodes[i][1])
                        else:
                            ops[j] = ops[j].replace(i, opcodes[i][0])
                    elif i == "STOR ":
                        if ops[j].count(':'):
                            ops[j] = ops[j].replace(i, opcodes[i][1])
                        else:
                            ops[j] = ops[j].replace(i, opcodes[i][0])
                    else:
                        ops[j] = ops[j].replace(i, opcodes[i])
        for ind, i in enumerate(ops[:]):
            temp = i.split('M(')
            if len(temp) == 1:
                ops[ind] = ops[ind] + "0"*12
            else:
                if temp[-1][1].isnumeric():
                    temp[-1] = bin(int(temp[-1][0:2])).lstrip('0b').zfill(12)
                    ops[ind] = "".join(temp)
                else:
                    temp[-1] = bin(int(temp[-1][0])).lstrip('0b').zfill(12)
                    ops[ind] = "".join(temp)
        memory.append(''.join(ops))
    with open(r"MACHINE_CODE.txt", 'w') as k:
        for line in memory:
            k.write(line + '\n')
