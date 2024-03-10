"""
PROJECT BY:
        IMT2023005-Gourav Anirudh
        IMT2023030-Sathish Adithiyaa S V
        IMT2023104-Subhash H

Program Description:
    This project aims to calculate the magnitude of the resultant vector of n 2D input vectors.
    We have hard coded N and the respective x, y components of the vector in the MEMORY.
    These values can be changed depending on the requirements of the input.
"""
from colorama import Fore,Style  #We are using this to show the output in each phase in a different colour
from assembler import memory

"""
   This just imports the MEMORY array that has been assembled by the assembler.
   We have only used about 50 MEMORY locations, our MEMORY array will only consist of these locations.
   The MEMORY is an array of strings each if length 40. These strings are all comprised of only 0s and 1s.
"""

"""                       ************THE CODE FOR PROCESS STARTS HERE********************                           """
MEMORY = memory
PC = '000000011110'    # PC initially storing address of the first instruction
MBR = "0" * 40   # 40 bits wide
MAR = "0" * 12   # 12 bits wide
IBR = "0" * 20   # 20 bits wide
AC = "0" * 40    # 40 bits wide
MQ = "0" * 40    # 40 bits wide
IR = "0" * 8     # 8 bits wide
present = 0      # present = 0 indicates no instruction is present in IBR


def conv_to_bin(register: int, req_width: int):
    """Converts a decimal number to a binary string with the required padding"""
    if register >= 0:
        neg = False
    else:
        neg = True
    temp = bin(register).replace("0b", "").replace("-", '')
    return temp.zfill(req_width) if not neg else '1' + temp.zfill(req_width-1)


def conv_to_decimal(bin_str: str):
    """Converts a binary string into a decimal"""
    dec = int(bin_str[1:], 2)
    return -dec if int(bin_str[0]) else dec


def fetch():
    """This function is the fetch phase of the instruction cycle of the IAS ISA"""
    global MEMORY, present, PC, MAR, MBR, IBR, IR
    if present == 0:  # If no instruction is present in IBR we are fetching instruction from MEMORY
        print(Fore.RED+"PC =", end=' ')
        print(conv_to_decimal(PC))
        print(Fore.LIGHTGREEN_EX+"Now PC is transferred to MAR")

        MAR = PC   # PC given to MAR
        print(Fore.RED+"MAR =", end=' ')
        print(conv_to_decimal(MAR))

        print(Fore.LIGHTGREEN_EX+"Now the information in the MEMORY location specified in MAR is loaded into MBR")
        MBR = MEMORY[conv_to_decimal(MAR)]

        print(Fore.RED+"MBR =", end=" ")
        print(MBR)

        # Opcode from MBR being given to IR
        print(Fore.LIGHTGREEN_EX+"The right 20 bits of the MBR are transferred into the IBR")
        print("In the left instruction, the opcode is given to IR and the address field is given to MAR.")

        IR = MBR[:8]
        print(Fore.RED+"IR =", end=" ")
        print(IR)

        MAR = MBR[8:20]
        print(Fore.RED+"MAR =", end=" ")
        print(MAR)

        # If there is a right instruction, store it in IBR
        IBR = MBR[20:]
        present = 1
        print(Fore.RED+"IBR =", end=" ")
        print(IBR)

        print(Fore.YELLOW+"Fetch Completed")
        PC = conv_to_bin(conv_to_decimal(PC) + 1, 12)

    else:
        print(Fore.LIGHTGREEN_EX+"Now the right instruction that was in the IBR is now split into IR and MAR")

        IR = IBR[:8]
        print(Fore.RED+"IR =", end=" ")
        print(IR)

        MAR = IBR[8:20]
        print(Fore.RED+"MAR =", end=" ")
        print(MAR)

        present = 0
        print(Fore.LIGHTGREEN_EX+"Fetch with IBR completed")


def load():
    """ Execute LOAD instruction"""
    global MEMORY, MAR, MBR, AC

    print(Fore.LIGHTGREEN_EX+"Now in the LOAD instruction, the information in the MEMORY location specified by MAR is loaded into MBR")

    MBR = MEMORY[conv_to_decimal(MAR)]  # contents of M(X) put to MBR
    print(Fore.RED+"MBR =", end=" ")
    print(conv_to_decimal(MBR))

    print(Fore.LIGHTGREEN_EX+"The information in the MBR is transferred into AC")

    AC = MBR  # contents of MBR put to AC
    print(Fore.RED+"AC =", end=" ")
    print(conv_to_decimal(AC))


