from marble_story import *
import random

class Girl(object):
    def __init__(self, pos):
        self.pos = pos
        self.start_pos = pos
        self.dead = False
        self.back = True
        self.graphic = None
        self.graphic_ch = None
        self.ch = 'stand'
        self.face_l = False
        self.face_r = False
        self.stand = True
        self.time = 1
        self.is_talking = False
        self.img = g_turn_l4
        self.s_turn_r = [g_turn_r4,g_turn_r4,g_turn_r4,g_turn_r3,g_turn_r3,g_turn_r3,g_turn_r2,g_turn_r2,g_turn_r2,g_turn_r1,g_turn_r1,g_turn_r1]
        self.r_turn_s = [g_turn_r1,g_turn_r1,g_turn_r1,g_turn_r2,g_turn_r2,g_turn_r2,g_turn_r3,g_turn_r3,g_turn_r3,g_turn_r4,g_turn_r4,g_turn_r4]
        self.s_turn_l = [g_turn_l4,g_turn_l4,g_turn_l4,g_turn_l3,g_turn_l3,g_turn_l3,g_turn_l2,g_turn_l2,g_turn_l2,g_turn_l1,g_turn_l1,g_turn_l1]
        self.l_turn_s = [g_turn_l1,g_turn_l1,g_turn_l1,g_turn_l2,g_turn_l2,g_turn_l2,g_turn_l3,g_turn_l3,g_turn_l3,g_turn_l4,g_turn_l4,g_turn_l4,]
        self.walk_l_list = [g_walk_l5,g_walk_l5,g_walk_l5,g_walk_l4,g_walk_l4,g_walk_l4,g_walk_l3,g_walk_l3,g_walk_l3,g_walk_l2,g_walk_l2,g_walk_l2,g_walk_l1,g_walk_l1,g_walk_l1]
        self.walk_r_list = [g_walk_r5,g_walk_r5,g_walk_r5,g_walk_r4,g_walk_r4,g_walk_r4,g_walk_r3,g_walk_r3,g_walk_r3,g_walk_r2,g_walk_r2,g_walk_r2,g_walk_r1,g_walk_r1,g_walk_r1]
        self.bubble_close = []
        self.bubble_open = [b_open6,b_open6,b_open5,b_open5,b_open4,b_open4,b_open3,b_open3,b_open2,b_open2,b_open1,b_open1]

    def turn_talking(self, H):
        if H.pos[0]+150 < self.pos[0]+150:
            if self.face_r:
                if self.r_turn_s == []:
                    self.img = g_turn_r1
                    self.stand = True; self.face_r = False
                    self.r_turn_s = [g_turn_r1,g_turn_r1,g_turn_r2,g_turn_r2,g_turn_r3,g_turn_r3,g_turn_r4,g_turn_r4]
                else: self.img = self.r_turn_s.pop()
            else: self.img = g_turn_r1
        else:
            if self.face_l:
                if self.l_turn_s == []:
                    self.img = g_turn_l1
                    self.stand = True; self.face_l = False
                    self.l_turn_s = [g_turn_l1,g_turn_l1,g_turn_l2,g_turn_l2,g_turn_l3,g_turn_l3,g_turn_l4,g_turn_l4,]
                else: self.img = self.l_turn_s.pop()
            else: self.img = g_turn_l1

    def shift(self, current_map, H):
        if H.pos[0]+150 > self.pos[0]+50 and H.pos[0]+150 < self.pos[0]+250 and H.is_talking:
            self.is_talking = True
            H.is_talking = False
        else:
            self.time+=1
            if self.time > 150:
                self.time = 1
                if self.ch == 'walk_r' or self.ch == 'walk_l':
                    self.s_turn_r = [g_turn_r4,g_turn_r4,g_turn_r4,g_turn_r3,g_turn_r3,g_turn_r3,g_turn_r2,g_turn_r2,g_turn_r2,g_turn_r1,g_turn_r1,g_turn_r1]
                    self.s_turn_l = [g_turn_l4,g_turn_l4,g_turn_l4,g_turn_l3,g_turn_l3,g_turn_l3,g_turn_l2,g_turn_l2,g_turn_l2,g_turn_l1,g_turn_l1,g_turn_l1]
                    self.walk_r_list = [g_walk_r5,g_walk_r5,g_walk_r5,g_walk_r4,g_walk_r4,g_walk_r4,g_walk_r3,g_walk_r3,g_walk_r3,g_walk_r2,g_walk_r2,g_walk_r2,g_walk_r1,g_walk_r1,g_walk_r1]
                    self.walk_l_list = [g_walk_l5,g_walk_l5,g_walk_l5,g_walk_l4,g_walk_l4,g_walk_l4,g_walk_l3,g_walk_l3,g_walk_l3,g_walk_l2,g_walk_l2,g_walk_l2,g_walk_l1,g_walk_l1,g_walk_l1]
                    self.ch = 'stand'
                else:
                    if self.pos[0]>current_map.map_dict['plat_a']['x_range'][1]-500 :
                        self.ch = 'walk_l'
                    elif self.pos[0]<current_map.map_dict['plat_a']['x_range'][0]+500:
                        self.ch = 'walk_r'
                    else:
                        self.ch = random.choice(['walk_r','walk_l'])

                    
            elif self.ch == 'stand':
                if not self.stand:
                    if self.face_r:
                        if self.r_turn_s == []:
                            self.img = g_turn_r1
                            self.r_turn_s = [g_turn_r1,g_turn_r1,g_turn_r2,g_turn_r2,g_turn_r3,g_turn_r3,g_turn_r4,g_turn_r4]
                            self.stand = True; self.face_r = False; self.face_l = False
                        else: self.img = self.r_turn_s.pop()
                    else:
                        if self.l_turn_s == []:
                            self.img = g_turn_l1
                            self.l_turn_s = [g_turn_l1,g_turn_l1,g_turn_l2,g_turn_l2,g_turn_l3,g_turn_l3,g_turn_l4,g_turn_l4,]
                            self.stand = True; self.face_r = False; self.face_l = False
                        else: self.img = self.l_turn_s.pop()
            elif self.ch == 'walk_r':
                if self.s_turn_r == []:
                    self.face_r = True; self.stand = False
                    if self.walk_r_list == []:
                        self.walk_r_list = [g_walk_r5,g_walk_r5,g_walk_r5,g_walk_r4,g_walk_r4,g_walk_r4,g_walk_r3,g_walk_r3,g_walk_r3,g_walk_r2,g_walk_r2,g_walk_r2,g_walk_r1,g_walk_r1,g_walk_r1]
                    else:
                        self.pos = (self.pos[0]+2, self.pos[1])
                        self.img = self.walk_r_list.pop()
                else: self.img = self.s_turn_r.pop()
            else: 
                if self.s_turn_l == []:
                    self.face_l = True; self.stand = False
                    if self.walk_l_list == []:
                        self.walk_l_list = [g_walk_l5,g_walk_l5,g_walk_l5,g_walk_l4,g_walk_l4,g_walk_l4,g_walk_l3,g_walk_l3,g_walk_l3,g_walk_l2,g_walk_l2,g_walk_l2,g_walk_l1,g_walk_l1,g_walk_l1]
                    else:
                        self.pos = (self.pos[0]-2, self.pos[1])
                        self.img = self.walk_l_list.pop()
                else: self.img = self.s_turn_l.pop()
        self.talking(current_map, H)
                

    def shift_background(self,current_map,x,y):
        
        current_map.background_pos = (current_map.background_pos[0]+x,current_map.background_pos[1]+y)
        if current_map.background2: current_map.background2_pos = (current_map.background2_pos[0]+x/5,current_map.background2_pos[1]+y/5)
        if current_map.background3: current_map.background3_pos = (current_map.background3_pos[0]+x/10,current_map.background3_pos[1]+y/10)
        
        return current_map
                
    def talking(self, current_map, H):
        if self.is_talking:
            if self.pos[1]<250:
                m = 15
                current_map = self.shift_background(current_map, 0, m)
                H.pos = (H.pos[0],H.pos[1]+m)
                for g in current_map.gob_list + current_map.dead_list + current_map.P.gob_list: g.pos = (g.pos[0],g.pos[1]+m) 
                for k in current_map.map_dict.keys():
                    if k in current_map.wall_dict.keys():
                        current_map.wall_dict[k]['y_range'] = (current_map.wall_dict[k]['y_range'][0]+m,current_map.wall_dict[k]['y_range'][1]+m)
                    elif k in current_map.climb_dict.keys():
                        current_map.climb_dict[k]['y_range'] = current_map.climb_dict[k]['y_range']+m
                    else:
                        current_map.map_dict[k]['img_pos'] = [(i[0],i[1]+m) for i in current_map.map_dict[k]['img_pos']]
                        current_map.map_dict[k]['y_range'] = current_map.map_dict[k]['y_range']+m 

        

