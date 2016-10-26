import django as dj


class HelloWorld:
    def __init__(self):
        self.test()

    def test(self):
        dj.get_version()

if __name__ == '__main__':
    s = HelloWorld()
