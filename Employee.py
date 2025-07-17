class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0
        self.competency = 0
        self.output = 0
        self.jobSat = 0
        self.laborHrs = 0
        self.training = False
    def work(self):
    def train(self):
        # Does this ever become False?
        # There needs to be a way to ensure that this loop breaks
        while self.training == True:
            self.laborHrs = 0
    def quit(self):