def stor():
    """ Execute STOR instruction"""
    global MEMORY, MBR, AC, MAR

    print(Fore.LIGHTGREEN_EX+"Now in the STOR function, the value in AC is first transferred into MBR")
    print(Fore.RED+"AC =", end=" ")
    print(conv_to_decimal(AC))

    MBR = AC    # Contents of AC to MBR
    print(Fore.RED+"MBR =", end=" ")
    print(conv_to_decimal(MBR))

    print(Fore.LIGHTGREEN_EX+"The data in MBR is now transferred into the MEMORY location specified by MAR")

    MEMORY[conv_to_decimal(MAR)] = MBR  # Contents of MBR gets stored in the MEMORY location indicated by MAR
    print(Fore.LIGHTGREEN_EX+f"MEMORY LOCATION {conv_to_decimal(MAR)} is now", end=" ")
    print(MEMORY[conv_to_decimal(MAR)])


def stor_right():
    """ Execute STOR M(X,28:39) instruction"""
    global MEMORY, MBR, AC, MAR, PC

    print(Fore.LIGHTGREEN_EX+"Now in the STOR M(X,28:39) instruction, the 12 rightmost bits in the AC replace the address field at M(X)")

    print(Fore.LIGHTGREEN_EX+"First, the value present at the address specified by the MAR is loaded into the MBR")

    MBR = MEMORY[conv_to_decimal(MAR)]
    print(Fore.RED+"MBR =", end=" ")
    print(MBR)

    print(Fore.LIGHTGREEN_EX+"After this, the 12 rightmost bits in the AC replace the address field of right instruction loaded into the MBR")

    MBR = MBR[:28] + AC[28:]
    print(Fore.RED+"MBR =", end=" ")
    print(MBR)

    MEMORY[conv_to_decimal(MAR)] = MBR  # Contents of MBR gets stored in the MEMORY location indicated by MAR
    print(Fore.LIGHTGREEN_EX+f"The address field in the MEMORY is changed to {MEMORY[conv_to_decimal(MAR)][28:40]} is now", end=" ")


def add():
    """Execute ADD instruction"""
    global MEMORY, MAR, MBR, AC

    print(Fore.LIGHTGREEN_EX+"Now in the ADD instruction, the value in the address specified by MAR is first loaded into MBR")

    MBR = MEMORY[conv_to_decimal(MAR)]  # Contents of MEMORY is put into MBR
    print(Fore.RED+"MBR =", end=" ")
    print(conv_to_decimal(MBR))

    print(Fore.LIGHTGREEN_EX+"The value in the MBR is added to the value already present in AC and this value is stored back in AC")

    AC = conv_to_bin(conv_to_decimal(AC) + conv_to_decimal(MBR), 40)
    print(Fore.RED+"AC =", end=' ')  # Performing Addition and storing the result in AC
    print(conv_to_decimal(AC))


def sub():
    """Execute ADD instruction"""
    global MEMORY, MAR, MBR, AC

    print(Fore.LIGHTGREEN_EX+"Now in the SUB function, the value in the address specified by MAR is first loaded into MBR")

    MBR = MEMORY[conv_to_decimal(MAR)]  # Contents of MEMORY is put into MBR
    print(Fore.RED+"MBR =", end=" ")
    print(conv_to_decimal(MBR))

    print(Fore.LIGHTGREEN_EX+"The value in the MBR is subtracted from the value already present in AC and this value is stored back in AC")

    AC = conv_to_bin(conv_to_decimal(AC) - conv_to_decimal(MBR), 40)
    print(Fore.RED+"AC =", end=' ')  # Performing Addition and storing the result in AC
    print(conv_to_decimal(AC))


def SQUARE():
    """Execute SQUARE instruction"""
    global MEMORY, MAR, MBR, AC

    print(Fore.LIGHTGREEN_EX+"Now in the SQUARE M(X) instruction, the value in M(X) is loaded into AC and then squared, this value is stored back into AC")
    print(Fore.LIGHTGREEN_EX+"The value in the MEMORY location specified by MAR is loaded into MBR.")

    MBR = MEMORY[conv_to_decimal(MAR)]
    print(Fore.RED+"MBR =", end=" ")
    print(conv_to_decimal(MBR))

    print(Fore.LIGHTGREEN_EX+"The information in the MBR is transferred into AC")

    AC = MBR  # contents of MBR put to AC
    print(Fore.RED+"AC =", end=" ")
    print(conv_to_decimal(AC))

    AC = conv_to_bin(conv_to_decimal(AC)**2, 40)

    print(Fore.LIGHTGREEN_EX+"The value in AC is now squared")
    print(Fore.RED+"AC =", end=" ")
    print(conv_to_decimal(AC))


def SQRT():
    """Execute SQRT instruction"""
    global AC, MQ

    print(Fore.LIGHTGREEN_EX+"Now in the SQRT instruction, the square root of the value present in AC is calculated.")
    print(Fore.LIGHTGREEN_EX+"The integer part is stored in AC and the first two numbers after the decimal point are stored in MQ")

    print(Fore.LIGHTGREEN_EX+"Before root the value in AC is", end=' ')
    print(conv_to_decimal(AC))

    sqrt_val = conv_to_decimal(AC)**0.5
    AC = conv_to_bin(int(sqrt_val), 40)
    MQ = conv_to_bin(int((sqrt_val - int(sqrt_val))*100), 40)

    print(Fore.RED+"AC =", end=" ")
    print(conv_to_decimal(AC))

    print(Fore.RED+"MQ =", end=" ")
    print(conv_to_decimal(MQ))


