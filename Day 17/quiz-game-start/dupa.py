class Processor:
    should_process: bool

    def __init__(self, should_process):
        self.should_process = should_process

    def process(self):
        if self.should_process:
            print("Processing...")
        else:
            print("Dupa!")


p = Processor(should_process=True)
p.process()

p.should_process = True
p.process()
p.process()
p.process()
p.process()
