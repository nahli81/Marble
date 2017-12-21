
from marble_images import *

##import sys

alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.',',','!','%','$',"'"]
       
text_az = [pygame.image.load('dark_graphic/'+i+'_.png') for i in alphabet_upper]

text_dict = {i[0]:i[1] for i in zip(alphabet_upper, text_az)}


class Textbox(object):
    def __init__(self):

##        self.option0 = pygame.image.load('text/op1.png').convert_alpha()
##        self.option1 = pygame.image.load('text/op2.png').convert_alpha()
##

        self.bubble_closed = []
        self.bubble_open = [b_open6,b_open6,b_open5,b_open5,b_open4,b_open4,b_open3,b_open3,b_open2,b_open2,b_open1,b_open1]

        self.is_textbox = True
        self.is_message = False
        self.is_option = False
        self.lock = True

        self.graphic = None
        self.graphic_ch = None
        self.graphic_pos = None
        
        self.counter = 0
        self.selector = 0

        self.message_list = []
        self.option_dict = {}
        self.blit_list = []
        self.text = []
        self.y_start = 0
        self.start_pos = 0
        self.prime_pos = 0
        
    def bubble(self):
        
        if self.graphic_ch == None or self.graphic_ch == 'bubble_open':
            self.graphic_ch = 'bubble_open'
            if self.bubble_open == []:
                self.bubble_close = [b_close5,b_close5,b_close4,b_close4,b_close3,b_close3,b_close2,b_close2,b_close1,b_close1]
                self.graphic = b_open6
            else:
                self.graphic = self.bubble_open.pop()
                    
        elif self.graphic_ch == 'bubble_close':
            self.graphic_ch = 'bubble_close'
            if self.bubble_close == []:
                self.bubble_open = [b_open6,b_open6,b_open5,b_open5,b_open4,b_open4,b_open3,b_open3,b_open2,b_open2,b_open1,b_open1]
                self.graphic_ch = None; self.graphic = None; self.is_message = False
            else: self.graphic = self.bubble_close.pop()

    def make_messages(self, pos, text, question):

        self.grapic_pos = (pos[0]-5, pos[1]-180)
        prime_pos = pos
        start_pos = pos[0]+5
        
        if len(text)> 70: y_start = prime_pos[1]-150
        elif len(text)>25: y_start = prime_pos[1]-120
        else: y_start = prime_pos[1]-80
        
        self.lock = False
        if question != None:
            self.make_option_box(question)
            self.is_option = True
            
        self.blit_list = []; self.text = []
        text = text.split('\n')[::-1]
        text.reverse()
        for t in text:
            self.message_list.append((pos,prime_pos,start_pos,y_start,t))
        
    def message(self):
        m = self.message_list.pop()
        self.graphic_pos = (m[0][0]-5, m[0][1]-180)
        prime_pos = m[1]
        start_pos = m[2]
        y_start = m[3]
        for t in m[4]:
            
            start_pos += 15
            #return words outside bubble
            if start_pos > prime_pos[0] + 300 and t == '%':
                y_start += 30; start_pos = prime_pos[0]+5
                
            self.blit_list.append((text_dict[t], (start_pos, y_start)))
            
            if t =='I' or t == ',' or t == "'" or t == '.': start_pos -= 5
            
        self.blit_list = self.blit_list[::-1]

    def next_message(self):
        
        if self.is_textbox and self.is_message:
            if len(self.message_list)>0:
                self.blit_list = []; self.text = []
                self.message()
            elif self.is_option:
                self.lock = True
                self.blit_list = []; self.text = []

    def make_option_box(self, text):
        self.selector = 0
        self.y_start = 500
        self.start_pos = 40
        
        options = text.split('\n')
        self.option_dict = {i:None for i in range(len(options))}
        
        for i in range(len(options)):
            option = []
            for t in options[i]:
                self.start_pos += 14
                option.append((text_dict[t], (self.start_pos, self.y_start)))
            self.y_start += 30; self.start_pos = 40;
            self.option_dict[i] = option

        self.y_start = 500
        self.start_pos = 40

    def select_option(self):
        self.lock = False
        self.is_option = False
        self.option_dict = {}
        return self.selector
        
    def blit_current_message(self, screen):
        self.bubble()

        if self.graphic != None:
            screen.blit(self.graphic, self.graphic_pos)

        if self.graphic == b_open6:

    ##        print(self.lock, self.is_option)
    ##        print(self.option_dict.keys())
            if not self.lock:
                if len(self.blit_list)> 0:
                    self.text.append(self.blit_list.pop())
                    
                for t in self.text: screen.blit(t[0],t[1])
                
                #down arrow
    ##            if len(self.message_list)>0:
    ##                if len(self.down_list)>0:
    ##                    screen.blit(self.down_list.pop(), (0,470))
    ##                else:
    ##                    self.down_list = [self.down1_img, self.down2_img, self.down3_img, self.down4_img]
    ##                    screen.blit(self.down_list.pop(), (0,470))
                
            elif self.lock and self.is_option:
                for k in self.option_dict.keys():
                    for letter in self.option_dict[k]:
                        screen.blit(letter[0], letter[1])

                if self.selector == 0: screen.blit(self.option0, self.pos)
                elif self.selector == 1: screen.blit(self.option1, self.pos)

