import string
import random
class Robot(object):
    def __init__(self):
        self.name = self.generate()
        self.name_holder = self.name

    def generate(self):
        char_string = string.ascii_uppercase
        num_list = '0123456789'
        num = random.choices(num_list, k=3)
        letter = random.choices(char_string, k=2)
        return (''.join(letter + num))

    def reset(self):
        while self.name_holder == self.name :
            self.name = self.generate()
