import unittest
from unittest.mock import patch
import IASprocessor as ip

class TestCalc(unittest.TestCase):

    def test_conv_to_bin(self):
        self.assertEqual(ip.conv_to_bin(4, 4), '0100')
        self.assertEqual(ip.conv_to_bin(10, 4), '1010')
        self.assertEqual(ip.conv_to_bin(15, 4), '1111')
        self.assertEqual(ip.conv_to_bin(20, 4), '10100')
        # For negative numbers
        self.assertEqual(ip.conv_to_bin(-4, 4), '1100')
        self.assertEqual(ip.conv_to_bin(-10, 4), '11010')
        self.assertEqual(ip.conv_to_bin(-15, 4), '11111')
        self.assertEqual(ip.conv_to_bin(-20, 4), '110100')

    def test_conv_to_dec(self):
        self.assertEqual(ip.conv_to_decimal('0100'), 4)
        self.assertEqual(ip.conv_to_decimal('1010'), -2)
        self.assertEqual(ip.conv_to_decimal('01111'), 15)
        self.assertEqual(ip.conv_to_decimal('010100'), 20)
        # For negative numbers
        self.assertEqual(ip.conv_to_decimal('1100'), -4)
        self.assertEqual(ip.conv_to_decimal('11010'), -10)
        self.assertEqual(ip.conv_to_decimal('11111'), -15)
        self.assertEqual(ip.conv_to_decimal('110100'), -20)

    @patch('IASprocessor.MEMORY', ['0'*40]*50)
    @patch('IASprocessor.PC', '000000011110')
    # Ensure fetch phase correctly updates MAR from PC
    def fetch(self):
        self.MAR = self.PC
        self.MBR = self.memory[self.MAR]
        self.IBR = self.MBR[20:]
        self.IR = self.MBR[:8]
        self.MAR = self.MBR[8:20]
        self.fetch_completed = True

    @patch('IASprocessor.MEMORY', ['0'*40]*50)
    def test_load(self):
        ip.MAR = '000000000001'
        ip.MEMORY[1] = '0000000000000000000000000000000000001010'
        ip.load()
        self.assertEqual(ip.MBR, '0000000000000000000000000000000000001010')
        self.assertEqual(ip.AC, '0000000000000000000000000000000000001010')

    @patch('IASprocessor.MEMORY', ['0'*40]*50)
    def test_stor(self):
        ip.AC = '0000000000000000000000000000000000001010'
        ip.MAR = '000000000010'
        ip.stor()
        self.assertEqual(ip.MEMORY[2], '0000000000000000000000000000000000001010')

    @patch('IASprocessor.MEMORY', ['0'*40]*50)
    def test_stor_right(self):
        ip.MAR = '000000000011'
        ip.AC = '0000000000000000000000000000000000001111'
        ip.MEMORY[3] = '0000000000000000000000000000000000000000'
        ip.stor_right()
        self.assertEqual(ip.MEMORY[3], '0000000000000000000000000000000000001111')

    @patch('IASprocessor.MEMORY', ['0'*40]*50)
    def test_add(self):
        ip.AC = '0000000000000000000000000000000000000100'
        ip.MAR = '000000000100'
        ip.MEMORY[4] = '0000000000000000000000000000000000000011'
        ip.add()
        self.assertEqual(ip.AC, '0000000000000000000000000000000000000111')

    @patch('IASprocessor.MEMORY', ['0'*40]*50)
    def test_sub(self):
        ip.AC = '0000000000000000000000000000000000000100'
        ip.MAR = '000000000101'
        ip.MEMORY[5] = '0000000000000000000000000000000000000011'
        ip.sub()
        self.assertEqual(ip.AC, '0000000000000000000000000000000000000001')

    @patch('IASprocessor.MEMORY', ['0'*40]*50)
    def test_SQUARE(self):
        ip.MAR = '000000000110'
        ip.MEMORY[6] = '0000000000000000000000000000000000000011'
        ip.SQUARE()
        self.assertEqual(ip.AC, '0000000000000000000000000000000000001001')

    def test_SQRT(self):
        ip.AC = '0000000000000000000000000000000000100000'
        ip.SQRT()
        self.assertEqual(ip.AC, '0000000000000000000000000000000000000101')


    def test_DEC(self):
        ip.AC = '0000000000000000000000000000000000000100'
        ip.DEC()
        self.assertEqual(ip.AC, '0000000000000000000000000000000000000011')

    @patch('IASprocessor.MAR', '000000000111')
    def test_jump(self):
        ip.AC = '0000000000000000000000000000000000000000'
        ip.jump()
        self.assertEqual(ip.PC, '000000000111')

    def test_loadMQ(self):
        ip.MQ = '0000000000000000000000000000000000001001'
        ip.load_MQ()
        self.assertEqual(ip.AC, '0000000000000000000000000000000000001001')

    @patch('IASprocessor.IR', '00000101')
    def test_decode_execute(self):
        ip.MAR = '000000001000'
        ip.MEMORY[8] = '0000000000000000000000000000000000000011'
        ip.AC = '0000000000000000000000000000000000000100'
        ip.decode_execute()
        self.assertEqual(ip.AC, '0000000000000000000000000000000000000111')

if __name__ == '__main__':
    unittest.main()