def DEC():
    """Execute DEC instruction"""
    global AC

    print(Fore.LIGHTGREEN_EX+"Now in the DEC instruction, the value in AC is decremented by 1")

    print(Fore.LIGHTGREEN_EX+"The value of AC before DEC is", end=" ")
    print(conv_to_decimal(AC))

    AC = conv_to_bin(conv_to_decimal(AC) - 1, 40)

    print(Fore.LIGHTGREEN_EX+"The value after DEC")
    print(Fore.RED+"AC =", end=" ")
    print(conv_to_decimal(AC))


def jump():
    """Execute JUMP +M(X,0:19)"""
    global MAR, PC, AC

    print(Fore.LIGHTGREEN_EX+"Now in JUMP+ M(X,0:19) instruction, if AC is non negative then it jumps to X")

    if AC[0] == "0":
        PC = MAR
        print(Fore.YELLOW+"JUMP successful")
        print(Fore.RED+"PC =", end=" ")
        print(conv_to_decimal(PC))
    else:
        print(Fore.YELLOW+"JUMP unsuccessful")

    print(Fore.RED+"AC =", end=" ")
    print(conv_to_decimal(AC))


def load_MQ():
    """Execute LOAD MQ instruction"""
    global AC, MQ

    print(Fore.LIGHTGREEN_EX+"Now in the LOAD MQ instruction, the value in MQ is transferred into AC")

    print(Fore.RED+"MQ =", end=" ")
    print(conv_to_decimal(MQ))

    AC = MQ
    print(Fore.RED+"AC =", end=" ")
    print(conv_to_decimal(AC))


def decode_execute():
    global MEMORY, IR
    """Decoding the opcodes will happen here and corresponding instructions are executed
    (It represents the functionality of the Control circuits)"""
    opcode = IR
    print(Fore.YELLOW+"Entering the Decode phase")
    # Checking opcode for LOAD instruction in the IR (opcode=00000001)
    if opcode == "00000001":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as LOAD")
        load()
    # Checking opcode for STORE instruction in the IR (opcode=00100001)
    elif opcode == "00100001":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as STOR")
        stor()
    # Checking opcode for ADD instruction in the IR (opcode=00000101)
    elif opcode == "00000101":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as ADD")
        add()
    # Checking opcode for SUB instruction in the IR (opcode=00000110)
    elif opcode == "00000110":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as SUB")
        sub()
    # Checking opcode for JUMP+M(X,0:19) instruction in the IR (opcode=00001111)
    elif opcode == "00001101":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as JUMP+M(X,0:19)")
        jump()
    # Checking opcode for HALT instruction in the IR (opcode=11111111)
    elif opcode == "11111111":
        print(Fore.CYAN+f"The integer part of the magnitude of the resultant vector is {conv_to_decimal(MEMORY[6])}")
        print(Fore.CYAN+f"The decimal part of the magnitude of the resultant vector is .{conv_to_decimal(MEMORY[7])}")

        print(Fore.LIGHTBLUE_EX+"IR has been decoded as HALT")
        print(Fore.CYAN+"The magnitude of resultant vector is approx", end=" ")
        print(conv_to_decimal(MEMORY[6]) + conv_to_decimal(MEMORY[7])/100, end="")
        print()
        print(Fore.YELLOW + "Program executed successfully")
        exit()

    #Checking opcode for NOP in the IR(opcode=00000000)
    elif opcode == "00000000":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as NOP")
        pass
    #Checking opcode for DEC in the IR(opcode=01111111)
    #This is a special instruction introduced by us
    elif opcode == "01111111":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as DEC")
        DEC()

    #Checking opcode for LOAD MQ in the IR(opcode=00001010)
    elif opcode == "00001010":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as LOAD MQ")
        load_MQ()

    #Checking opcode for STOR RIGHT in the IR(opcode=00010011)
    elif opcode == "00010011":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as STOR RIGHT")
        stor_right()

    #Checking opcode for SQUARE in the IR(opcode=10101010)
    #This is a special isntruction instroduced by us
    elif opcode == "10101010":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as SQUARE")
        SQUARE()

    #Checking opcdoe for SQRT in the IR(opcode=11111110)
    #This is a special instruction introduced by us
    elif opcode == "11111110":
        print(Fore.LIGHTBLUE_EX+"IR has been decoded as SQRT")
        SQRT()

def main():
    """This is the Driver Code"""
    print(Fore.YELLOW+"START:")
    while True:  # Once HALT instruction is found the processor cycle execution stops
        fetch()   # Fetch cycle
        decode_execute()  # Decode using the control circuits and then execute(Check opcodes from MEMORY and then perform that instruction)


if __name__ == "__main__":
    main()

"""                             **********THE PROCESSOR CODE ENDS HERE***************                               """
