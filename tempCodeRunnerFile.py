    def fetch(self):
        self.MAR = self.PC
        self.MBR = self.memory[self.MAR]
        self.IBR = self.MBR[20:]
        self.IR = self.MBR[:8]
        self.MAR = self.MBR[8:20]
        self.fetch_completed = True