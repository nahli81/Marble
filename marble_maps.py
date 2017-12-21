
from marble_chars import *
import sys

class Red_cave(object):
    def __init__(self):
        self.background = red_cave_inside
        self.background2 = None
        self.background3 = red_cave
        self.background_pos = (-500,-300)
        self.background2_pos = None
        self.background3_pos = (-300,-300)
        self.plat_img = platform1
##        self.goblik_total = 1

        self.script_1 = True
        self.textbox = Textbox()

        self.P = Phalanx((0,0), 0, 0, None)
        self.gob_list = [Goblik(i, None) for i in [(200,0),(200,700)]] +\
                        [Troglik(i, None) for i in [(200,500)]] 
        self.dead_list = []

        self.map_dict = {'plat_a':{'img_pos':[(-100+i*50,330) for i in range(16)],
                                    'x_range':(-100,600),
                                    'y_range':330},
                         'plat_b':{'img_pos':[(750+i*50,450) for i in range(2)],
                                    'x_range':(750,750),
                                    'y_range':450},
                         'plat_c':{'img_pos':[(850+i*50,550) for i in range(2)],
                                    'x_range':(850,850),
                                    'y_range':550},
                         'plat_d':{'img_pos':[(0+i*50,750) for i in range(20)],
                                    'x_range':(0,950),
                                    'y_range':750},
                         'plat_e':{'img_pos':[(-100+i*50,1150) for i in range(13)],
                                    'x_range':(-100,450),
                                    'y_range':1150},
                         'plat_f':{'img_pos':[(-150+i*50,1350) for i in range(23)],
                                    'x_range':(-150,850),
                                    'y_range':1350},
                         'plat_g':{'img_pos':[(50+i*50,1250) for i in range(2)],
                                    'x_range':(50,50),
                                    'y_range':1250},
                         'plat_h':{'img_pos':[(750+i*50,650) for i in range(2)],
                                    'x_range':(750,750),
                                    'y_range':650},
                         
                         'plat_wall_1':{'img_pos':[(-150,1300+i*-50) for i in range(26)],
                                    'x_range':(-150,-150),
                                    'y_range':0},
                         'plat_wall_2':{'img_pos':[(950,1300+i*-50) for i in range(26)],
                                    'x_range':(950,950),
                                    'y_range':0},
                         'climb_wall_1':{'img_pos':[(150+k*50,1100+i*-50) for k in range(2) for i in range(9)],
                                        'x_range':(150,200),
                                        'y_range':650}
                         }
        self.wall_dict = {'plat_wall_1':{'x_range':self.map_dict['plat_wall_1']['x_range'],
                                         'y_range':(1300,-50)},
                          'plat_wall_2':{'x_range':self.map_dict['plat_wall_2']['x_range'],
                                         'y_range':(1300,-50)},
                          }
        
        self.climb_dict = {'climb_wall_1':{'img_pos':self.map_dict['climb_wall_1']['img_pos'],
                                        'x_range':self.map_dict['climb_wall_1']['x_range'],
                                        'y_range':650}
                           }


    def blit_gobs(self,screen,current_map,H):
        for g in self.gob_list:
            g.shift(current_map,H)
            screen.blit(g.img, g.pos)
            if g.graphic != None: screen.blit(g.graphic, g.graphic_pos)
            if g.dead:
                self.dead_list.append(g)
                self.gob_list.remove(g)

    def blit_dead_list(self,screen,current_map,H):
        for g in self.dead_list:
            screen.blit(g.img, g.pos)

    def blit_platform(self, screen):
        self.plat_map = self.map_dict['plat_a']['img_pos'] +\
                        self.map_dict['plat_b']['img_pos'] +\
                        self.map_dict['plat_c']['img_pos'] +\
                        self.map_dict['plat_d']['img_pos'] +\
                        self.map_dict['plat_e']['img_pos'] +\
                        self.map_dict['plat_f']['img_pos'] +\
                        self.map_dict['plat_g']['img_pos'] +\
                        self.map_dict['plat_h']['img_pos'] +\
                        self.map_dict['plat_wall_1']['img_pos'] +\
                        self.map_dict['plat_wall_2']['img_pos'] +\
                        self.map_dict['climb_wall_1']['img_pos']

        self.wall_dict = {'plat_wall_1':{'x_range':self.wall_dict['plat_wall_1']['x_range'],
                                         'y_range':self.wall_dict['plat_wall_1']['y_range']},
                          'plat_wall_2':{'x_range':self.wall_dict['plat_wall_2']['x_range'],
                                         'y_range':self.wall_dict['plat_wall_2']['y_range']},
                          }

        self.climb_dict = {'climb_wall_1':{'img_pos':self.map_dict['climb_wall_1']['img_pos'],
                                        'x_range':self.map_dict['climb_wall_1']['x_range'],
                                        'y_range':self.map_dict['climb_wall_1']['y_range']}
                           }
        
        for pos in self.plat_map:
            screen.blit(self.plat_img, pos)

    def script(self, pos):
        #later on, approach character
        if self.script_1:
            self.textbox.is_message = True
            self.textbox.make_messages(pos,"HEY%BUDDY,%HOWS%IT%GOING$%I%HEARD%WE%WERE%TESTIN'%OUT%SOME%FUNCTIONS!%I%THINK%THIS%PROJECT%IS%GOING%WELL.\nHOW%ABOUT%YOU$", None)
            self.script_1 = False
            
