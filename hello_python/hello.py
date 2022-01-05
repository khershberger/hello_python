class HelloClass(object):
    def __init__(self):
        self.a = None
        self.count = 0

    def say_hello(sself):
        print("Hello world!")
    
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
    return 0

def return_true():
    return True

if __name__ == '__main__':
    main()