class People1(object):
    def __init__(self, pos):
        self.pos = pos
        self.dead = False
        self.back = True
        self.graphic = None
        self.graphic_ch = None
        self.face_l = True
        self.face_r = False
        self.is_talking = False
        self.is_waiting = False
        self.img = p1_turning1
        self.l_turn_r = [p1_turning5, p1_turning5, p1_turning5, p1_turning4, p1_turning4, p1_turning4, p1_turning3, p1_turning3, p1_turning3, p1_turning2, p1_turning2, p1_turning2, p1_turning1, p1_turning1, p1_turning1]
        self.r_turn_l = [p1_turning1, p1_turning1, p1_turning1, p1_turning2, p1_turning2, p1_turning2, p1_turning3, p1_turning3, p1_turning3, p1_turning4, p1_turning4, p1_turning4, p1_turning5, p1_turning5, p1_turning5]
        self.confront_l = [p1_con_l9, p1_con_l9, p1_con_l8, p1_con_l8, p1_con_l7, p1_con_l7, p1_con_l6, p1_con_l6, p1_con_l5, p1_con_l5, p1_con_l4, p1_con_l4, p1_con_l3, p1_con_l3, p1_con_l2, p1_con_l2, p1_con_l1, p1_con_l1]
        self.confront_r = [p1_con_r12, p1_con_r12, p1_con_r11, p1_con_r11, p1_con_r10, p1_con_r10, p1_con_r9, p1_con_r9, p1_con_r8, p1_con_r8, p1_con_r7, p1_con_r7, p1_con_r6, p1_con_r6, p1_con_r5, p1_con_r5, p1_con_r4, p1_con_r4, p1_con_r3, p1_con_r3, p1_con_r2, p1_con_r2, p1_con_r1, p1_con_r1]
        self.bubble_close = []
        self.bubble_open = [b_open6,b_open6,b_open5,b_open5,b_open4,b_open4,b_open3,b_open3,b_open2,b_open2,b_open1,b_open1]
        

    def shift(self, current_map, H):
        self.talking(current_map, H)
        
        if H.pos[0]+150 < self.pos[0]+150:
            if self.face_r:
                if self.r_turn_l == []:
                    self.img = p1_turning1
                    self.face_l = True; self.face_r = False
                    self.r_turn_l = [p1_turning1, p1_turning1, p1_turning1, p1_turning2, p1_turning2, p1_turning2, p1_turning3, p1_turning3, p1_turning3, p1_turning4, p1_turning4, p1_turning4, p1_turning5, p1_turning5, p1_turning5]
                else: self.img = self.r_turn_l.pop()
            else: self.img = p1_turning1
        else:
            if self.face_l:
                if self.l_turn_r == []:
                    self.img = p1_turning5
                    self.face_r = True; self.face_l = False
                    self.l_turn_r = [p1_turning5, p1_turning5, p1_turning5, p1_turning4, p1_turning4, p1_turning4, p1_turning3, p1_turning3, p1_turning3, p1_turning2, p1_turning2, p1_turning2, p1_turning1, p1_turning1, p1_turning1]
                else: self.img = self.l_turn_r.pop()
            else: self.img = p1_turning5

        if H.pos[0]+150 > self.pos[0]+50 and H.pos[0]+150 < self.pos[0]+250 and H.is_talking or self.is_talking:
            self.is_talking = True
            if len(self.l_turn_r) == len(self.r_turn_l):
                if self.face_l:
                    if len(self.confront_l) > 0: self.img = self.confront_l.pop()
                else:
                    if len(self.confront_r) > 0: self.img = self.confront_r.pop()

    def shift_background(self,current_map,x,y):
        
        current_map.background_pos = (current_map.background_pos[0]+x,current_map.background_pos[1]+y)
        if current_map.background2: current_map.background2_pos = (current_map.background2_pos[0]+x/5,current_map.background2_pos[1]+y/5)
        if current_map.background3: current_map.background3_pos = (current_map.background3_pos[0]+x/10,current_map.background3_pos[1]+y/10)
        
        return current_map
                
    def talking(self, current_map, H):
        if self.is_talking:
            H.is_talking = False

        else:
            self.confront_l = [p1_con_l9, p1_con_l9, p1_con_l8, p1_con_l8, p1_con_l7, p1_con_l7, p1_con_l6, p1_con_l6, p1_con_l5, p1_con_l5, p1_con_l4, p1_con_l4, p1_con_l3, p1_con_l3, p1_con_l2, p1_con_l2, p1_con_l1, p1_con_l1]
            self.confront_r = [p1_con_r12, p1_con_r12, p1_con_r11, p1_con_r11, p1_con_r10, p1_con_r10, p1_con_r9, p1_con_r9, p1_con_r8, p1_con_r8, p1_con_r7, p1_con_r7, p1_con_r6, p1_con_r6, p1_con_r5, p1_con_r5, p1_con_r4, p1_con_r4, p1_con_r3, p1_con_r3, p1_con_r2, p1_con_r2, p1_con_r1, p1_con_r1]


