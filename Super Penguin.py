class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("swim faster")


class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whosithis(self):
        print("Penguin")
    def run(self):
        print("Run Faster")
peggy=Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()
