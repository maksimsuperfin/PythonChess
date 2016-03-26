class Figure():
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def put_on_desk(self):
        print("Figure: put_on_desk")

    def move(self):
        print("Figure: move")
        self.check_move()

    def check_move(self):
        print("Figure: check_move")