class People2(object):
    def __init__(self, pos):
        self.pos = pos
        self.dead = False
        self.back = True
        self.graphic = None
        self.graphic_ch = None
        self.face_l = True
        self.face_r = False
        self.is_talking = False
        self.is_waiting = False
        self.img = p1_turning1
        self.l_turn_r = [p2_turning5, p2_turning5, p2_turning5, p2_turning4, p2_turning4, p2_turning4, p2_turning3, p2_turning3, p2_turning3, p2_turning2, p2_turning2, p2_turning2, p2_turning1, p2_turning1, p2_turning1]
        self.r_turn_l = [p2_turning1, p2_turning1, p2_turning1, p2_turning2, p2_turning2, p2_turning2, p2_turning3, p2_turning3, p2_turning3, p2_turning4, p2_turning4, p2_turning4, p2_turning5, p2_turning5, p2_turning5]
        self.confront_l = [p2_con_l8, p2_con_l8, p2_con_l7, p2_con_l7, p2_con_l6, p2_con_l6, p2_con_l5, p2_con_l5, p2_con_l4, p2_con_l4, p2_con_l3, p2_con_l3, p2_con_l2, p2_con_l2, p2_con_l1, p2_con_l1]
        self.confront_r = [p2_con_r6, p2_con_r6, p2_con_r5, p2_con_r5, p2_con_r4, p2_con_r4, p2_con_r3, p2_con_r3, p2_con_r2, p2_con_r2, p2_con_r1, p2_con_r1]
        self.bubble_close = []
        self.bubble_open = [b_open6,b_open6,b_open5,b_open5,b_open4,b_open4,b_open3,b_open3,b_open2,b_open2,b_open1,b_open1]
        

    def shift(self, current_map, H):
        self.talking(current_map, H)
        
        if H.pos[0]+150 < self.pos[0]+150:
            if self.face_r:
                if self.r_turn_l == []:
                    self.img = p2_turning1
                    self.face_l = True; self.face_r = False
                    self.r_turn_l = [p2_turning1, p2_turning1, p2_turning1, p2_turning2, p2_turning2, p2_turning2, p2_turning3, p2_turning3, p2_turning3, p2_turning4, p2_turning4, p2_turning4, p2_turning5, p2_turning5, p2_turning5]
                else: self.img = self.r_turn_l.pop()
            else: self.img = p2_turning1
        else:
            if self.face_l:
                if self.l_turn_r == []:
                    self.img = p2_turning5
                    self.face_r = True; self.face_l = False
                    self.l_turn_r = [p2_turning5, p2_turning5, p2_turning5, p2_turning4, p2_turning4, p2_turning4, p2_turning3, p2_turning3, p2_turning3, p2_turning2, p2_turning2, p2_turning2, p2_turning1, p2_turning1, p2_turning1]
                else: self.img = self.l_turn_r.pop()
            else: self.img = p2_turning5

        if H.pos[0]+150 > self.pos[0]+50 and H.pos[0]+150 < self.pos[0]+250 and H.is_talking or self.is_talking:
            self.is_talking = True
            if len(self.l_turn_r) == len(self.r_turn_l):
                if self.face_l:
                    if len(self.confront_l) > 0: self.img = self.confront_l.pop()
                else:
                    if len(self.confront_r) > 0: self.img = self.confront_r.pop()

    def shift_background(self,current_map,x,y):
        
        current_map.background_pos = (current_map.background_pos[0]+x,current_map.background_pos[1]+y)
        if current_map.background2: current_map.background2_pos = (current_map.background2_pos[0]+x/5,current_map.background2_pos[1]+y/5)
        if current_map.background3: current_map.background3_pos = (current_map.background3_pos[0]+x/10,current_map.background3_pos[1]+y/10)
        
        return current_map
                
    def talking(self, current_map, H):
        if self.is_talking:
            H.is_talking = False

        else:
            self.confront_l = [p2_con_l8, p2_con_l8, p2_con_l7, p2_con_l7, p2_con_l6, p2_con_l6, p2_con_l5, p2_con_l5, p2_con_l4, p2_con_l4, p2_con_l3, p2_con_l3, p2_con_l2, p2_con_l2, p2_con_l1, p2_con_l1]
            self.confront_r = [p2_con_r6, p2_con_r6, p2_con_r5, p2_con_r5, p2_con_r4, p2_con_r4, p2_con_r3, p2_con_r3, p2_con_r2, p2_con_r2, p2_con_r1, p2_con_r1]

