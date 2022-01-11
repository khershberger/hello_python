import sys

class HelloClass(object):
    def __init__(self):
        self.a = None
        self.count = 0

    def say_hello(sself):
        print("Hello world!")

    def show_args(self):
        print("Arguments: " + str(sys.argv))
        if len(sys.argv) == 2:
            print(sys.argv[1])

    def increment(self):
        self.count += 1
        return True
    
    def set_count(self, c):
        self.count = c
    
    def get_count(self):
        return self.count

def main():
    hc = HelloClass()
    hc.say_hello()
    hc.show_args()
    return 0

def return_true():
    return True

if __name__ == '__main__':
    main()
