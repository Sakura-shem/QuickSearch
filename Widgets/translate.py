from Widgets import RoundShadow
class Window(RoundShadow):

    def __init__(self, size, position):
        super().__init__()
        self.setWindowTitle("result")
        self.resize(400, size)
        self.move(position[0], position[1])