class Hinin1(object):
    def __init__(self, pos):
        self.pos = pos
        self.dead = False
        self.back = True
        self.graphic = None
        self.graphic_ch = None
        self.move_list = [p3_stand2,p3_stand3,p3_stand3,p3_stand4,p3_stand5,p3_stand5,p3_stand5,p3_stand5,p3_stand6,p3_stand6,p3_stand6,p3_stand6,p3_stand7,p3_stand7,p3_stand6,p3_stand6,p3_stand5,p3_stand5,p3_stand4,p3_stand4,p3_stand3,p3_stand3,p3_stand2,p3_stand2,p3_stand1,p3_stand1]
        self.is_talking = False
        self.img = p3_stand1

    def shift(self, current_map, H):
        if len(self.move_list)>0 and len(self.move_list)<14: self.img = self.move_list.pop()
        else:
            if H.pos[0]+150 > self.pos[0]+150:
                if self.move_list == []:
                    self.img = p3_stand1
                else: self.img = self.move_list.pop()
            else:
                if self.move_list == []:
                    self.img = p3_stand1
                    self.move_list = [p3_stand2,p3_stand3,p3_stand3,p3_stand4,p3_stand5,p3_stand5,p3_stand5,p3_stand5,p3_stand6,p3_stand6,p3_stand6,p3_stand6,p3_stand7,p3_stand7,p3_stand6,p3_stand6,p3_stand5,p3_stand5,p3_stand4,p3_stand4,p3_stand3,p3_stand3,p3_stand2,p3_stand2,p3_stand1,p3_stand1]
