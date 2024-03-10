# IAS-processor
This is a python code that mimic the IAS( Von neumann machine ) which takes the memory as input and gives the output
 EG 212 COMPUTER ARCHTECTURE– Processor design
PROJECT-1: IAS Processor design

PROJECT DESCRIPTION:
TOPIC- Calculation of the magnitude of the resultant vector of N 2D vectors, given their x and y components.

FILES SUBMITTED: 
We have created the following five files for our program-
1) CA_program.c - This file demonstrates our program. This C program has N which is the number of vectors as an input. Then the respective values of x and y components of the N given vectors are given as input. We calculate the value of the magnitude of the resultant of the N given vectors. The result is accurate up to 2 decimal places.
2) ASSEMBLY_CODE.txt - This file has the assembly code for our program.
3) ASSEMBLER.py - This file contains an assembler that converts the 	assembly code into binary instructions which is stored in MACHINE_CODE.txt
4) MACHINE_CODE.txt - This file contains the binary representation of the data and instructions which acts as the MEMORY for the processor.py file.
5) PROCESSOR.py - This file contains code which mimics the processor. It has various functions which represent the various instructions used in the IAS architecture.				

EXTRA INSTRUCTIONS DESIGNED:
INSTRUCTION	OPCODE	DESCRIPTION
SQRT	11111110	It takes square root of value present in AC and stores integer part of the result in AC and the first two decimals in MQ.
SQUARE M(X)	10101010	Squares the value present in memory location ‘X’ and stores the result in AC.
DEC	01111111	Decrements the value of AC by 1.
HALT	11111111	Terminates the program.

STEPS TO RUN THE PROCESSOR CODE: 
STEP 1: Save the CA_program.c, ASSEMBLY_CODE.txt, ASSEMBLER.py, 	     MACHINE_CODE.txt and PROCESSOR.py in the same directory (as            	      they import files from each other).
STEP 2: On the terminal, enter ‘Python3 pip install colorama’ if not 		      installed.

STEP 3: Run the command python3 PROCESSOR.py
 
STEP 4: Output of the processor file is shown with each register's contents 	      printed and information on how the data is being transferred. 
  


THE C CODE:
We are implementing a C program that calculates the magnitude of the resultant of N 2D vectors whose x and y components are given. 
N and the respective x and y components of the vectors are hard coded in the IAS-Program. These values can be changed easily, the memory contains buffer space for larger values of N to store the x and y component arrays.


  





ASSEMBLY CODE:
The following below is the Assembly Language Code and memory implementation. It contains comments wherever necessary.

 





ASSEMBLER OUTPUT:
The following is the output of the assembler which represents the memory. The first 30 lines (0 – 29) contain data, the instructions start after this. So, we have set PC = 30. This memory is imported by the processor:

 
 




PROCESSOR OUTPUT
We have used the package colorama to indicate different phases of the cycle with distinct colors. The table below explains the use of these colors.
COLOR	USE
RED	Register values
YELLOW	Beginning or completion of a phase
BLUE	The Decode of IR
GREEN	Description of what is happening in each instruction

 
  
  
  
  
  
  



       
 
  
  

  
  
  
  
  
  
  

  
  




PROJECT BY:
Roll No.	Name
IMT2023005	Gourav Anirudh B.J

IMT2023030	Sathish Adithiyaa S V
IMT2023104	Subhash H

 