class Citycity(object):
    def __init__(self):
        self.background = city_city
        self.background2 = None
        self.background3 = city_back
        self.background_pos = (-25,-1050)
        self.background2_pos = None
        self.background3_pos = (-100,-475)
        self.plat_img = platform1
        self.goblik_total = 1

        self.script_a1 = True
        self.script_a2 = False
        self.script_b1 = True
        self.script_c1 = True
        self.textbox = Textbox()
        self.dead_list = []
        self.P = Phalanx((0,0), 0, 0, None)
        self.gob_list = [People1((750,290)),Hinin1((1050,290)),People2((2850,390)),Girl((1550,295))]

        self.map_dict = {'plat_a':{'img_pos':[(200+i*50,550) for i in range(50)],
                                    'x_range':(200,2600),
                                    'y_range':550},
                         'plat_b':{'img_pos':[(2700+i*50,600) for i in range(2)],
                                    'x_range':(2700,2700),
                                    'y_range':600},
                         'plat_c':{'img_pos':[(2750+i*50,650) for i in range(17)],
                                    'x_range':(2800,3500),
                                    'y_range':650},
                         'plat_d':{'img_pos':[(2700+i*50,500) for i in range(2)],
                                    'x_range':(2700,2700),
                                    'y_range':500},
                         'plat_e':{'img_pos':[(2800+i*50,450) for i in range(3)],
                                    'x_range':(2800,2850),
                                    'y_range':450},
                         'plat_f':{'img_pos':[(2950+i*50,400) for i in range(2)],
                                    'x_range':(2950,2950),
                                    'y_range':400},
                         'plat_g':{'img_pos':[(3050+i*50,350) for i in range(10)],
                                    'x_range':(3050,3450),
                                    'y_range':350},
                         'plat_h':{'img_pos':[(2950+i*50,300) for i in range(2)],
                                    'x_range':(2950,2950),
                                    'y_range':300},
                         'plat_i':{'img_pos':[(2850+i*50,250) for i in range(2)],
                                    'x_range':(2850,2850),
                                    'y_range':250},
                         'plat_j':{'img_pos':[(2750+i*50,200) for i in range(2)],
                                    'x_range':(2750,2750),
                                    'y_range':200},
                         'plat_k':{'img_pos':[(2600+i*50,150) for i in range(3)],
                                    'x_range':(2600,2650),
                                    'y_range':150},
                         'plat_l':{'img_pos':[(1300+i*50,100) for i in range(26)],
                                    'x_range':(1300,2500),
                                    'y_range':100},
                         'plat_m':{'img_pos':[(1200+i*50,50) for i in range(2)],
                                    'x_range':(1200,1200),
                                    'y_range':50},
                         'plat_n':{'img_pos':[(1100+i*50,0) for i in range(2)],
                                    'x_range':(1100,1100),
                                    'y_range':0},
                         'plat_o':{'img_pos':[(1000+i*50,-50) for i in range(2)],
                                    'x_range':(1000,1000),
                                    'y_range':-50},
                         'plat_p':{'img_pos':[(600+i*50,-100) for i in range(8)],
                                    'x_range':(600,900),
                                    'y_range':-100},
                         'plat_q':{'img_pos':[(2300+i*50,50) for i in range(3)],
                                    'x_range':(2300,2350),
                                    'y_range':50},
                         'plat_r':{'img_pos':[(2500+i*50,0) for i in range(3)],
                                    'x_range':(2500,2600),
                                    'y_range':0},
                         'plat_s':{'img_pos':[(2750+i*50,-50) for i in range(3)],
                                    'x_range':(2750,3650),
                                    'y_range':-50},
                         }

        self.wall_dict = {}

        self.climb_dict = {}

    def blit_gobs(self,screen,current_map,H):
        for g in self.gob_list:
            g.shift(current_map,H)
            if not g.back and not g.dead: screen.blit(g.img, g.pos)
            if g.graphic != None: screen.blit(g.graphic, g.graphic_pos)

    def blit_dead_list(self,screen,current_map,H):
        for g in self.gob_list:
            if g.dead: screen.blit(g.img, g.pos)
            elif g.back: screen.blit(g.img, g.pos)

    def blit_platform(self, screen):
        self.plat_map = self.map_dict['plat_a']['img_pos'] +\
                        self.map_dict['plat_b']['img_pos'] +\
                        self.map_dict['plat_c']['img_pos'] +\
                        self.map_dict['plat_d']['img_pos'] +\
                        self.map_dict['plat_e']['img_pos'] +\
                        self.map_dict['plat_f']['img_pos'] +\
                        self.map_dict['plat_g']['img_pos'] +\
                        self.map_dict['plat_h']['img_pos'] +\
                        self.map_dict['plat_i']['img_pos'] +\
                        self.map_dict['plat_j']['img_pos'] +\
                        self.map_dict['plat_k']['img_pos'] +\
                        self.map_dict['plat_l']['img_pos'] +\
                        self.map_dict['plat_m']['img_pos'] +\
                        self.map_dict['plat_n']['img_pos'] +\
                        self.map_dict['plat_o']['img_pos'] +\
                        self.map_dict['plat_p']['img_pos'] +\
                        self.map_dict['plat_q']['img_pos'] +\
                        self.map_dict['plat_r']['img_pos'] +\
                        self.map_dict['plat_s']['img_pos']
                        
        self.wall_dict = {}
        self.climb_dict = {}

        for pos in self.plat_map:
            screen.blit(self.plat_img, pos)
            
    def script(self,H):
        if self.gob_list[0].is_talking and self.script_a1:
            self.textbox.is_message = True
            self.textbox.make_messages((self.gob_list[0].pos[0],H.pos[1]),"HEY%BUDDY,%HOWS%IT%GOING$%I%HEARD%WE%WERE%TESTIN'%OUT%SOME%FUNCTIONS!%I%THINK%THIS%PROJECT%IS%GOING%WELL.\nHOW%ABOUT%YOU$", None)
            self.textbox.make_messages(H.pos,"WHAT%IS%ALL%THIS%ABOUT$", None)
            self.textbox.message_list.reverse()
            self.textbox.message()
            self.script_a1 = False; self.script_a2 = True
                
        elif self.gob_list[0].is_talking and self.script_a2:
            self.textbox.is_message = True
            self.textbox.make_messages((self.gob_list[0].pos[0],H.pos[1]),"YOU%STILL%HERE$.%WE'LL%BE%LEAVING%SOON", None)
            self.textbox.message_list.reverse()
            self.textbox.message()
            self.script_a2 = False;

        elif self.gob_list[2].is_talking and self.script_b1:
            self.textbox.is_message = True
            self.textbox.make_messages((self.gob_list[2].pos[0],H.pos[1]),"WHERE%DID%ALL%THE%CROWS%GO$", None)
            self.textbox.message_list.reverse()
            self.textbox.message()
            self.script_b1= False


class Battle_gate1(object):
    def __init__(self):
        self.background = battle_gate1
        self.background2 = None
        self.background3 = highland1
        self.background_pos = (-100,-650)
        self.background2_pos = None
        self.background3_pos = (-150,-275)
        self.plat_img = platform1
        self.goblik_total = 1

        self.script_1 = True
        self.textbox = Textbox()
        self.dead_list = []
        self.P = Phalanx((0,0), 0, 0, None)
        self.gob_list = [Shieldlik(i, None) for i in [(400,-400),(500,-400)]] + [Troglik(i, None) for i in [(800,-200)]]
##        self.gob_list = [Goblik(i, None) for i in [(400,-400),(450,-400),(200,-400),(250,-400)]]

        self.map_dict = {'plat_a':{'img_pos':[(200+i*50,-150) for i in range(18)],
                                    'x_range':(200,1050),
                                    'y_range':-150},
                         'plat_b':{'img_pos':[(50+i*50,-50) for i in range(7)],
                                    'x_range':(50,300),
                                    'y_range':-50},
                         'plat_c':{'img_pos':[(300+i*50,50) for i in range(6)],
                                    'x_range':(300,500),
                                    'y_range':50},
                         'plat_d':{'img_pos':[(550+i*50,200) for i in range(12)],
                                    'x_range':(550,1050),
                                    'y_range':200},
                         'plat_e':{'img_pos':[(1000+i*50,350) for i in range(3)],
                                    'x_range':(1000,1050),
                                    'y_range':350},
                         'plat_f':{'img_pos':[(350+i*50,500) for i in range(16)],
                                    'x_range':(350,1050),
                                    'y_range':500},
                          'plat_wall_1':{'img_pos':[(0,1200+i*-50) for i in range(30)],
                                'x_range':(0,0),
                                'y_range':50},
                          'plat_wall_2':{'img_pos':[(300,1200+i*-50) for i in range(26)],
                                'x_range':(300,300),
                                'y_range':50},
                         'plat_wall_3':{'img_pos':[(1100,1200+i*-50) for i in range(30)],
                                'x_range':(1100,1100),
                                'y_range':50}
                         }
        self.wall_dict = {'plat_wall_1':{'x_range':self.map_dict['plat_wall_1']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_1']['y_range']+2400,self.map_dict['plat_wall_1']['y_range']-550)},
                          'plat_wall_2':{'x_range':self.map_dict['plat_wall_2']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_2']['y_range']+2400,self.map_dict['plat_wall_2']['y_range']-200)},
                          'plat_wall_3':{'x_range':self.map_dict['plat_wall_3']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_3']['y_range']+2400,self.map_dict['plat_wall_3']['y_range']-550)},
                          }
        self.climb_dict = {}

    def blit_gobs(self,screen,current_map,H):
        for g in self.gob_list:
            g.shift(current_map,H)
            if not g.back and not g.dead: screen.blit(g.img, g.pos)
            if g.graphic != None: screen.blit(g.graphic, g.graphic_pos)

    def blit_dead_list(self,screen,current_map,H):
        for g in self.gob_list:
            if g.dead: screen.blit(g.img, g.pos)
            elif g.back: screen.blit(g.img, g.pos)

    def blit_platform(self, screen):
        self.plat_map = self.map_dict['plat_a']['img_pos'] +\
                        self.map_dict['plat_b']['img_pos'] +\
                        self.map_dict['plat_c']['img_pos'] +\
                        self.map_dict['plat_d']['img_pos'] +\
                        self.map_dict['plat_e']['img_pos'] +\
                        self.map_dict['plat_f']['img_pos'] +\
                        self.map_dict['plat_wall_1']['img_pos'] +\
                        self.map_dict['plat_wall_2']['img_pos'] +\
                        self.map_dict['plat_wall_3']['img_pos']
                        

        self.wall_dict = {'plat_wall_1':{'x_range':self.map_dict['plat_wall_1']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_1']['y_range']+2400,self.map_dict['plat_wall_1']['y_range']-550)},
                          'plat_wall_2':{'x_range':self.map_dict['plat_wall_2']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_2']['y_range']+2400,self.map_dict['plat_wall_2']['y_range']-200)},
                          'plat_wall_3':{'x_range':self.map_dict['plat_wall_3']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_3']['y_range']+2400,self.map_dict['plat_wall_3']['y_range']-550)},
                          }
        self.climb_dict = {}

        for pos in self.plat_map:
            screen.blit(self.plat_img, pos)

class Map_cave11(object):
    def __init__(self):
        self.background = cave11
        self.background2 = None
        self.background3 = None
        self.background_pos = (0,0)
        self.background2_pos = None
        self.background3_pos = None
        self.plat_img = blank
        self.goblik_total = 1

        self.script_1 = True
        self.textbox = Textbox()
        self.dead_list = []
        self.P = Phalanx((0,0), 0, 0, None)
        self.gob_list = [Shieldlik(i, None) for i in [(400,900)]] + [Troglik(i, None) for i in [(200,900)]]
##        self.gob_list = [Troglik(i, None) for i in [(400,900)]] +\
##                        [Goblik(i, None) for i in [(700,900)]] +\
##                        [Spearlik(i, None) for i in [(800,900)]]

        self.map_dict = {'plat_a':{'img_pos':[(100+i*50,500) for i in range(5)],
                                    'x_range':(100,250),
                                    'y_range':500},
                         'plat_b':{'img_pos':[(300+i*50,650) for i in range(3)],
                                    'x_range':(300,350),
                                    'y_range':650},
                         'plat_c':{'img_pos':[(600+i*50,450) for i in range(7)],
                                    'x_range':(600,900),
                                    'y_range':450},
                         'plat_d':{'img_pos':[(450+i*50,550) for i in range(2)],
                                    'x_range':(450,450),
                                    'y_range':550},
                         'plat_e':{'img_pos':[(550+i*50,500) for i in range(3)],
                                    'x_range':(550,600),
                                    'y_range':500},
                         'plat_f':{'img_pos':[(200+i*50,800) for i in range(2)],
                                    'x_range':(200,200),
                                    'y_range':800},
                         'plat_g':{'img_pos':[(100+i*50,900) for i in range(2)],
                                    'x_range':(100,100),
                                    'y_range':900},
                         'plat_h':{'img_pos':[(200+i*50,1000) for i in range(3)],
                                    'x_range':(200,250),
                                    'y_range':1000},
                         'plat_i':{'img_pos':[(100+i*50,1100) for i in range(3)],
                                    'x_range':(100,150),
                                    'y_range':1100},
                         'plat_j':{'img_pos':[(700+i*50,800) for i in range(5)],
                                    'x_range':(700,850),
                                    'y_range':800},
                         'plat_floor':{'img_pos':[(100+i*50,1200) for i in range(16)],
                                    'x_range':(100,900),
                                    'y_range':1200},
                          'plat_wall_1':{'img_pos':[(50,1200+i*-50) for i in range(24)],
                                'x_range':(50,50),
                                'y_range':50},
                          'plat_wall_2':{'img_pos':[(850,1200+i*-50) for i in range(24)],
                                'x_range':(850,850),
                                'y_range':50}
                         }
        self.wall_dict = {'plat_wall_1':{'x_range':self.map_dict['plat_wall_1']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_1']['y_range']+2400,self.map_dict['plat_wall_1']['y_range']-50)},
                          'plat_wall_2':{'x_range':self.map_dict['plat_wall_2']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_2']['y_range']+2400,self.map_dict['plat_wall_2']['y_range']-50)},
                          }
        self.climb_dict = {}


    def blit_gobs(self,screen,current_map,H):
        for g in self.gob_list:
            g.shift(current_map,H)
            screen.blit(g.img, g.pos)
            if g.graphic != None: screen.blit(g.graphic, g.graphic_pos)
            if g.dead:
                self.dead_list.append(g)
                self.gob_list.remove(g)

    def blit_dead_list(self,screen,current_map,H):
        for g in self.dead_list:
            screen.blit(g.img, g.pos)

    def blit_platform(self, screen):
        self.plat_map = self.map_dict['plat_a']['img_pos'] +\
        self.map_dict['plat_b']['img_pos'] +\
        self.map_dict['plat_c']['img_pos'] +\
        self.map_dict['plat_d']['img_pos'] +\
        self.map_dict['plat_e']['img_pos'] +\
        self.map_dict['plat_f']['img_pos'] +\
        self.map_dict['plat_g']['img_pos'] +\
        self.map_dict['plat_h']['img_pos'] +\
        self.map_dict['plat_i']['img_pos'] +\
        self.map_dict['plat_j']['img_pos'] +\
        self.map_dict['plat_floor']['img_pos'] +\
        self.map_dict['plat_wall_1']['img_pos'] +\
        self.map_dict['plat_wall_2']['img_pos']

        self.wall_dict = {'plat_wall_1':{'x_range':self.map_dict['plat_wall_1']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_1']['y_range']+2400,self.map_dict['plat_wall_1']['y_range']-50)},
                          'plat_wall_2':{'x_range':self.map_dict['plat_wall_2']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_2']['y_range']+2400,self.map_dict['plat_wall_2']['y_range']-50)},
                          }

        self.climb_dict = {}
        
        for pos in self.plat_map:
            screen.blit(self.plat_img, pos)

    def script(self, pos):
        #later on, approach character
        if self.script_1:
            self.textbox.is_message = True
            self.textbox.make_messages(pos,"HEY%BUDDY,%HOWS%IT%GOING$%I%HEARD%WE%WERE%TESTIN'%OUT%SOME%FUNCTIONS!%I%THINK%THIS%PROJECT%IS%GOING%WELL.\nHOW%ABOUT%YOU$", None)
            self.script_1 = False

class Map_one(object):
    def __init__(self):
        self.background = swamp_oil
        self.background_pos = (0,0)
        self.plat_img = platform1
        self.goblik_total = 1
        self.textbox = Textbox()

        self.gob_list = [Goblik(i) for i in [(200,0),(-200,0)]]
        
        self.map_dict = {'plat_a':{'img_pos':[(-200+i*50,500) for i in range(13)],
                                    'x_range':(-200,350),
                                    'y_range':500},
                          'plat_b':{'img_pos':[(500+i*50,400) for i in range(6)],
                                    'x_range':(500,700),
                                    'y_range':400},
                          'plat_c':{'img_pos':[(700+i*50,500) for i in range(9)],
                                    'x_range':(700,1050),
                                    'y_range':500},
                          'plat_d':{'img_pos':[(700+i*50,300) for i in range(9)],
                                    'x_range':(700,1050),
                                    'y_range':300},
                          'plat_e':{'img_pos':[(700+i*50,150) for i in range(9)],
                                    'x_range':(700,1050),
                                    'y_range':150},
                          'plat_f':{'img_pos':[(700+i*50,50) for i in range(9)],
                                    'x_range':(700,1050),
                                    'y_range':50},
                          'plat_wall_1':{'img_pos':[(-200,500+i*-50) for i in range(10)],
                                'x_range':(-200,-200),
                                'y_range':50},
                          'plat_wall_2':{'img_pos':[(1100,500+i*-50) for i in range(10)],
                                'x_range':(1050,1050),
                                'y_range':50},
                          'climb_wall':{'img_pos':[(0+k*50,500+i*-50) for k in range(2) for i in range(10)],
                                        'x_range':(0,0),
                                        'y_range':50}
                          }

        self.wall_dict = {'plat_wall_1':{'x_range':self.map_dict['plat_wall_1']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_1']['y_range']+500,self.map_dict['plat_wall_1']['y_range']-50)},
                          'plat_wall_2':{'x_range':self.map_dict['plat_wall_2']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_2']['y_range']+500,self.map_dict['plat_wall_2']['y_range']-50)},
                          }

        self.climb_dict = {'climb_wall':{'img_pos':self.map_dict['climb_wall']['img_pos'],
                                        'x_range':self.map_dict['climb_wall']['x_range'],
                                        'y_range':(self.map_dict['plat_wall_2']['y_range']+500,self.map_dict['plat_wall_2']['y_range']-50)}
                           }

    def blit_gobs(self, screen, current_map, H):
        for g in self.gob_list:
            g.shift(current_map,H)
            screen.blit(g.img, g.pos)
            if g.graphic != None: screen.blit(g.graphic, g.graphic_pos)

    def blit_platform(self, screen):
        self.plat_map = self.map_dict['plat_a']['img_pos'] +\
        self.map_dict['plat_b']['img_pos'] +\
        self.map_dict['plat_c']['img_pos'] +\
        self.map_dict['plat_d']['img_pos'] +\
        self.map_dict['plat_e']['img_pos'] +\
        self.map_dict['plat_f']['img_pos'] +\
        self.map_dict['plat_wall_1']['img_pos'] +\
        self.map_dict['plat_wall_2']['img_pos'] +\
        self.map_dict['climb_wall']['img_pos']

        self.wall_dict = {'plat_wall_1':{'x_range':self.map_dict['plat_wall_1']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_1']['y_range']+500,self.map_dict['plat_wall_1']['y_range']-50)},
                          'plat_wall_2':{'x_range':self.map_dict['plat_wall_2']['x_range'],
                                         'y_range':(self.map_dict['plat_wall_2']['y_range']+500,self.map_dict['plat_wall_2']['y_range']-50)},
                          }

        self.climb_dict = {'climb_wall':{'img_pos':self.map_dict['climb_wall']['img_pos'],
                                        'x_range':self.map_dict['climb_wall']['x_range'],
                                        'y_range':self.map_dict['climb_wall']['y_range']}
                           }
        
        for pos in self.plat_map:
            screen.blit(self.plat_img, pos)
