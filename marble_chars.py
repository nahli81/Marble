from marble_NPC import *


class Phalanx(object):
    def __init__(self, pos, rows, cols, gob_type):
        self.pos = pos
        self.rows = rows
        self.cols = cols
        self.row_pos_list = []
        self.start_x = self.pos[0]
        self.gob_list = []
        self.dead = False
        self.cheer = False
        self.time_limit = random.choice([100,300])
        self.time = 1
        self.marching = False
        
        for y in range(self.cols):
            self.row_pos_list = self.row_pos_list + [(self.start_x+i*20, pos[1]) for i in range(rows)]
            self.start_x += 100
            
        if gob_type == None:
            pass
        elif gob_type == 'spear':
            for pos in self.row_pos_list: self.gob_list.append(Spearlik(pos, True))
        elif gob_type == 'gob':
            for pos in self.row_pos_list: self.gob_list.append(Goblik(pos, True))

    def march(self, H):
        lead = self.gob_list[0].pos[0]
        if any([i.is_phalanx for i in self.gob_list]) == False: self.dead = True
        else:
            self.time += 1
            if H.pos[0]+150 < lead - 500: self.cheer = True
            elif self.time > self.time_limit:
                if self.marching: self.marching = False
                else: self.marching = True
                self.time_limit = random.choice([100,75])
                self.time = 1
            else: self.cheer = False

    def shift_phalanx(self, i, H):
        if i.current_plat == H.current_plat:
            if not i.striking:
                if i.pos[0]+20<H.pos[0]+150 and i.pos[0]+50>H.pos[0]+150:
                    if i.face_l:
                        self.marching = False; i.striking = True; i.ch = None; i.striking_ch = random.choice(['l_1','l_2'])
                    else: i.ch = 'turn'
                elif i.pos[0]+250<H.pos[0]+150 and i.pos[0]+280>H.pos[0]+150:
                    if i.face_r:
                        self.marching = False; i.striking = True; i.ch = None; i.striking_ch = random.choice(['r_1','r_2'])
                    else: i.ch = 'turn'
                else:
                    if self.cheer: i.ch = 'taunt'
                    elif self.marching: i.ch = 'walk'
                    elif H.pos[0]+150>i.pos[0]+150 and i.face_l: i.ch = 'turn'
                    elif H.pos[0]+150<i.pos[0]+150 and i.face_r: i.ch = 'turn'
                    else: i.ch = 'stand'
        else: i.ch = 'stand'
        

class Shieldlik(object):
    def __init__(self, pos, is_phalanx):
        self.pos = pos
        self.img = sh_stand_l6
        self.travelling = False
        self.current_plat = None
        self.falling = True
        self.landing = False
        self.face_r = False
        self.face_l = True
        self.leaping_back = False
        self.taunt = False
        self.striking = False
        self.hitting = False
        self.blocking = False
        self.knock_back = False
        self.turning_r_l = False
        self.turning_l_r = False
        self.dead = False
        self.back = False
        self.idle = False
        self.dying = False
        self.graphic = None
        self.graphic_pos = None
        self.graphic_ch = None
        
        self.time = 1
        self.turn_time = 1
        self.turn_limit = random.choice([400,200,100])
        self.strike_list = []
        self.ch = None
        self.striking_ch = None
        self.hp = 9
        self.hurt = False
        self.dying_ch = None

        self.is_phalanx = is_phalanx

        self.idle_list = [s_idle_7,s_idle_7,s_idle_7,s_idle_6,s_idle_6,s_idle_6,s_idle_5,s_idle_5,s_idle_5,s_idle_4,s_idle_4,s_idle_4,s_idle_3,s_idle_3,s_idle_3,s_idle_2,s_idle_2,s_idle_2,s_idle_1,s_idle_1,s_idle_1]
        
        self.stand_list_l = [sh_stand_l6,sh_stand_l6,sh_stand_l6,sh_stand_l5,sh_stand_l5,sh_stand_l5,sh_stand_l4,sh_stand_l4,sh_stand_l4,sh_stand_l3,sh_stand_l3,sh_stand_l3,sh_stand_l2,sh_stand_l2,sh_stand_l2,sh_stand_l1,sh_stand_l1,sh_stand_l1]
        self.stand_list_r = [sh_stand_r6,sh_stand_r6,sh_stand_r6,sh_stand_r5,sh_stand_r5,sh_stand_r5,sh_stand_r4,sh_stand_r4,sh_stand_r4,sh_stand_r3,sh_stand_r3,sh_stand_r3,sh_stand_r2,sh_stand_r2,sh_stand_r2,sh_stand_r1,sh_stand_r1,sh_stand_r1] 

        self.l_turn_r_list = [s_turning_lr6,s_turning_lr6,s_turning_lr6,s_turning_lr5,s_turning_lr5,s_turning_lr5,s_turning_lr4,s_turning_lr4,s_turning_lr4,s_turning_lr3,s_turning_lr3,s_turning_lr3,s_turning_lr2,s_turning_lr2,s_turning_lr2,s_turning_lr1,s_turning_lr1,s_turning_lr1]
        self.r_turn_l_list = [s_turning_lr1,s_turning_lr1,s_turning_lr1,s_turning_lr2,s_turning_lr2,s_turning_lr2,s_turning_lr3,s_turning_lr3,s_turning_lr3,s_turning_lr4,s_turning_lr4,s_turning_lr4,s_turning_lr5,s_turning_lr5,s_turning_lr5,s_turning_lr6,s_turning_lr6,s_turning_lr6]

        self.start_walking_l = [s_walking_l3,s_walking_l3,s_walking_l3,s_walking_l2,s_walking_l2,s_walking_l2,s_walking_l1,s_walking_l1,s_walking_l1]
        self.start_walking_r = [s_walking_r3,s_walking_r3,s_walking_r3,s_walking_r2,s_walking_r2,s_walking_r2,s_walking_r1,s_walking_r1,s_walking_r1]

        self.walk_l_list = [s_walking_l8,s_walking_l8,s_walking_l8,s_walking_l7,s_walking_l7,s_walking_l7,s_walking_l6,s_walking_l6,s_walking_l6,s_walking_l5,s_walking_l5,s_walking_l5,s_walking_l4,s_walking_l4,s_walking_l4]
        self.walk_r_list = [s_walking_r8,s_walking_r8,s_walking_r8,s_walking_r7,s_walking_r7,s_walking_r7,s_walking_r6,s_walking_r6,s_walking_r6,s_walking_r5,s_walking_r5,s_walking_r5,s_walking_r4,s_walking_r4,s_walking_r4]
        
        self.walk_back_list_l = [s_walking_back_l5,s_walking_back_l5,s_walking_back_l5,s_walking_back_l4,s_walking_back_l4,s_walking_back_l4,s_walking_back_l3,s_walking_back_l3,s_walking_back_l3,s_walking_back_l2,s_walking_back_l2,s_walking_back_l2,s_walking_back_l1,s_walking_back_l1,s_walking_back_l1]
        self.walk_back_list_r = [s_walking_back_r5,s_walking_back_r5,s_walking_back_r5,s_walking_back_r4,s_walking_back_r4,s_walking_back_r4,s_walking_back_r3,s_walking_back_r3,s_walking_back_r3,s_walking_back_r2,s_walking_back_r2,s_walking_back_r2,s_walking_back_r1,s_walking_back_r1,s_walking_back_r1]

        self.jump_strike_l_list = [s_strike1_l5,s_strike1_l5,s_strike1_l5,s_strike1_l4,s_strike1_l4,s_strike1_l4,s_strike1_l3,s_strike1_l3,s_strike1_l3,s_strike1_l2,s_strike1_l2,s_strike1_l2,s_strike1_l1,s_strike1_l1,s_strike1_l1]
        self.strike2_l_list = [s_strike2_l16,s_strike2_l16,s_strike2_l15,s_strike2_l15,s_strike2_l14,s_strike2_l14,s_strike2_l13,s_strike2_l13,s_strike2_l12,s_strike2_l12,s_strike2_l11,s_strike2_l11,s_strike2_l10,s_strike2_l10,s_strike2_l9,s_strike2_l9,s_strike2_l8,s_strike2_l8,s_strike2_l7,s_strike2_l7,s_strike2_l6,s_strike2_l6,s_strike2_l5,s_strike2_l5,s_strike2_l4,s_strike2_l4,s_strike2_l3,s_strike2_l3,s_strike2_l2,s_strike2_l2,s_strike2_l1,s_strike2_l1,s_strike2_l1]
        self.strike3_l_list = [s_strike3_l7,s_strike3_l7,s_strike3_l6,s_strike3_l6,s_strike3_l5,s_strike3_l5,s_strike3_l4,s_strike3_l4,s_strike3_l3,s_strike3_l3,s_strike3_l2,s_strike3_l2,s_strike3_l1,s_strike3_l1]

        self.strike1_r_list = [s_strike1_r8,s_strike1_r8,s_strike1_r7,s_strike1_r7,s_strike1_r6,s_strike1_r6,s_strike1_r5,s_strike1_r5,s_strike1_r4,s_strike1_r4,s_strike1_r3,s_strike1_r3,s_strike1_r2,s_strike1_r2,s_strike1_r1,s_strike1_r1]
        self.strike2_r_list = [s_strike3_r10,s_strike3_r10,s_strike3_r9,s_strike3_r9,s_strike3_r8,s_strike3_r8,s_strike3_r7,s_strike3_r7,s_strike3_r6,s_strike3_r6,s_strike3_r5,s_strike3_r5,s_strike3_r4,s_strike3_r4,s_strike3_r3,s_strike3_r3,s_strike3_r2,s_strike3_r2,s_strike3_r1,s_strike3_r1]
        self.jump_strike_r_list = [s_strike2_r8,s_strike2_r8,s_strike2_r7,s_strike2_r7,s_strike2_r6,s_strike2_r6,s_strike2_r5,s_strike2_r5,s_strike2_r4,s_strike2_r4,s_strike2_r3,s_strike2_r3,s_strike2_r2,s_strike2_r2,s_strike2_r1,s_strike2_r1]

        self.deadl_1_list = [s_death1_l15,s_death1_l15,s_death1_l15,s_death1_l14,s_death1_l14,s_death1_l14,s_death1_l13,s_death1_l13,s_death1_l13,s_death1_l12,s_death1_l12,s_death1_l12,s_death1_l11,s_death1_l11,s_death1_l11,s_death1_l10,s_death1_l10,s_death1_l10,s_death1_l9,s_death1_l9,s_death1_l9,s_death1_l8,s_death1_l8,s_death1_l8,s_death1_l7,s_death1_l7,s_death1_l7,s_death1_l6,s_death1_l6,s_death1_l6,s_death1_l5,s_death1_l5,s_death1_l5,s_death1_l4,s_death1_l4,s_death1_l4,s_death1_l3,s_death1_l3,s_death1_l3,s_death1_l2,s_death1_l2,s_death1_l2,s_death1_l1,s_death1_l1,s_death1_l1]
        self.deadl_2_list = [s_death2_l15,s_death2_l15,s_death2_l15,s_death2_l14,s_death2_l14,s_death2_l14,s_death2_l13,s_death2_l13,s_death2_l13,s_death2_l12,s_death2_l12,s_death2_l12,s_death2_l11,s_death2_l11,s_death2_l11,s_death2_l10,s_death2_l10,s_death2_l10,s_death2_l9,s_death2_l9,s_death2_l9,s_death2_l8,s_death2_l8,s_death2_l8,s_death2_l7,s_death2_l7,s_death2_l7,s_death2_l6,s_death2_l6,s_death2_l6,s_death2_l5,s_death2_l5,s_death2_l5,s_death2_l4,s_death2_l4,s_death2_l4,s_death2_l3,s_death2_l3,s_death2_l3,s_death2_l2,s_death2_l2,s_death2_l2,s_death2_l1,s_death2_l1,s_death2_l1]
        self.deadl_3_list = [s_death3_l17,s_death3_l17,s_death3_l17,s_death3_l16,s_death3_l16,s_death3_l16,s_death3_l15,s_death3_l15,s_death3_l15,s_death3_l14,s_death3_l14,s_death3_l14,s_death3_l13,s_death3_l13,s_death3_l13,s_death3_l12,s_death3_l12,s_death3_l12,s_death3_l11,s_death3_l11,s_death3_l11,s_death3_l10,s_death3_l10,s_death3_l10,s_death3_l9,s_death3_l9,s_death3_l9,s_death3_l8,s_death3_l8,s_death3_l8,s_death3_l7,s_death3_l7,s_death3_l7,s_death3_l6,s_death3_l6,s_death3_l6,s_death3_l5,s_death3_l5,s_death3_l5,s_death3_l4,s_death3_l4,s_death3_l4,s_death3_l3,s_death3_l3,s_death3_l3,s_death3_l2,s_death3_l2,s_death3_l2,s_death3_l1,s_death3_l1,s_death3_l1]

        self.deadr_1_list = [s_death1_r14,s_death1_r14,s_death1_r14,s_death1_r13,s_death1_r13,s_death1_r13,s_death1_r12,s_death1_r12,s_death1_r12,s_death1_r11,s_death1_r11,s_death1_r11,s_death1_r10,s_death1_r10,s_death1_r10,s_death1_r9,s_death1_r9,s_death1_r9,s_death1_r8,s_death1_r8,s_death1_r8,s_death1_r7,s_death1_r7,s_death1_r7,s_death1_r6,s_death1_r6,s_death1_r6,s_death1_r5,s_death1_r5,s_death1_r5,s_death1_r4,s_death1_r4,s_death1_r4,s_death1_r3,s_death1_r3,s_death1_r3,s_death1_r2,s_death1_r2,s_death1_r2,s_death1_r1,s_death1_r1,s_death1_r1]
        self.deadr_2_list = [s_death2_r17,s_death2_r17,s_death2_r17,s_death2_r16,s_death2_r16,s_death2_r16,s_death2_r15,s_death2_r15,s_death2_r15,s_death2_r14,s_death2_r14,s_death2_r14,s_death2_r13,s_death2_r13,s_death2_r13,s_death2_r12,s_death2_r12,s_death2_r12,s_death2_r11,s_death2_r11,s_death2_r11,s_death2_r10,s_death2_r10,s_death2_r10,s_death2_r9,s_death2_r9,s_death2_r9,s_death2_r8,s_death2_r8,s_death2_r8,s_death2_r7,s_death2_r7,s_death2_r7,s_death2_r6,s_death2_r6,s_death2_r6,s_death2_r5,s_death2_r5,s_death2_r5,s_death2_r4,s_death2_r4,s_death2_r4,s_death2_r3,s_death2_r3,s_death2_r3,s_death2_r2,s_death2_r2,s_death2_r2,s_death2_r1,s_death2_r1,s_death2_r1]
        
        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_2]
        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_2]
        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_2]

        self.block_graph1 = [block_graph1_4,block_graph1_3,block_graph1_2,block_graph1_1]
        self.block_graph2 = [block_graph2_4,block_graph2_3,block_graph2_2,block_graph2_1]
        self.block_graph3 = [block_graph3_4,block_graph3_3,block_graph3_2,block_graph3_1]

    def fall(self, current_map):
        y = 2*self.time + self.pos[1]
        self.time += 1
        for k in current_map.map_dict.keys():
            if self.pos[1]+200<current_map.map_dict[k]['y_range'] and self.pos[1]+320>current_map.map_dict[k]['y_range']:
                if self.pos[0]+90<current_map.map_dict[k]['x_range'][1] and self.pos[0]+200>current_map.map_dict[k]['x_range'][0]:
                    y = current_map.map_dict[k]['y_range']-260
                    self.current_plat = k
                    self.falling = False
                    self.landing = True
                    self.time = 1
                    
        self.pos = (self.pos[0], y)

    def regenerate(self):
        self.dying = False; self.dying_ch = None
        
##        self.pos = (random.choice([-200, 500, 1100]), -300)
        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_4]
        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_4]
        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_4]

    def shift(self, current_map, H):

        if self.dying or self.hurt:

            if self.hurt or self.graphic_ch == 'bl1' or self.graphic_ch == 'bl2' or self.graphic_ch == 'bl3':
                if self.graphic_ch == None:

                    self.graphic_ch = random.choice(['bl1','bl2','bl3'])
                if self.graphic_ch == 'bl1':
                    if self.blood_graph1 == []:
                        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_4]
                        self.graphic_ch = None; self.graphic = None; self.hurt = False
                    else: self.graphic = self.blood_graph1.pop()
                elif self.graphic_ch == 'bl2':
                    if self.blood_graph2 == []:
                        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_4]
                        self.graphic_ch = None; self.graphic = None; self.hurt = False
                    else: self.graphic = self.blood_graph2.pop()
                elif self.graphic_ch == 'bl3':
                    if self.blood_graph3 == []:
                        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_4]
                        self.graphic_ch = None; self.graphic = None; self.hurt = False
                    else: self.graphic = self.blood_graph3.pop()
                self.graphic_pos = (self.pos[0]+150, self.pos[1]+110)
                if not self.turning_r_l and not self.turning_l_r:
                    if self.face_r: self.img = s_death1_r3
                    else: self.img = s_death1_l3
                
            if self.dying:
                if self.dying_ch == None:
                    if self.face_l: self.dying_ch = random.choice(['dl1','dl2','dl3'])
                    else: self.dying_ch = random.choice(['dr1','dr2'])
                else:
                    if self.dying_ch == 'dl1':
                        if self.deadl_1_list == []:
                            self.img = s_death1_l15; self.dead = True
                        else: self.img = self.deadl_1_list.pop()
                        
                    elif self.dying_ch == 'dl2':
                        if self.deadl_2_list == []:
                            self.img = s_death2_l15; self.dead = True
                        else: self.img = self.deadl_2_list.pop()

                    elif self.dying_ch == 'dl3':
                        if self.deadl_3_list == []:
                            self.img = s_death3_l17; self.dead = True
                        else: self.img = self.deadl_3_list.pop()
                        
                    elif self.dying_ch == 'dr1':
                        if self.deadr_1_list == []:
                            self.img = s_death1_r14; self.dead = True
                        else: self.img = self.deadr_1_list.pop()
                            
                    elif self.dying_ch == 'dr2':
                        if self.deadr_2_list == []:
                            self.img = s_death2_r17; self.dead = True
                        else: self.img = self.deadr_2_list.pop()
            
        elif self.falling:
            self.fall(current_map)
##            if self.pos[1]>600:
##                self.pos = (200,0)

        elif self.knock_back:
            if self.time > 10: self.time = 1
            if self.face_r:
                if self.time == 10:
                    self.knock_back = False
                    self.time = 1
                else:
                    self.time += 1
                    self.img = s_strike1_r3
                    self.pos = (self.pos[0]-2*self.time**(1/2), self.pos[1])
            else:
                if self.time == 10:
                    self.knock_back = False
                    self.time = 1
                else:
                    self.time += 1
                    self.img = s_strike2_l11
                    self.pos = (self.pos[0]+2*self.time**(1/2), self.pos[1])

            # HURT
        elif H.current_plat == self.current_plat and H.hitting and not H.blocking:
            
            if self.face_r and H.face_l:
                if H.pos[0]+100>self.pos[0]+130 and H.pos[0]+100<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.blocking:
                        self.knock_back = True; H.blocked = True; H.hitting = False
                    else:
                        if self.hp < 1: self.dying = True; self.hurt = True
                        else: self.hp -= 1; self.hurt = True; self.striking = False
            elif self.face_l and H.face_l:
                if H.pos[0]+100>self.pos[0]+130 and H.pos[0]+100<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.hp < 1: self.dying = True; self.hurt = True
                    else: self.hp -= 1; self.hurt = True; self.striking = False
            elif self.face_l and H.face_r:
                if H.pos[0]+300>self.pos[0]+130 and H.pos[0]+300<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.blocking:
                        self.knock_back = True; H.blocked = True; H.hitting = False
                    else:
                        if self.hp < 1: self.dying = True; self.hurt = True
                        else: self.hp -= 1; self.hurt = True; self.striking = False
            elif self.face_r and H.face_r:
                if H.pos[0]+300>self.pos[0]+130 and H.pos[0]+300<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.hp < 1: self.dying = True; self.hurt = True
                    else: self.hp -= 1; self.hurt = True; self.striking = False
                                        
        # ON PLATFORM
        else:
            
            if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:
                
                # HIT THE HERO
                if self.hitting and self.pos[0]+150>H.pos[0]+150 and self.pos[0]<H.pos[0]+180 or +\
                   self.hitting and self.pos[0]+150<H.pos[0]+150 and self.pos[0]+300>H.pos[0]+120:
                    if H.blocking and H.face_r:
                        if self.pos[0]+150<H.pos[0]+150: H.hurt = True; self.hitting = False
                        else: H.knock_back = True;
                    elif H.blocking and H.face_l:
                        if self.pos[0]+150>H.pos[0]+150: H.hurt = True; self.hitting = False
                        else: H.knock_back = True;
                    else: H.hurt = True; self.hitting = False
                            
                # STRIKE!!!
                if self.striking and self.current_plat == H.current_plat:
                    self.blocking = False
                
                    if self.striking_ch == None:
                        if self.face_l:
                            self.striking_ch = random.choice(['s_1','l_1','l_2','w_l','stand_l'])
                        else: self.striking_ch = random.choice(['r_1','r_2','r_j','w_r','stand_r'])
                    else:
                        if self.striking_ch == 's_1':
                            if self.pos[0]+200>current_map.map_dict[self.current_plat]['x_range'][1] and self.face_r:
                                if self.jump_strike_l_list == []:
                                    self.time = 1; self.falling = True
                                    self.jump_strike_l_list = [s_strike1_l5,s_strike1_l5,s_strike1_l5,s_strike1_l4,s_strike1_l4,s_strike1_l4,s_strike1_l3,s_strike1_l3,s_strike1_l3,s_strike1_l2,s_strike1_l2,s_strike1_l2,s_strike1_l1,s_strike1_l1,s_strike1_l1]
                                    self.striking_ch = None; self.striking = False; self.hitting = False
                                else:
                                    self.pos = (self.pos[0]-3,self.pos[1]-(1.5/self.time)**2)
                                    self.time += 1
                                    if len(self.jump_strike_l_list)==3: self.hitting = True
                                    self.img = self.jump_strike_l_list.pop()
                            else: self.striking_ch = 'l_1'
                            
                        elif self.striking_ch == 'l_1':
                            if self.strike2_l_list == []:
                                self.strike2_l_list = [s_strike2_l16,s_strike2_l16,s_strike2_l15,s_strike2_l15,s_strike2_l14,s_strike2_l14,s_strike2_l13,s_strike2_l13,s_strike2_l12,s_strike2_l12,s_strike2_l11,s_strike2_l11,s_strike2_l10,s_strike2_l10,s_strike2_l9,s_strike2_l9,s_strike2_l8,s_strike2_l8,s_strike2_l7,s_strike2_l7,s_strike2_l6,s_strike2_l6,s_strike2_l5,s_strike2_l5,s_strike2_l4,s_strike2_l4,s_strike2_l3,s_strike2_l3,s_strike2_l2,s_strike2_l2,s_strike2_l1,s_strike2_l1,s_strike2_l1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike2_l_list)==3: self.hitting = True
                                elif len(self.strike2_l_list)==15: self.hitting = True
                                self.img = self.strike2_l_list.pop()
                                
                        elif self.striking_ch == 'l_2':
                            if self.strike3_l_list == []:
                                self.time = 1; self.falling = True
                                self.strike3_l_list = [s_strike3_l7,s_strike3_l7,s_strike3_l6,s_strike3_l6,s_strike3_l5,s_strike3_l5,s_strike3_l4,s_strike3_l4,s_strike3_l3,s_strike3_l3,s_strike3_l2,s_strike3_l2,s_strike3_l1,s_strike3_l1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                self.pos = (self.pos[0]-3,self.pos[1]-(1.5/self.time)**2)
                                self.time += 1
                                if len(self.strike3_l_list)==3: self.hitting = True
                                self.img = self.strike3_l_list.pop()

                        elif self.striking_ch == 'w_l':
                            if self.walk_back_list_l == []:
                                self.walk_back_list_l = [s_walking_back_l5,s_walking_back_l5,s_walking_back_l5,s_walking_back_l4,s_walking_back_l4,s_walking_back_l4,s_walking_back_l3,s_walking_back_l3,s_walking_back_l3,s_walking_back_l2,s_walking_back_l2,s_walking_back_l2,s_walking_back_l1,s_walking_back_l1,s_walking_back_l1]
                            if self.time > 40:
                                self.striking_ch = None; self.striking = False; self.hitting = False; self.time = 1
                            else:
                                self.img = self.walk_back_list_l.pop()
                                self.pos = (self.pos[0]+2,self.pos[1])
                                self.time += 1

                        elif self.striking_ch == 'stand_l':
                            if self.stand_list_l == []:
                                self.stand_list_l = [sh_stand_l6,sh_stand_l6,sh_stand_l6,sh_stand_l5,sh_stand_l5,sh_stand_l5,sh_stand_l4,sh_stand_l4,sh_stand_l4,sh_stand_l3,sh_stand_l3,sh_stand_l3,sh_stand_l2,sh_stand_l2,sh_stand_l2,sh_stand_l1,sh_stand_l1,sh_stand_l1]
                            if self.time > 40:
                                self.striking_ch = None; self.striking = False; self.hitting = False; self.time = 1
                            else:
                                self.img = self.stand_list_l.pop()
                                self.time += 1
                            
                        elif self.striking_ch == 'r_1':
                            if self.strike1_r_list == []:
                                self.strike1_r_list = [s_strike1_r8,s_strike1_r8,s_strike1_r7,s_strike1_r7,s_strike1_r6,s_strike1_r6,s_strike1_r5,s_strike1_r5,s_strike1_r4,s_strike1_r4,s_strike1_r3,s_strike1_r3,s_strike1_r2,s_strike1_r2,s_strike1_r1,s_strike1_r1]

                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike1_r_list)==3: self.hitting = True
                                self.img = self.strike1_r_list.pop()

                        elif self.striking_ch == 'r_2': 
                            if self.strike2_r_list == []:
                                self.strike2_r_list = [s_strike3_r10,s_strike3_r10,s_strike3_r9,s_strike3_r9,s_strike3_r8,s_strike3_r8,s_strike3_r7,s_strike3_r7,s_strike3_r6,s_strike3_r6,s_strike3_r5,s_strike3_r5,s_strike3_r4,s_strike3_r4,s_strike3_r3,s_strike3_r3,s_strike3_r2,s_strike3_r2,s_strike3_r1,s_strike3_r1,s_strike3_r1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike2_r_list)==3: self.hitting = True
                                self.img = self.strike2_r_list.pop()

                        elif self.striking_ch == 'r_j':
                            if self.pos[0]+200<current_map.map_dict[self.current_plat]['x_range'][0] and self.face_r:
                                if self.jump_strike_r_list == []:
                                    self.time = 1; self.falling = True
                                    self.jump_strike_r_list = [s_strike2_r8,s_strike2_r8,s_strike2_r7,s_strike2_r7,s_strike2_r6,s_strike2_r6,s_strike2_r5,s_strike2_r5,s_strike2_r4,s_strike2_r4,s_strike2_r3,s_strike2_r3,s_strike2_r2,s_strike2_r2,s_strike2_r2,s_strike2_r1,s_strike2_r1,s_strike2_r1]
                                    self.striking_ch = None; self.striking = False; self.hitting = False
                                else:
                                    self.pos = (self.pos[0]+3,self.pos[1]-(1.5/self.time)**2)
                                    self.time += 1
                                    if len(self.jump_strike_r_list)==3: self.hitting = True
                                    self.img = self.jump_strike_r_list.pop()
                            else: self.striking_ch = 'r_1'

                        elif self.striking_ch == 'w_r':
                            if self.walk_back_list_r == []:
                                self.walk_back_list_r = [s_walking_back_r5,s_walking_back_r5,s_walking_back_r5,s_walking_back_r4,s_walking_back_r4,s_walking_back_r4,s_walking_back_r3,s_walking_back_r3,s_walking_back_r3,s_walking_back_r2,s_walking_back_r2,s_walking_back_r2,s_walking_back_r1,s_walking_back_r1,s_walking_back_r1]
                                if self.time > 40:
                                    self.striking_ch = None; self.striking = False; self.hitting = False; self.time = 1
                            else:
                                self.img = self.walk_back_list_r.pop()
                                self.pos = (self.pos[0]-2,self.pos[1])
                                self.time += 1

                        elif self.striking_ch == 'stand_r':
                            if self.stand_list_r == []:
                                self.stand_list_r = [sh_stand_r6,sh_stand_r6,sh_stand_r6,sh_stand_r5,sh_stand_r5,sh_stand_r5,sh_stand_r4,sh_stand_r4,sh_stand_r4,sh_stand_r3,sh_stand_r3,sh_stand_r3,sh_stand_r2,sh_stand_r2,sh_stand_r2,sh_stand_r1,sh_stand_r1,sh_stand_r1] 
                                if self.time > 40:
                                    self.striking_ch = None; self.striking = False; self.hitting = False; self.time = 1
                            else:
                                self.img = self.stand_list_r.pop()
                                self.time += 1
                            
 
                # IDLE
                else:
                    self.blocking = True
                    # HERO SPOTTED
                    if self.current_plat == H.current_plat:
                        self.back = False
                        if self.idle:
                            if H.pos[0]+150 < self.pos[0]+150:
                                if len(self.r_turn_l_list) < 9 :
                                    self.r_turn_l_list = [s_turning_lr1,s_turning_lr1,s_turning_lr1,s_turning_lr2,s_turning_lr2,s_turning_lr2,s_turning_lr3,s_turning_lr3,s_turning_lr3,s_turning_lr4,s_turning_lr4,s_turning_lr4,s_turning_lr5,s_turning_lr5,s_turning_lr5,s_turning_lr6,s_turning_lr6,s_turning_lr6]
                                    self.face_l; self.idle = False
                                else: self.img = self.r_turn_l_list.pop()
                            elif H.pos[0]+150 > self.pos[0]+150:
                                if len(self.l_turn_r_list) < 9 :
                                    self.l_turn_r_list = [s_turning_lr6,s_turning_lr6,s_turning_lr6,s_turning_lr5,s_turning_lr5,s_turning_lr5,s_turning_lr4,s_turning_lr4,s_turning_lr4,s_turning_lr3,s_turning_lr3,s_turning_lr3,s_turning_lr2,s_turning_lr2,s_turning_lr2,s_turning_lr1,s_turning_lr1,s_turning_lr1]
                                    self.face_r; self.idle = False
                                else: self.img = self.l_turn_r_list.pop()
                        else:
                            # H on left side, strike
                            if self.pos[0]+30<H.pos[0]+150 and self.pos[0]+50>H.pos[0]+150:
                                if self.face_l: self.striking = True; self.ch = None
                                else: self.ch = 'turn'
                            # H on right side, strike
                            elif self.pos[0]+250<H.pos[0]+150 and self.pos[0]+270>H.pos[0]+150:
                                if self.face_r: self.striking = True; self.ch = None
                                else: self.ch = 'turn'
                            elif H.pos[0]+150<self.pos[0]+150:
                                if self.face_r: self.ch = 'turn'
                                else: self.ch = 'walk'
                            elif H.pos[0]+150>self.pos[0]+150:
                                if self.face_l: self.ch = 'turn'
                                else: self.ch = 'walk'
                            else:
                                self.ch = 'walk'
                        
                    else:
                        if H.pos[1] > self.pos[1]: self.back = True
                        self.ch = None
                        #becomes idle
                        if self.idle == False:
                            if self.face_l:
                                if len(self.l_turn_r_list) < 9:
                                    self.idle = True
                                else: self.img = self.l_turn_r_list.pop()
                            if self.face_r:
                                if len(self.r_turn_l_list) < 9:
                                    self.idle = True
                                else: self.img = self.r_turn_l_list.pop()
                        else:
                            self.r_turn_l_list = [s_turning_lr1,s_turning_lr1,s_turning_lr1,s_turning_lr2,s_turning_lr2,s_turning_lr2,s_turning_lr3,s_turning_lr3,s_turning_lr3]
                            self.l_turn_r_list = [s_turning_lr6,s_turning_lr6,s_turning_lr6,s_turning_lr5,s_turning_lr5,s_turning_lr5,s_turning_lr4,s_turning_lr4,s_turning_lr4]

                            if self.idle_list == []:
                                self.idle_list = [s_idle_7,s_idle_7,s_idle_7,s_idle_6,s_idle_6,s_idle_6,s_idle_5,s_idle_5,s_idle_5,s_idle_4,s_idle_4,s_idle_4,s_idle_3,s_idle_3,s_idle_3,s_idle_2,s_idle_2,s_idle_2,s_idle_1,s_idle_1,s_idle_1]
                            else: self.img = self.idle_list.pop()
                    
                    if self.ch == 'walk':
                        if self.current_plat != H.current_plat:
                            if self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][1] and self.face_r or +\
                                self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][0] and self.face_l:
                                self.ch = random.choice(['stand','turn'])

                        else:
                            if self.face_l:
                                if self.start_walking_l == []:
                                    if self.walk_l_list == []:
                                        self.walk_l_list = [s_walking_l8,s_walking_l8,s_walking_l8,s_walking_l7,s_walking_l7,s_walking_l7,s_walking_l6,s_walking_l6,s_walking_l6,s_walking_l5,s_walking_l5,s_walking_l5,s_walking_l4,s_walking_l4,s_walking_l4]
                                    else: self.img = self.walk_l_list.pop()
                                else: self.img = self.start_walking_l.pop()
                                self.pos = (self.pos[0]-2, self.pos[1])
                            else:
                                if self.start_walking_r == []:
                                    if self.walk_r_list == []:
                                        self.walk_r_list = [s_walking_r8,s_walking_r8,s_walking_r8,s_walking_r7,s_walking_r7,s_walking_r7,s_walking_r6,s_walking_r6,s_walking_r6,s_walking_r5,s_walking_r5,s_walking_r5,s_walking_r4,s_walking_r4,s_walking_r4]
                                    else: self.img = self.walk_r_list.pop()
                                else: self.img = self.start_walking_r.pop()
                                self.pos = (self.pos[0]+2,self.pos[1])
                            
                    elif self.ch == 'stand':
                        if self.face_l:
                            if self.stand_list_l == []:
                                self.stand_list_l = [sh_stand_l6,sh_stand_l6,sh_stand_l6,sh_stand_l5,sh_stand_l5,sh_stand_l5,sh_stand_l4,sh_stand_l4,sh_stand_l4,sh_stand_l3,sh_stand_l3,sh_stand_l3,sh_stand_l2,sh_stand_l2,sh_stand_l2,sh_stand_l1,sh_stand_l1,sh_stand_l1]
                            else: self.img = self.stand_list_l.pop()
                        else:
                            if self.stand_list_r == []:
                                self.stand_list_r = [sh_stand_r6,sh_stand_r6,sh_stand_r6,sh_stand_r5,sh_stand_r5,sh_stand_r5,sh_stand_r4,sh_stand_r4,sh_stand_r4,sh_stand_r3,sh_stand_r3,sh_stand_r3,sh_stand_r2,sh_stand_r2,sh_stand_r2,sh_stand_r1,sh_stand_r1,sh_stand_r1] 
                            else: self.img = self.stand_list_r.pop()

                    elif self.ch == 'turn':
                        if self.face_l:
                            if self.l_turn_r_list == []:
                                self.start_walking_l = [s_walking_l3,s_walking_l3,s_walking_l3,s_walking_l2,s_walking_l2,s_walking_l2,s_walking_l1,s_walking_l1,s_walking_l1]
                                self.r_turn_l_list = [s_turning_lr1,s_turning_lr1,s_turning_lr1,s_turning_lr2,s_turning_lr2,s_turning_lr2,s_turning_lr3,s_turning_lr3,s_turning_lr3,s_turning_lr4,s_turning_lr4,s_turning_lr4,s_turning_lr5,s_turning_lr5,s_turning_lr5,s_turning_lr6,s_turning_lr6,s_turning_lr6]
                                self.ch = random.choice(['walk','stand'])
                                self.face_r = True; self.face_l = False
                            else: self.img = self.l_turn_r_list.pop()
                        else:
                            if self.r_turn_l_list == []:
                                self.start_walking_r = [s_walking_r3,s_walking_r3,s_walking_r3,s_walking_r2,s_walking_r2,s_walking_r2,s_walking_r1,s_walking_r1,s_walking_r1]
                                self.l_turn_r_list = [s_turning_lr6,s_turning_lr6,s_turning_lr6,s_turning_lr5,s_turning_lr5,s_turning_lr5,s_turning_lr4,s_turning_lr4,s_turning_lr4,s_turning_lr3,s_turning_lr3,s_turning_lr3,s_turning_lr2,s_turning_lr2,s_turning_lr2,s_turning_lr1,s_turning_lr1,s_turning_lr1]
                                self.ch = random.choice(['walk','stand'])
                                self.face_r = False; self.face_l = True
                            else: self.img = self.r_turn_l_list.pop()       
                self.turn_time += 1
            else:
                self.falling = True
        

class Troglik(object):
    def __init__(self, pos, is_phalanx):
        self.pos = pos
        self.img = t_stand_l5
        self.travelling = False
        self.current_plat = None
        self.falling = True
        self.landing = False
        self.face_r = False
        self.face_l = True
        self.leaping_back = False
        self.taunt = False
        self.striking = False
        self.hitting = False
        self.blocking = False
        self.knock_back = False
        self.turning_r_l = False
        self.turning_l_r = False
        self.dead = False
        self.back = False
        self.dying = False
        self.graphic = None
        self.graphic_pos = None
        self.graphic_ch = None
        
        self.time = 1
        self.turn_time = 1
        self.turn_limit = random.choice([400,200,100])
        self.strike_list = []
        self.ch = 'stand'
        self.striking_ch = None
        self.hp = 9
        self.hurt = False
        self.dying_ch = None

        self.is_phalanx = is_phalanx

        self.stand_list_l = [t_stand_l5,t_stand_l5,t_stand_l5,t_stand_l4,t_stand_l4,t_stand_l4,t_stand_l3,t_stand_l3,t_stand_l3,t_stand_l2,t_stand_l2,t_stand_l2,t_stand_l1,t_stand_l1,t_stand_l1]
        self.stand_list_r = [t_stand_r5,t_stand_r5,t_stand_r5,t_stand_r4,t_stand_r4,t_stand_r4,t_stand_r3,t_stand_r3,t_stand_r3,t_stand_r2,t_stand_r2,t_stand_r2,t_stand_r1,t_stand_r1,t_stand_r1] 

        self.l_turn_r_list = [t_turning4,t_turning4,t_turning3,t_turning3,t_turning2,t_turning2,t_turning1,t_turning1]
        self.r_turn_l_list = [t_turning8,t_turning8,t_turning7,t_turning7,t_turning6,t_turning6,t_turning5,t_turning5]

        self.start_walking_l = [t_walk_l3,t_walk_l3,t_walk_l3,t_walk_l2,t_walk_l2,t_walk_l2,t_walk_l1,t_walk_l1,t_walk_l1]
        self.start_walking_r = [t_walk_r3,t_walk_r3,t_walk_r3,t_walk_r2,t_walk_r2,t_walk_r2,t_walk_r1,t_walk_r1,t_walk_r1]

        self.walk_l_list = [t_walk_l8,t_walk_l8,t_walk_l8,t_walk_l7,t_walk_l7,t_walk_l7,t_walk_l6,t_walk_l6,t_walk_l6,t_walk_l5,t_walk_l5,t_walk_l5,t_walk_l4,t_walk_l4,t_walk_l4,]
        self.walk_r_list = [t_walk_r8,t_walk_r8,t_walk_r8,t_walk_r7,t_walk_r7,t_walk_r7,t_walk_r6,t_walk_r6,t_walk_r6,t_walk_r5,t_walk_r5,t_walk_r5,t_walk_r4,t_walk_r4,t_walk_r4]
        
        self.leap_back_list_l = [t_jump_left5,t_jump_left5,t_jump_left4,t_jump_left4,t_jump_left3,t_jump_left3,t_jump_left2,t_jump_left2,t_jump_left1,t_jump_left1]
        self.leap_back_list_r = [t_jump_right5,t_jump_right5,t_jump_right4,t_jump_right4,t_jump_right3,t_jump_right3,t_jump_right2,t_jump_right2,t_jump_right1,t_jump_right1]

        self.jump_strike_l_list = [t_strike1_l10,t_strike1_l10,t_strike1_l9,t_strike1_l9,t_strike1_l8,t_strike1_l8,t_strike1_l7,t_strike1_l7,t_strike1_l6,t_strike1_l6,t_strike1_l5,t_strike1_l5,t_strike1_l4,t_strike1_l4,t_strike1_l3,t_strike1_l3,t_strike1_l2,t_strike1_l2,t_strike1_l1,t_strike1_l1]
        self.strike2_l_list = [t_strike2_l10,t_strike2_l10,t_strike2_l9,t_strike2_l9,t_strike2_l8,t_strike2_l8,t_strike2_l7,t_strike2_l7,t_strike2_l6,t_strike2_l6,t_strike2_l5,t_strike2_l5,t_strike2_l4,t_strike2_l4,t_strike2_l3,t_strike2_l3,t_strike2_l2,t_strike2_l2,t_strike2_l1,t_strike2_l1]
        self.strike3_l_list = [t_strike3_l11,t_strike3_l11,t_strike3_l10,t_strike3_l10,t_strike3_l9,t_strike3_l9,t_strike3_l8,t_strike3_l8,t_strike3_l7,t_strike3_l7,t_strike3_l6,t_strike3_l6,t_strike3_l5,t_strike3_l5,t_strike3_l4,t_strike3_l4,t_strike3_l3,t_strike3_l3,t_strike3_l2,t_strike3_l2,t_strike3_l1,t_strike3_l1]
        self.strike4_l_list = [t_strike4_l10,t_strike4_l10,t_strike4_l9,t_strike4_l9,t_strike4_l8,t_strike4_l8,t_strike4_l7,t_strike4_l7,t_strike4_l6,t_strike4_l6,t_strike4_l5,t_strike4_l5,t_strike4_l4,t_strike4_l4,t_strike4_l3,t_strike4_l3,t_strike4_l2,t_strike4_l2,t_strike4_l1,t_strike4_l1]
        self.drop_strike_l = [t_strike4_l10,t_strike4_l10,t_strike4_l9,t_strike4_l9,t_strike4_l8,t_strike4_l8]
        self.swing_l = [t_strike4_l5,t_strike4_l5,t_strike4_l4,t_strike4_l4,t_strike4_l3,t_strike4_l3,t_strike4_l2,t_strike4_l2,t_strike4_l1,t_strike4_l1]

        self.strike1_r_list = [t_strike1_r9,t_strike1_r9,t_strike1_r8,t_strike1_r8,t_strike1_r7,t_strike1_r7,t_strike1_r6,t_strike1_r6,t_strike1_r5,t_strike1_r5,t_strike1_r4,t_strike1_r4,t_strike1_r3,t_strike1_r3,t_strike1_r2,t_strike1_r2,t_strike1_r1,t_strike1_r1]
        self.strike2_r_list = [t_strike3_r7,t_strike3_r7,t_strike3_r6,t_strike3_r6,t_strike3_r5,t_strike3_r5,t_strike3_r4,t_strike3_r4,t_strike3_r3,t_strike3_r3,t_strike3_r2,t_strike3_r2,t_strike3_r1,t_strike3_r1]
        self.strike3_r_list = [t_strike2_r13,t_strike2_r13,t_strike2_r12,t_strike2_r12,t_strike2_r11,t_strike2_r11,t_strike2_r10,t_strike2_r10,t_strike2_r9,t_strike2_r9,t_strike2_r8,t_strike2_r8,t_strike2_r7,t_strike2_r7,t_strike2_r6,t_strike2_r6,t_strike2_r5,t_strike2_r5,t_strike2_r4,t_strike2_r4,t_strike2_r3,t_strike2_r3,t_strike2_r2,t_strike2_r2,t_strike2_r1,t_strike2_r1]
        self.drop_strike_r = [t_strike2_r13,t_strike2_r13,t_strike2_r12,t_strike2_r12,t_strike2_r11,t_strike2_r11,t_strike2_r10,t_strike2_r10]
        self.swing_r = [t_strike2_r6,t_strike2_r6,t_strike2_r5,t_strike2_r5,t_strike2_r4,t_strike2_r4,t_strike2_r3,t_strike2_r3,t_strike2_r2,t_strike2_r2,t_strike2_r1,t_strike2_r1]

        self.block_l_list = [t_strike4_l8,t_strike4_l8,t_strike4_l7,t_strike4_l7,t_strike4_l6,t_strike4_l6]
        self.block_r_list = [t_strike2_r7,t_strike2_r7,t_strike2_r8,t_strike2_r8,t_strike2_r9,t_strike2_r9]

        self.deadl_1_list = [t_death1_l13,t_death1_l13,t_death1_l12,t_death1_l12,t_death1_l11,t_death1_l11,t_death1_l10,t_death1_l10,t_death1_l9,t_death1_l9,t_death1_l8,t_death1_l8,t_death1_l7,t_death1_l7,t_death1_l6,t_death1_l6,t_death1_l5,t_death1_l5,t_death1_l4,t_death1_l4,t_death1_l3,t_death1_l3,t_death1_l2,t_death1_l2,t_death1_l1,t_death1_l1]
        self.deadl_2_list = [t_death2_l11,t_death2_l11,t_death2_l10,t_death2_l10,t_death2_l9,t_death2_l9,t_death2_l8,t_death2_l8,t_death2_l7,t_death2_l7,t_death2_l6,t_death2_l6,t_death2_l5,t_death2_l5,t_death2_l4,t_death2_l4,t_death2_l3,t_death2_l3,t_death2_l2,t_death2_l2,t_death2_l1,t_death2_l1]

        self.deadr_1_list = [t_death1_r14,t_death1_r14,t_death1_r13,t_death1_r13,t_death1_r12,t_death1_r12,t_death1_r11,t_death1_r11,t_death1_r10,t_death1_r10,t_death1_r9,t_death1_r9,t_death1_r8,t_death1_r8,t_death1_r7,t_death1_r7,t_death1_r6,t_death1_r6,t_death1_r5,t_death1_r5,t_death1_r4,t_death1_r4,t_death1_r3,t_death1_r3,t_death1_r2,t_death1_r2,t_death1_r1,t_death1_r1]
        self.deadr_2_list = [t_death2_r11,t_death2_r11,t_death2_r10,t_death2_r10,t_death2_r9,t_death2_r9,t_death2_r8,t_death2_r8,t_death2_r7,t_death2_r7,t_death2_r6,t_death2_r6,t_death2_r5,t_death2_r5,t_death2_r4,t_death2_r4,t_death2_r3,t_death2_r3,t_death2_r2,t_death2_r2,t_death2_r1,t_death2_r1]
        
        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_2]
        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_2]
        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_2]

        self.block_graph1 = [block_graph1_4,block_graph1_3,block_graph1_2,block_graph1_1]
        self.block_graph2 = [block_graph2_4,block_graph2_3,block_graph2_2,block_graph2_1]
        self.block_graph3 = [block_graph3_4,block_graph3_3,block_graph3_2,block_graph3_1]
        
    def fall(self, current_map):
        y = 2*self.time + self.pos[1]
        self.time += 1
        for k in current_map.map_dict.keys():
            if self.pos[1]+200<current_map.map_dict[k]['y_range'] and self.pos[1]+320>current_map.map_dict[k]['y_range']:
                if self.pos[0]+90<current_map.map_dict[k]['x_range'][1] and self.pos[0]+200>current_map.map_dict[k]['x_range'][0]:
                    y = current_map.map_dict[k]['y_range']-260
                    self.current_plat = k
                    self.falling = False
                    self.landing = True
                    self.time = 1
                    
        self.pos = (self.pos[0], y)

    def regenerate(self):
        self.dying = False; self.dying_ch = None
        
##        self.pos = (random.choice([-200, 500, 1100]), -300)
        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_4]
        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_4]
        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_4]

    def shift(self, current_map, H):

        if self.dying or self.hurt:

            if self.hurt or self.graphic_ch == 'bl1' or self.graphic_ch == 'bl2' or self.graphic_ch == 'bl3':
                if self.graphic_ch == None:
                    self.graphic_ch = random.choice(['bl1','bl2'])
                if self.graphic_ch == 'bl1':
                    if self.blood_graph1 == []:
                        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_4]
                        self.graphic_ch = None; self.graphic = None; self.hurt = False
                    else: self.graphic = self.blood_graph1.pop()
                elif self.graphic_ch == 'bl2':
                    if self.blood_graph2 == []:
                        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_4]
                        self.graphic_ch = None; self.graphic = None; self.hurt = False
                    else: self.graphic = self.blood_graph2.pop()
                elif self.graphic_ch == 'bl3':
                    if self.blood_graph3 == []:
                        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_4]
                        self.graphic_ch = None; self.graphic = None; self.hurt = False
                    else: self.graphic = self.blood_graph3.pop()
                self.graphic_pos = (self.pos[0]+150, self.pos[1]+110)
                if self.face_r: self.img = t_death1_r2
                else: self.img = t_death1_l2
                
            if self.dying:
                if self.dying_ch == None:
                    if self.face_l: self.dying_ch = random.choice(['dl1','dl2'])
                    else: self.dying_ch = random.choice(['dr1','dr2'])
                else:
                    if self.dying_ch == 'dl1':
                        if self.deadl_1_list == []:
                            self.img = t_death1_l13; self.dead = True
                        else: self.img = self.deadl_1_list.pop()
                        
                    elif self.dying_ch == 'dl2':
                        if self.deadl_2_list == []:
                            self.img = t_death2_l11; self.dead = True
                        else: self.img = self.deadl_2_list.pop()
                        
                    elif self.dying_ch == 'dr1':
                        if self.deadr_1_list == []:
                            self.img = t_death1_r14; self.dead = True
                        else: self.img = self.deadr_1_list.pop()
                            
                    elif self.dying_ch == 'dr2':
                        if self.deadr_2_list == []:
                            self.img = t_death2_r11; self.dead = True
                        else: self.img = self.deadr_2_list.pop()
            
        elif self.falling:
            self.fall(current_map)
##            if self.pos[1]>600:
##                self.pos = (200,0)
            
            # HURT
        elif H.current_plat == self.current_plat and H.hitting and not H.blocking:
            
            if self.face_r and H.face_l:
                if H.pos[0]+100>self.pos[0]+130 and H.pos[0]+100<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.blocking:
                        self.knock_back = True; H.blocked = True; H.hitting = False
                    else:
                        if self.hp < 1: self.dying = True; self.hurt = True
                        else: self.hp -= 1; self.hurt = True; self.striking = False
            elif self.face_l and H.face_l:
                if H.pos[0]+100>self.pos[0]+130 and H.pos[0]+100<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.hp < 1: self.dying = True; self.hurt = True
                    else: self.hp -= 1; self.hurt = True; self.striking = False
            elif self.face_l and H.face_r:
                if H.pos[0]+300>self.pos[0]+130 and H.pos[0]+300<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.blocking:
                        self.knock_back = True; H.blocked = True; H.hitting = False
                    else:
                        if self.hp < 1: self.dying = True; self.hurt = True
                        else: self.hp -= 1; self.hurt = True; self.striking = False
            elif self.face_r and H.face_r:
                if H.pos[0]+300>self.pos[0]+130 and H.pos[0]+300<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.hp < 1: self.dying = True; self.hurt = True
                    else: self.hp -= 1; self.hurt = True; self.striking = False
                                        
        # ON PLATFORM
        else:
            
            if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:

                # HIT THE HERO
                if self.hitting and self.pos[0]+150>H.pos[0]+150 and self.pos[0]<H.pos[0]+180 or +\
                   self.hitting and self.pos[0]+150<H.pos[0]+150 and self.pos[0]+300>H.pos[0]+120:
                    if H.blocking and H.face_r:
                        if self.pos[0]+150<H.pos[0]+150: H.hurt = True
                        else: H.knock_back = True;
                    elif H.blocking and H.face_l:
                        if self.pos[0]+150>H.pos[0]+150: H.hurt = True
                        else: H.knock_back = True;
                    else: H.hurt = True
                            
                # STRIKE!!!
                if self.striking and self.current_plat == H.current_plat:
                    if self.striking_ch == None:
                        if self.face_l:
                            self.striking_ch = random.choice(['s_1','l_1','l_2','l_3','b_l','leap_l','leap_l'])
                        else: self.striking_ch = random.choice(['r_1','r_2','r_3','b_r','leap_r','leap_r'])
                    else:
                        if self.striking_ch == 's_1':
                            if self.pos[0]+200>current_map.map_dict[self.current_plat]['x_range'][1] and self.face_r:
                                if self.jump_strike_l_list == []:
                                    self.time = 1; self.falling = True
                                    self.jump_strike_l_list = [t_strike1_l10,t_strike1_l10,t_strike1_l9,t_strike1_l9,t_strike1_l8,t_strike1_l8,t_strike1_l7,t_strike1_l7,t_strike1_l6,t_strike1_l6,t_strike1_l5,t_strike1_l5,t_strike1_l4,t_strike1_l4,t_strike1_l3,t_strike1_l3,t_strike1_l2,t_strike1_l2,t_strike1_l1,t_strike1_l1]
                                    self.striking_ch = None; self.striking = False; self.hitting = False
                                else:
                                    self.pos = (self.pos[0]-3,self.pos[1]-(1.5/self.time)**2)
                                    self.time += 1
                                    if len(self.jump_strike_l_list)==3: self.hitting = True
                                    self.img = self.jump_strike_l_list.pop()
                            else: self.striking_ch = 'l_1'
                        elif self.striking_ch == 'l_1':
                            if self.strike2_l_list == []:
                                self.strike2_l_list = [t_strike2_l10,t_strike2_l10,t_strike2_l9,t_strike2_l9,t_strike2_l8,t_strike2_l8,t_strike2_l7,t_strike2_l7,t_strike2_l6,t_strike2_l6,t_strike2_l5,t_strike2_l5,t_strike2_l4,t_strike2_l4,t_strike2_l3,t_strike2_l3,t_strike2_l2,t_strike2_l2,t_strike2_l1,t_strike2_l1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike2_l_list)==3: self.hitting = True
                                self.img = self.strike2_l_list.pop()
                        elif self.striking_ch == 'l_2':
                            if self.strike3_l_list == []:
                                self.strike3_l_list = [t_strike3_l11,t_strike3_l11,t_strike3_l10,t_strike3_l10,t_strike3_l9,t_strike3_l9,t_strike3_l8,t_strike3_l8,t_strike3_l7,t_strike3_l7,t_strike3_l6,t_strike3_l6,t_strike3_l5,t_strike3_l5,t_strike3_l4,t_strike3_l4,t_strike3_l3,t_strike3_l3,t_strike3_l2,t_strike3_l2,t_strike3_l1,t_strike3_l1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike3_l_list)==3: self.hitting = True
                                self.img = self.strike3_l_list.pop()
                        elif self.striking_ch == 'l_3':
                            if self.strike4_l_list == []:
                                self.strike4_l_list = [t_strike4_l10,t_strike4_l10,t_strike4_l9,t_strike4_l9,t_strike4_l8,t_strike4_l8,t_strike4_l7,t_strike4_l7,t_strike4_l6,t_strike4_l6,t_strike4_l5,t_strike4_l5,t_strike4_l4,t_strike4_l4,t_strike4_l3,t_strike4_l3,t_strike4_l2,t_strike4_l2,t_strike4_l1,t_strike4_l1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike4_l_list)==3: self.hitting = True
                                self.img = self.strike4_l_list.pop()
                                
                        elif self.striking_ch == 'leap_l':
                            if self.pos[0]<current_map.map_dict[self.current_plat]['x_range'][0]+50:
                                if self.leap_back_list_l == []:
                                    self.time = 1; self.falling = True
                                    self.leap_back_list_l = [t_jump_left5,t_jump_left5,t_jump_left4,t_jump_left4,t_jump_left3,t_jump_left3,t_jump_left2,t_jump_left2,t_jump_left1,t_jump_left1]
                                    self.striking_ch = None; self.striking = False
                                else:
                                    self.pos = (self.pos[0]+7,self.pos[1]-(1.5/self.time)**2)
                                    self.time += 1
                                    self.img = self.leap_back_list_l.pop()
                            else: self.striking_ch = None; self.striking = False
                            
                        elif self.striking_ch == 'b_l':
                            if self.swing_l == []:
                                if self.block_l_list == []:
                                    self.block_l_list = [t_strike4_l6,t_strike4_l6,t_strike4_l7,t_strike4_l7,t_strike4_l8,t_strike4_l8]
                                elif self.time < 45:
                                    self.blocking = True
                                    self.time += 1
                                    self.img = self.block_l_list.pop()
                                    if self.knock_back:
                                        if self.time > 10: self.time = 1
                                        elif self.time == 10:
                                            self.knock_back = False
                                            self.time = 1
                                        else:
                                            self.time += 1
                                            self.pos = (self.pos[0]+2*self.time**(1/2), self.pos[1])
                                else:
                                    self.blocking = False
                                    if self.drop_strike_l == []:
                                        self.striking_ch = None; self.striking = False; self.hitting = False; self.time = 1
                                        self.swing_l = [t_strike4_l5,t_strike4_l5,t_strike4_l4,t_strike4_l4,t_strike4_l3,t_strike4_l3,t_strike4_l2,t_strike4_l2,t_strike4_l1,t_strike4_l1]
                                        self.drop_strike_l = [t_strike4_l10,t_strike4_l10,t_strike4_l9,t_strike4_l9,t_strike4_l8,t_strike4_l8]
                                    else:
                                        if len(self.drop_strike_l)==3: self.hitting = True
                                        self.img = self.drop_strike_l.pop()
                            else: self.img = self.swing_l.pop()
                            
                        elif self.striking_ch == 'r_1':
                            if self.strike1_r_list == []:
                                self.strike1_r_list = [t_strike1_r9,t_strike1_r9,t_strike1_r8,t_strike1_r8,t_strike1_r7,t_strike1_r7,t_strike1_r6,t_strike1_r6,t_strike1_r5,t_strike1_r5,t_strike1_r4,t_strike1_r4,t_strike1_r3,t_strike1_r3,t_strike1_r2,t_strike1_r2,t_strike1_r1,t_strike1_r1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike1_r_list)==3: self.hitting = True
                                self.img = self.strike1_r_list.pop()
                            
                        elif self.striking_ch == 'r_2':
                            if self.pos[0]+100<current_map.map_dict[self.current_plat]['x_range'][0] and self.face_l:
                                if self.strike2_r_list == []:
                                    self.strike2_r_list = [t_strike3_r7,t_strike3_r7,t_strike3_r6,t_strike3_r6,t_strike3_r5,t_strike3_r5,t_strike3_r4,t_strike3_r4,t_strike3_r3,t_strike3_r3,t_strike3_r2,t_strike3_r2,t_strike3_r1,t_strike3_r1]
                                    self.striking_ch = None; self.striking = False; self.hitting = False
                                else:
                                    self.time += 1
                                    self.pos = (self.pos[0]+3,self.pos[1]-(1.5/self.time)**2)
                                    if len(self.strike2_r_list)==3: self.hitting = True
                                    self.img = self.strike2_r_list.pop()
                            else: self.striking_ch = 'r_1'
                        elif self.striking_ch == 'r_3':
                            if self.strike3_r_list == []:
                                self.time = 1; self.falling = True
                                self.strike3_r_list = [t_strike2_r13,t_strike2_r13,t_strike2_r12,t_strike2_r12,t_strike2_r11,t_strike2_r11,t_strike2_r10,t_strike2_r10,t_strike2_r9,t_strike2_r9,t_strike2_r8,t_strike2_r8,t_strike2_r7,t_strike2_r7,t_strike2_r6,t_strike2_r6,t_strike2_r5,t_strike2_r5,t_strike2_r4,t_strike2_r4,t_strike2_r3,t_strike2_r3,t_strike2_r2,t_strike2_r2,t_strike2_r1,t_strike2_r1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike3_r_list)==3: self.hitting = True
                                self.img = self.strike3_r_list.pop()
                        elif self.striking_ch == 'b_r':
                            if self.swing_r == []:
                                if self.block_r_list == []:
                                    self.block_r_list = [t_strike2_r9,t_strike2_r9,t_strike2_r8,t_strike2_r8,t_strike2_r7,t_strike2_r7]
                                elif self.time < 75:
                                    self.blocking = True
                                    self.time += 1
                                    self.img = self.block_r_list.pop()
                                    if self.knock_back:
                                        if self.time > 10: self.time = 1
                                        elif self.time == 10:
                                            self.knock_back = False
                                            self.time = 1
                                        else:
                                            self.time += 1
                                            self.pos = (self.pos[0]-2*self.time**(1/2), self.pos[1])
                                else:
                                    self.blocking = False
                                    if self.drop_strike_r == []:
                                        self.striking_ch = None; self.striking = False; self.hitting = False; self.time = 1
                                        self.swing_r = [t_strike2_r6,t_strike2_r6,t_strike2_r5,t_strike2_r5,t_strike2_r4,t_strike2_r4,t_strike2_r3,t_strike2_r3,t_strike2_r2,t_strike2_r2,t_strike2_r1,t_strike2_r1]
                                        self.drop_strike_r = [t_strike2_r13,t_strike2_r13,t_strike2_r12,t_strike2_r12,t_strike2_r11,t_strike2_r11,t_strike2_r10,t_strike2_r10]
                                    else:
                                        if len(self.drop_strike_r)==3: self.hitting = True
                                        self.img = self.drop_strike_r.pop()
                            else: self.img = self.swing_r.pop()
                            
                        elif self.striking_ch == 'leap_r':
                            if self.pos[0]>current_map.map_dict[self.current_plat]['x_range'][0]+50:
                                if self.leap_back_list_r == []:
                                    self.time = 1; self.falling = True
                                    self.leap_back_list_r = [t_jump_right5,t_jump_right5,t_jump_right4,t_jump_right4,t_jump_right3,t_jump_right3,t_jump_right2,t_jump_right2,t_jump_right1,t_jump_right1]
                                    self.striking_ch = None; self.striking = False
                                else:
                                    self.pos = (self.pos[0]-7,self.pos[1]-(1.5/self.time)**2)
                                    self.time += 1
                                    self.img = self.leap_back_list_r.pop()
                            else: self.striking_ch = None; self.striking = False
 
                # IDLE
                else:

                    # HERO SPOTTED
                    if self.current_plat == H.current_plat:
                        self.back = False
                        # H on left side, strike
                        if self.pos[0]+30<H.pos[0]+150 and self.pos[0]+50>H.pos[0]+150:
                            if self.face_l: self.striking = True; self.ch = None
                            else: self.ch = 'turn'
                        # H on right side, strike
                        elif self.pos[0]+250<H.pos[0]+150 and self.pos[0]+270>H.pos[0]+150:
                            if self.face_r: self.striking = True; self.ch = None
                            else: self.ch = 'turn'
                        elif H.pos[0]+250<self.pos[0]+150:
                            if self.face_r: self.ch = 'turn'
                            else: self.ch = 'walk'
                        elif H.pos[0]+50>self.pos[0]+150:
                            if self.face_l: self.ch = 'turn'
                            else: self.ch = 'walk'
                        else:
                            self.ch = 'walk'
                        
                    else:
                        if H.pos[1] > self.pos[1]: self.back = True
                        if self.turn_time == self.turn_limit or self.striking:
                            self.ch = random.choice(['walk','stand','turn'])
                            self.turn_time = 1; self.striking = False; self.hitting = False
                    
                    if self.ch == 'walk':
                        
                        if self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][1] and self.face_r or +\
                            self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][0] and self.face_l:
                                if self.current_plat != H.current_plat:
                                    self.ch = random.choice(['stand','turn'])

                        else:
                            if self.face_l:
                                if self.start_walking_l == []:
                                    if self.walk_l_list == []:
                                        self.walk_l_list = [t_walk_l8,t_walk_l8,t_walk_l8,t_walk_l7,t_walk_l7,t_walk_l7,t_walk_l6,t_walk_l6,t_walk_l6,t_walk_l5,t_walk_l5,t_walk_l5,t_walk_l4,t_walk_l4,t_walk_l4]
                                    else: self.img = self.walk_l_list.pop()
                                else: self.img = self.start_walking_l.pop()
                                self.pos = (self.pos[0]-4, self.pos[1])
                            else:
                                if self.start_walking_r == []:
                                    if self.walk_r_list == []:
                                        self.walk_r_list = [t_walk_r8,t_walk_r8,t_walk_r8,t_walk_r7,t_walk_r7,t_walk_r7,t_walk_r6,t_walk_r6,t_walk_r6,t_walk_r5,t_walk_r5,t_walk_r5,t_walk_r4,t_walk_r4,t_walk_r4]
                                    else: self.img = self.walk_r_list.pop()
                                else: self.img = self.start_walking_r.pop()
                                self.pos = (self.pos[0]+4,self.pos[1])
                            
                    elif self.ch == 'stand':
                        if self.face_l:
                            if self.stand_list_l == []:
                                self.stand_list_l = [t_stand_l5,t_stand_l5,t_stand_l5,t_stand_l4,t_stand_l4,t_stand_l4,t_stand_l3,t_stand_l3,t_stand_l3,t_stand_l2,t_stand_l2,t_stand_l2,t_stand_l1,t_stand_l1,t_stand_l1]
                            else: self.img = self.stand_list_l.pop()
                        else:
                            if self.stand_list_r == []:
                                self.stand_list_r = [t_stand_r5,t_stand_r5,t_stand_r5,t_stand_r4,t_stand_r4,t_stand_r4,t_stand_r3,t_stand_r3,t_stand_r3,t_stand_r2,t_stand_r2,t_stand_r2,t_stand_r1,t_stand_r1,t_stand_r1] 
                            else: self.img = self.stand_list_r.pop()

                    elif self.ch == 'turn':
                        if self.face_l:
                            if self.l_turn_r_list == []:
                                self.start_walking_l = [t_walk_l3,t_walk_l3,t_walk_l3,t_walk_l2,t_walk_l2,t_walk_l2,t_walk_l1,t_walk_l1,t_walk_l1]
                                self.r_turn_l_list = [t_turning8,t_turning8,t_turning7,t_turning7,t_turning6,t_turning6,t_turning5,t_turning5]
                                self.ch = random.choice(['walk','stand'])
                                self.face_r = True; self.face_l = False
                            else: self.img = self.l_turn_r_list.pop()
                        else:
                            if self.r_turn_l_list == []:
                                self.start_walking_r = [t_walk_r3,t_walk_r3,t_walk_r3,t_walk_r2,t_walk_r2,t_walk_r2,t_walk_r1,t_walk_r1,t_walk_r1]
                                self.l_turn_r_list = [t_turning4,t_turning4,t_turning3,t_turning3,t_turning2,t_turning2,t_turning1,t_turning1]
                                self.ch = random.choice(['walk','stand'])
                                self.face_r = False; self.face_l = True
                            else: self.img = self.r_turn_l_list.pop()       
                self.turn_time += 1
            else:
                self.falling = True


class Spearlik(object):
    def __init__(self, pos, is_phalanx):
        self.pos = pos
        self.img = g_stand_l5
        self.travelling = False
        self.current_plat = None
        self.falling = True
        self.landing = False
        self.face_r = False
        self.face_l = True
        self.leaping_back = False
        self.taunt = False
        self.striking = False
        self.hitting = False
        self.blocking = False
        self.knock_back = False
        self.turning_r_l = False
        self.turning_l_r = False
        self.dying = False
        self.dead = False
        self.back = False
        self.graphic = None
        self.graphic_pos = None
        self.graphic_ch = None
        
        self.time = 1
        self.turn_time = 1
        self.turn_limit = random.choice([400,200,100])
        self.strike_list = []
        self.ch = None
        self.striking_ch = None
        self.dying_ch = None

        self.is_phalanx = is_phalanx

        self.stand_list_l = [s_stand_l5,s_stand_l5,s_stand_l5,s_stand_l4,s_stand_l4,s_stand_l4,s_stand_l3,s_stand_l3,s_stand_l3,s_stand_l2,s_stand_l2,s_stand_l2,s_stand_l1,s_stand_l1,s_stand_l1]
        self.stand_list_r = [s_stand_r5,s_stand_r5,s_stand_r5,s_stand_r4,s_stand_r4,s_stand_r4,s_stand_r3,s_stand_r3,s_stand_r3,s_stand_r2,s_stand_r2,s_stand_r2,s_stand_r1,s_stand_r1,s_stand_r1] 

        self.l_turn_r_list = [s_turning5,s_turning5,s_turning4,s_turning4,s_turning3,s_turning3,s_turning2,s_turning2,s_turning1,s_turning1]
        self.r_turn_l_list = [s_turning1,s_turning1,s_turning2,s_turning2,s_turning3,s_turning3,s_turning4,s_turning4,s_turning5,s_turning5]

        self.start_walking_l = [s_walk_left2,s_walk_left2,s_walk_left2,s_walk_left1,s_walk_left1,s_walk_left1]
        self.start_walking_r = [s_walk_right2,s_walk_right2,s_walk_right2,s_walk_right1,s_walk_right1,s_walk_right1]

        self.walk_l_list = [s_walk_left8,s_walk_left8,s_walk_left8,s_walk_left7,s_walk_left7,s_walk_left7,s_walk_left6,s_walk_left6,s_walk_left6,s_walk_left5,s_walk_left5,s_walk_left5,s_walk_left4,s_walk_left4,s_walk_left4,s_walk_left3,s_walk_left3,s_walk_left3]
        self.walk_r_list = [s_walk_right8,s_walk_right8,s_walk_right8,s_walk_right7,s_walk_right7,s_walk_right7,s_walk_right6,s_walk_right6,s_walk_right6,s_walk_right5,s_walk_right5,s_walk_right5,s_walk_right4,s_walk_right4,s_walk_right4,s_walk_right3,s_walk_right3,s_walk_right3]

        self.taunt_l_list = [s_taunt_left9,s_taunt_left9,s_taunt_left8,s_taunt_left8,s_taunt_left7,s_taunt_left7,s_taunt_left6,s_taunt_left6,s_taunt_left5,s_taunt_left5,s_taunt_left4,s_taunt_left4,s_taunt_left3,s_taunt_left3,s_taunt_left2,s_taunt_left2,s_taunt_left1,s_taunt_left1]
        self.taunt_r_list = [s_taunt_right10,s_taunt_right10,s_taunt_right9,s_taunt_right9,s_taunt_right8,s_taunt_right8,s_taunt_right7,s_taunt_right7,s_taunt_right6,s_taunt_right6,s_taunt_right5,s_taunt_right5,s_taunt_right4,s_taunt_right4,s_taunt_right3,s_taunt_right3,s_taunt_right2,s_taunt_right2,s_taunt_right1,s_taunt_right1]
        
        self.leap_back_list_l = [s_jump_back_left5,s_jump_back_left5,s_jump_back_left4,s_jump_back_left4,s_jump_back_left3,s_jump_back_left3,s_jump_back_left2,s_jump_back_left2,s_jump_back_left1,s_jump_back_left1]
        self.leap_back_list_r = [s_jump_back_right5,s_jump_back_right5,s_jump_back_right4,s_jump_back_right4,s_jump_back_right3,s_jump_back_right3,s_jump_back_right2,s_jump_back_right2,s_jump_back_right1,s_jump_back_right1]

        self.strike1_l_list = [s_strike_left1_6,s_strike_left1_6,s_strike_left1_5,s_strike_left1_5,s_strike_left1_4,s_strike_left1_4,s_strike_left1_3,s_strike_left1_3,s_strike_left1_2,s_strike_left1_2,s_strike_left1_1,s_strike_left1_1]
        self.strike2_l_list = [s_strike_left2_5,s_strike_left2_5,s_strike_left2_4,s_strike_left2_4,s_strike_left2_3,s_strike_left2_3,s_strike_left2_2,s_strike_left2_2,s_strike_left2_1,s_strike_left2_1]

        self.strike1_r_list = [s_strike_right1_5,s_strike_right1_5,s_strike_right1_4,s_strike_right1_4,s_strike_right1_3,s_strike_right1_3,s_strike_right1_2,s_strike_right1_2,s_strike_right1_1,s_strike_right1_1]
        self.strike2_r_list = [s_strike_right2_5,s_strike_right2_5,s_strike_right2_4,s_strike_right2_4,s_strike_right2_3,s_strike_right2_3,s_strike_right2_2,s_strike_right2_2,s_strike_right2_1,s_strike_right2_1]

        self.block_l_list = [s_taunt_left2,s_taunt_left2,s_taunt_left5,s_taunt_left5,s_taunt_left6,s_taunt_left6,s_taunt_left7,s_taunt_left7,s_taunt_left8,s_taunt_left8,s_taunt_left9,s_taunt_left9]
        self.block_r_list = [s_taunt_right10,s_taunt_right10,s_taunt_right9,s_taunt_right9,s_taunt_right8,s_taunt_right8,s_taunt_right7,s_taunt_right7,s_taunt_right8,s_taunt_right8,s_taunt_right8]

        self.deadl_1_list = [s_death_l1_12,s_death_l1_12,s_death_l1_11,s_death_l1_11,s_death_l1_9,s_death_l1_9,s_death_l1_8,s_death_l1_8,s_death_l1_7,s_death_l1_7,s_death_l1_6,s_death_l1_6,s_death_l1_6,s_death_l1_5,s_death_l1_5,s_death_l1_5,s_death_l1_4,s_death_l1_4,s_death_l1_4,s_death_l1_3,s_death_l1_3,s_death_l1_3,s_death_l1_2,s_death_l1_2,s_death_l1_2,s_death_l1_1,s_death_l1_1,s_death_l1_1]
        self.deadl_2_list = [s_death_l2_7,s_death_l2_7,s_death_l2_6,s_death_l2_6,s_death_l2_5,s_death_l2_5,s_death_l2_4,s_death_l2_4,s_death_l2_4,s_death_l2_3,s_death_l2_3,s_death_l2_3,s_death_l2_2,s_death_l2_2,s_death_l2_2,s_death_l2_1,s_death_l2_1,s_death_l2_1]
        self.deadl_3_list = [s_death_l3_7,s_death_l3_7,s_death_l3_6,s_death_l3_6,s_death_l3_5,s_death_l3_5,s_death_l3_4,s_death_l3_4,s_death_l3_4,s_death_l3_3,s_death_l3_3,s_death_l3_3,s_death_l3_2,s_death_l3_2,s_death_l3_2,s_death_l3_1,s_death_l3_1,s_death_l3_1]
        self.deadl_4_list = [s_death_l4_9,s_death_l4_9,s_death_l4_8,s_death_l4_8,s_death_l4_7,s_death_l4_7,s_death_l4_6,s_death_l4_6,s_death_l4_5,s_death_l4_5,s_death_l4_4,s_death_l4_4,s_death_l4_3,s_death_l4_3,s_death_l4_3,s_death_l4_2,s_death_l4_2,s_death_l4_2,s_death_l4_1,s_death_l4_1,s_death_l4_1]

        self.deadr_1_list = [s_death_r1_9,s_death_r1_9,s_death_r1_8,s_death_r1_8,s_death_r1_7,s_death_r1_7,s_death_r1_6,s_death_r1_6,s_death_r1_6,s_death_r1_5,s_death_r1_5,s_death_r1_5,s_death_r1_4,s_death_r1_4,s_death_r1_4,s_death_r1_3,s_death_r1_3,s_death_r1_3,s_death_r1_2,s_death_r1_2,s_death_r1_2,s_death_r1_1,s_death_r1_1,s_death_r1_1]
        self.deadr_2_list = [s_death_r2_5,s_death_r2_5,s_death_r2_4,s_death_r2_4,s_death_r2_3,s_death_r2_3,s_death_r2_3,s_death_r2_2,s_death_r2_2,s_death_r2_2,s_death_r2_1,s_death_r2_1,s_death_r2_1]
        
        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_2]
        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_2]
        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_2]

    def fall(self, current_map):
        y = 2*self.time + self.pos[1]
        self.time += 1
        for k in current_map.map_dict.keys():
            if self.pos[1]+200<current_map.map_dict[k]['y_range'] and self.pos[1]+320>current_map.map_dict[k]['y_range']:
                if self.pos[0]+90<current_map.map_dict[k]['x_range'][1] and self.pos[0]+200>current_map.map_dict[k]['x_range'][0]:
                    y = current_map.map_dict[k]['y_range']-260
                    self.current_plat = k
                    self.falling = False
                    self.landing = True
                    self.time = 1
                    
        self.pos = (self.pos[0], y)

    def regenerate(self):
        self.is_phalanx = False
##        self.dying = False; self.dying_ch = None
        
        self.pos = (random.choice([-200, 500, 1100]), -300)
        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_4]
        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_4]
        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_4]

    def shift(self, current_map, H):

        if self.dying:

            if self.graphic_ch == None:
                self.graphic_ch = random.choice(['bl1','bl2','b13'])
            if self.graphic_ch == 'bl1':
                if self.blood_graph1 != []: self.graphic = self.blood_graph1.pop()
                else: self.graphic = None
            elif self.graphic_ch == 'bl2':
                if self.blood_graph2 != []: self.graphic = self.blood_graph2.pop()
                else: self.graphic = None
            elif self.graphic_ch == 'bl3':
                if self.blood_graph3 != []: self.graphic = self.blood_graph3.pop()
                else: self.graphic = None
            self.graphic_pos = (self.pos[0]+150, self.pos[1]+110)
            
            if self.dying_ch == None:
                if self.face_l: self.dying_ch = random.choice(['dl1','dl2','dl3','dl4'])
                else: self.dying_ch = random.choice(['dr1','dr2'])
            else:
                if self.dying_ch == 'dl1':
                    if self.deadl_1_list == []:
                        self.img = s_death_l1_12; self.dead = True
                    else: self.img = self.deadl_1_list.pop()
                    
                elif self.dying_ch == 'dl2':
                    if self.deadl_2_list == []:
                        self.img = s_death_l2_7; self.dead = True
                    else: self.img = self.deadl_2_list.pop()
                    
                elif self.dying_ch == 'dl3':
                    if self.deadl_3_list == []:
                        self.img = s_death_l3_7; self.dead = True
                    else: self.img = self.deadl_3_list.pop()
                        
                elif self.dying_ch == 'dl4':
                    if self.deadl_4_list == []:
                        self.img = s_death_l4_9; self.dead = True
                    else: self.img = self.deadl_4_list.pop()
                        
                elif self.dying_ch == 'dr1':
                    if self.deadr_1_list == []:
                        self.img = s_death_r1_9; self.dead = True
                    else: self.img = self.deadr_1_list.pop()
                        
                elif self.dying_ch == 'dr2':
                    if self.deadr_2_list == []:
                        self.img = s_death_r2_5; self.dead = True
                    else: self.img = self.deadr_2_list.pop()
            
        elif self.falling:
            self.fall(current_map)
##            if self.pos[1]>600:
##                self.pos = (200,0)

        elif H.current_plat == self.current_plat and self.knock_back:
            if self.face_r:
                if self.time == 10:
                    self.knock_back = False
                    self.time = 1
                else:
                    self.time += 1
                    self.img = s_taunt_right9
                    self.pos = (self.pos[0]-5*self.time**(1/2), self.pos[1])
            else:
                if self.time == 10:
                    self.knock_back = False
                    self.time = 1
                else:
                    self.time += 1
                    self.img = s_taunt_left9
                    self.pos = (self.pos[0]+5*self.time**(1/2), self.pos[1])

            # HURT
        elif H.current_plat == self.current_plat and H.hitting and not H.blocking:
            if self.face_r and H.face_l:
                if H.pos[0]+100>self.pos[0]+130 and H.pos[0]+100<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.blocking:
                        self.knock_back = True
                    else:
                        self.dying = True
            elif self.face_l and H.face_l:
                if H.pos[0]+100>self.pos[0]+130 and H.pos[0]+100<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    self.dying = True
            elif self.face_l and H.face_r:
                if H.pos[0]+300>self.pos[0]+130 and H.pos[0]+300<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.blocking:
                        self.knock_back = True
                    else:
                        self.dying = True
            elif self.face_r and H.face_r:
                if H.pos[0]+300>self.pos[0]+130 and H.pos[0]+300<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    self.dying = True
                    
        # ON PLATFORM
        else:
            if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:

                # HIT THE HERO
                if self.hitting and self.pos[0]+150>H.pos[0]+150 and self.pos[0]<H.pos[0]+170 or +\
                   self.hitting and self.pos[0]+150<H.pos[0]+150 and self.pos[0]+300>H.pos[0]+130:
                    if H.blocking and H.face_r:
                        if self.pos[0]+150<H.pos[0]+150: H.hurt = True
                        else: H.knock_back = True
                    elif H.blocking and H.face_l:
                        if self.pos[0]+150>H.pos[0]+150: H.hurt = True
                        else: H.knock_back = True
                    else: H.hurt = True
                            
                # STRIKE!!!
                if self.striking:
                    if self.striking_ch == None and not self.is_phalanx:
                        if self.face_l:
                            self.striking_ch = random.choice(['l_1','l_2','b_l','leap_l'])
                        else: self.striking_ch = random.choice(['r_1','r_2','b_r','leap_r'])
                    else:
                        if self.striking_ch == 'l_1':
                            if self.strike1_l_list == []:
                                self.strike1_l_list = [s_strike_left1_6,s_strike_left1_6,s_strike_left1_5,s_strike_left1_5,s_strike_left1_4,s_strike_left1_4,s_strike_left1_3,s_strike_left1_3,s_strike_left1_2,s_strike_left1_2,s_strike_left1_1,s_strike_left1_1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike1_l_list)==3: self.hitting = True
                                self.img = self.strike1_l_list.pop()
                        elif self.striking_ch == 'l_2':
                            if self.strike2_l_list == []:
                                self.strike2_l_list = [s_strike_left2_5,s_strike_left2_5,s_strike_left2_4,s_strike_left2_4,s_strike_left2_3,s_strike_left2_3,s_strike_left2_2,s_strike_left2_2,s_strike_left2_2,s_strike_left2_1,s_strike_left2_1,s_strike_left2_1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike2_l_list)==3: self.hitting = True
                                self.img = self.strike2_l_list.pop()
                        elif self.striking_ch == 'leap_l':
                            if self.leap_back_list_l == []:
                                self.time = 1; self.falling = True
                                self.leap_back_list_l = [s_jump_back_left5,s_jump_back_left5,s_jump_back_left4,s_jump_back_left4,s_jump_back_left3,s_jump_back_left3,s_jump_back_left2,s_jump_back_left2,s_jump_back_left1,s_jump_back_left1]
                                self.striking_ch = None; self.striking = False
                            else:
                                self.pos = (self.pos[0]+7,self.pos[1]-(1.5/self.time)**2)
                                self.time += 1
                                self.img = self.leap_back_list_l.pop()
                        elif self.striking_ch == 'b_l':
                            if self.block_l_list == []:
                                self.block_l_list = [s_taunt_left9,s_taunt_left9,s_taunt_left8,s_taunt_left8,s_taunt_left7,s_taunt_left7,s_taunt_left6,s_taunt_left6,s_taunt_left5,s_taunt_left5,s_taunt_left4,s_taunt_left4,s_taunt_left3,s_taunt_left3,s_taunt_left2,s_taunt_left2,s_taunt_left1,s_taunt_left1]
                                self.striking_ch = None; self.striking = False; self.blocking = False
                            else:
                                self.blocking = True
                                self.img = self.block_l_list.pop()
                            
                        elif self.striking_ch == 'r_1':
                            if self.strike1_r_list == []:
                                self.strike1_r_list = [s_strike_right1_5,s_strike_right1_5,s_strike_right1_4,s_strike_right1_4,s_strike_right1_3,s_strike_right1_3,s_strike_right1_2,s_strike_right1_2,s_strike_right1_2,s_strike_right1_1,s_strike_right1_1,s_strike_right1_1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike1_r_list)==3: self.hitting = True
                                self.img = self.strike1_r_list.pop()
                        elif self.striking_ch == 'r_2':
                            if self.strike2_r_list == []:
                                self.strike2_r_list = [s_strike_right2_5,s_strike_right2_5,s_strike_right2_4,s_strike_right2_4,s_strike_right2_3,s_strike_right2_3,s_strike_right2_2,s_strike_right2_2,s_strike_right2_2,s_strike_right2_1,s_strike_right2_1,s_strike_right2_1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike2_r_list)==3: self.hitting = True
                                self.img = self.strike2_r_list.pop()
                        elif self.striking_ch == 'b_r':
                            if self.block_r_list == []:
                                self.block_r_list = [s_taunt_right7,s_taunt_right7,s_taunt_right7,s_taunt_right7,s_taunt_right7,s_taunt_right7,s_taunt_right8,s_taunt_right8,s_taunt_right8,s_taunt_right8,s_taunt_right8,s_taunt_right8]
                                self.striking_ch = None; self.striking = False; self.blocking = False
                            else:
                                self.blocking = True
                                self.img = self.block_r_list.pop()
                        elif self.striking_ch == 'leap_r':
                            if self.pos[0]>current_map.map_dict[self.current_plat]['x_range'][0]+50:
                                if self.leap_back_list_r == []:
                                    self.time = 1; self.falling = True
                                    self.leap_back_list_r = [s_jump_back_right5,s_jump_back_right5,s_jump_back_right4,s_jump_back_right4,s_jump_back_right3,s_jump_back_right3,s_jump_back_right2,s_jump_back_right2,s_jump_back_right1,s_jump_back_right1]
                                    self.striking_ch = None; self.striking = False
                                else:
                                    self.pos = (self.pos[0]-7,self.pos[1]-(1.5/self.time)**2)
                                    self.time += 1
                                    self.img = self.leap_back_list_r.pop()
                            else: self.striking_ch = None; self.striking = False
 
                # IDLE
                else:

                    # HERO SPOTTED
                    if self.current_plat == H.current_plat and not self.is_phalanx:
                        self.back = False
                        if self.pos[0]+30<H.pos[0]+180 and self.pos[0]+50>H.pos[0]+180:
                            if self.face_l: self.striking = True; self.ch = None
                            else: self.ch = 'turn'
                        elif self.pos[0]+250<H.pos[0]+120 and self.pos[0]+270>H.pos[0]+120:
                            if self.face_r: self.striking = True; self.ch = None
                            else: self.ch = 'turn'
                        elif H.pos[0]+150<self.pos[0]:
                            if self.face_r: self.ch = 'turn'
                            else: self.ch = 'walk'
                        elif H.pos[0]+150>self.pos[0]+150:
                            if self.face_l: self.ch = 'turn'
                            else: self.ch = 'walk'
                        else: self.ch = 'walk'
                        
                    elif self.current_plat != H.current_plat:
                        if H.pos[1] > self.pos[1]: self.back = True
                        if self.turn_time == self.turn_limit:
                            self.ch = random.choice(['walk','stand','taunt','turn'])
                            self.turn_time = 1
                    
                    if self.ch == 'walk':
                        if self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][1] and self.face_r or +\
                            self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][0] and self.face_l:
                            self.ch = random.choice(['stand','turn'])
                        else:
                            if self.face_l:
                                if self.start_walking_l == []:
                                    if self.walk_l_list == []:
                                        self.walk_l_list = [s_walk_left8,s_walk_left8,s_walk_left8,s_walk_left7,s_walk_left7,s_walk_left7,s_walk_left6,s_walk_left6,s_walk_left6,s_walk_left5,s_walk_left5,s_walk_left5,s_walk_left4,s_walk_left4,s_walk_left4]
                                    else: self.img = self.walk_l_list.pop()
                                else: self.img = self.start_walking_l.pop()
                                self.pos = (self.pos[0]-2, self.pos[1])
                            else:
                                if self.start_walking_r == []:
                                    if self.walk_r_list == []:
                                        self.walk_r_list = [s_walk_right8,s_walk_right8,s_walk_right8,s_walk_right7,s_walk_right7,s_walk_right7,s_walk_right6,s_walk_right6,s_walk_right6,s_walk_right5,s_walk_right5,s_walk_right5,s_walk_right4,s_walk_right4,s_walk_right4]
                                    else: self.img = self.walk_r_list.pop()
                                else: self.img = self.start_walking_r.pop()
                                self.pos = (self.pos[0]+2,self.pos[1])
                            
                    elif self.ch == 'stand':
                        if self.face_l:
                            if self.stand_list_l == []:
                                self.stand_list_l = [s_stand_l5,s_stand_l5,s_stand_l5,s_stand_l4,s_stand_l4,s_stand_l4,s_stand_l3,s_stand_l3,s_stand_l3,s_stand_l3,s_stand_l3,s_stand_l3,s_stand_l2,s_stand_l2,s_stand_l2,s_stand_l1,s_stand_l1,s_stand_l1]
                            else: self.img = self.stand_list_l.pop()
                        else:
                            if self.stand_list_r == []:
                                self.stand_list_r = [s_stand_r5,s_stand_r5,s_stand_r5,s_stand_r4,s_stand_r4,s_stand_r4,s_stand_r3,s_stand_r3,s_stand_r3,s_stand_r3,s_stand_r3,s_stand_r3,s_stand_r2,s_stand_r2,s_stand_r2,s_stand_r1,s_stand_r1,s_stand_r1] 
                            else: self.img = self.stand_list_r.pop()

                    elif self.ch == 'taunt':
                        if self.face_l:
                            if self.taunt_l_list == []:
                                self.start_walking_l = [s_walk_left2,s_walk_left2,s_walk_left2,s_walk_left1,s_walk_left1,s_walk_left1]
                                self.taunt_l_list = [s_taunt_left9,s_taunt_left9,s_taunt_left8,s_taunt_left8,s_taunt_left7,s_taunt_left7,s_taunt_left6,s_taunt_left6,s_taunt_left5,s_taunt_left5,s_taunt_left4,s_taunt_left4,s_taunt_left3,s_taunt_left3,s_taunt_left2,s_taunt_left2,s_taunt_left1,s_taunt_left1]
                                self.ch = 'walk'
                            else: self.img = self.taunt_l_list.pop()
                        else:
                            if self.taunt_r_list == []:
                                self.start_walking_r = [s_walk_right2,s_walk_right2,s_walk_right2,s_walk_right1,s_walk_right1,s_walk_right1]
                                self.taunt_r_list = [s_taunt_right10,s_taunt_right10,s_taunt_right9,s_taunt_right9,s_taunt_right8,s_taunt_right8,s_taunt_right7,s_taunt_right7,s_taunt_right6,s_taunt_right6,s_taunt_right5,s_taunt_right5,s_taunt_right4,s_taunt_right4,s_taunt_right3,s_taunt_right3,s_taunt_right2,s_taunt_right2,s_taunt_right1,s_taunt_right1]
                                self.ch = 'walk'
                            else: self.img = self.taunt_r_list.pop()
                    elif self.ch == 'turn':
                        if self.face_l:
                            if self.l_turn_r_list == []:
                                self.r_turn_l_list = [s_turning1,s_turning1,s_turning2,s_turning2,s_turning3,s_turning3,s_turning4,s_turning4,s_turning5,s_turning5]
                                self.ch = random.choice(['walk','stand','taunt'])
                                self.face_r = True; self.face_l = False
                            else: self.img = self.l_turn_r_list.pop()
                        else:
                            if self.r_turn_l_list == []:
                                self.l_turn_r_list = [s_turning5,s_turning5,s_turning4,s_turning4,s_turning3,s_turning3,s_turning2,s_turning2,s_turning1,s_turning1]
                                self.ch = random.choice(['walk','stand','taunt'])
                                self.face_r = False; self.face_l = True
                            else: self.img = self.r_turn_l_list.pop()
                    else:
                        if self.face_l: self.img = s_taunt_left9
                        else: self.img = s_taunt_right10
                            
                self.turn_time += 1
                
            else:
                self.falling = True

        
class Goblik(object):
    def __init__(self, pos, is_phalanx):
        self.pos = pos
        self.img = g_stand_l5
        self.travelling = False
        self.current_plat = None
        self.falling = True
        self.landing = False
        self.face_r = False
        self.face_l = True
        self.leaping_back = False
        self.taunt = False
        self.striking = False
        self.hitting = False
        self.blocking = False
        self.knock_back = False
        self.turning_r_l = False
        self.turning_l_r = False
        self.is_scared = False
        self.dead = False
        self.back = False
        self.dying = False
        self.hurt = False
        self.hp = 7
        self.graphic = None
        self.graphic_pos = None
        self.graphic_ch = None
        
        self.time = 1
        self.turn_time = 1
        self.turn_limit = random.choice([400,200,100])
        self.strike_list = []
        self.ch = None
        self.striking_ch = None
        self.dying_ch = None

        self.is_phalanx = is_phalanx

        self.stand_list_l = [g_stand_l5,g_stand_l5,g_stand_l5,g_stand_l4,g_stand_l4,g_stand_l4,g_stand_l3,g_stand_l3,g_stand_l3,g_stand_l2,g_stand_l2,g_stand_l2,g_stand_l1,g_stand_l1,g_stand_l1]
        self.stand_list_r = [g_stand_r5,g_stand_r5,g_stand_r5,g_stand_r4,g_stand_r4,g_stand_r4,g_stand_r3,g_stand_r3,g_stand_r3,g_stand_r2,g_stand_r2,g_stand_r2,g_stand_r1,g_stand_r1,g_stand_r1]

        self.l_turn_r_list = [g_turn3, g_turn3, g_turn3, g_turn2, g_turn2, g_turn2, g_turn1, g_turn1, g_turn1]
        self.r_turn_l_list = [g_turn1, g_turn1, g_turn1, g_turn2, g_turn2, g_turn2, g_turn3, g_turn3, g_turn3]

        self.start_walking_l = [g_walking1_l,g_walking1_l,g_walking1_l,g_walking2_l,g_walking2_l,g_walking2_l]
        self.start_walking_r = [g_walking1_r,g_walking1_r,g_walking1_r,g_walking2_r,g_walking2_r,g_walking2_r]
        
        self.walk_l_list = [g_walking11_l,g_walking11_l,g_walking11_l,g_walking10_l,g_walking10_l,g_walking10_l,g_walking9_l,g_walking9_l,g_walking9_l,g_walking8_l,g_walking8_l,g_walking8_l,g_walking7_l,
                            g_walking7_l,g_walking7_l,g_walking6_l,g_walking6_l,g_walking6_l,g_walking5_l,g_walking5_l,g_walking5_l,g_walking4_l,g_walking4_l,g_walking4_l,g_walking3_l,g_walking3_l,g_walking3_l,]
        self.walk_r_list = [g_walking11_r,g_walking11_r,g_walking11_r,g_walking10_r,g_walking10_r,g_walking10_r,g_walking9_r,g_walking9_r,g_walking9_r,g_walking8_r,g_walking8_r,g_walking8_r,g_walking7_r,
                            g_walking7_r,g_walking7_r,g_walking6_r,g_walking6_r,g_walking6_r,g_walking5_r,g_walking5_r,g_walking5_r,g_walking4_r,g_walking4_r,g_walking4_r,g_walking3_r,g_walking3_r,g_walking3_r]

        self.taunt_l_list = [g_taunt_l14,g_taunt_l14,g_taunt_l13,g_taunt_l13,g_taunt_l12,g_taunt_l12,g_taunt_l11,g_taunt_l11,g_taunt_l10,g_taunt_l10,g_taunt_l9,g_taunt_l9,g_taunt_l8,g_taunt_l8,
                             g_taunt_l7,g_taunt_l7,g_taunt_l6,g_taunt_l6,g_taunt_l5,g_taunt_l5,g_taunt_l4,g_taunt_l4,g_taunt_l3,g_taunt_l3,g_taunt_l2,g_taunt_l2,g_taunt_l1,g_taunt_l1]

        self.taunt_r_list = [g_taunt_r14,g_taunt_r14,g_taunt_r13,g_taunt_r13,g_taunt_r12,g_taunt_r12,g_taunt_r11,g_taunt_r11,g_taunt_r10,g_taunt_r10,g_taunt_r9,g_taunt_r9,g_taunt_r8,g_taunt_r8,
                             g_taunt_r7,g_taunt_r7,g_taunt_r6,g_taunt_r6,g_taunt_r5,g_taunt_r5,g_taunt_r4,g_taunt_r4,g_taunt_r3,g_taunt_r3,g_taunt_r2,g_taunt_r2,g_taunt_r1,g_taunt_r1]

        self.leap_back_list = [g_leap_back5,g_leap_back5,g_leap_back4,g_leap_back4,g_leap_back3,g_leap_back3,g_leap_back2,g_leap_back2,g_leap_back1,g_leap_back1]
        
        self.block_l_list = [g_block3_l,g_block3_l,g_block3_l,g_block3_l,g_block3_l,g_block3_l,g_block2_l,g_block2_l,g_block1_l,g_block1_l]
        self.block_r_list = [g_block3_r,g_block3_r,g_block3_r,g_block3_r,g_block3_r,g_block3_r,g_block2_r,g_block2_r,g_block1_r,g_block1_r]

        self.strike1_l_list = [g_strike1_l6,g_strike1_l6,g_strike1_l5,g_strike1_l5,g_strike1_l4,g_strike1_l4,g_strike1_l3,g_strike1_l3,g_strike1_l2,g_strike1_l2,g_strike1_l1,g_strike1_l1]
        self.strike2_l_list = [g_strike2_l10,g_strike2_l10,g_strike2_l9,g_strike2_l9,g_strike2_l8,g_strike2_l8,g_strike2_l7,g_strike2_l7,g_strike2_l6,g_strike2_l6,g_strike2_l5,g_strike2_l5,g_strike2_l4,g_strike2_l4,g_strike2_l3,g_strike2_l3,g_strike2_l2,g_strike2_l2,g_strike2_l1,g_strike2_l1]
        self.jump_strike_l_list = [g_jump_strike_l6,g_jump_strike_l6,g_jump_strike_l5,g_jump_strike_l5,g_jump_strike_l4,g_jump_strike_l4,g_jump_strike_l3,g_jump_strike_l3,g_jump_strike_l2,g_jump_strike_l2,g_jump_strike_l1,g_jump_strike_l1]

        self.strike1_r_list = [g_strike1_r7,g_strike1_r7,g_strike1_r6,g_strike1_r6,g_strike1_r5,g_strike1_r5,g_strike1_r4,g_strike1_r4,g_strike1_r3,g_strike1_r3,g_strike1_r2,g_strike1_r2,g_strike1_r1,g_strike1_r1]
        self.jump_strike_r_list = [g_jump_strike_r6,g_jump_strike_r6,g_jump_strike_r5,g_jump_strike_r5,g_jump_strike_r4,g_jump_strike_r4,g_jump_strike_r3,g_jump_strike_r3,g_jump_strike_r2,g_jump_strike_r2,g_jump_strike_r1,g_jump_strike_r1]

        self.deadl_1_list = [g_dead1_l8,g_dead1_l8,g_dead1_l8,g_dead1_l8,g_dead1_l8,g_dead1_l8,g_dead1_l7,g_dead1_l7,g_dead1_l6,g_dead1_l6,g_dead1_l5,g_dead1_l5,g_dead1_l4,g_dead1_l4,g_dead1_l3,g_dead1_l3,g_dead1_l2,g_dead1_l2,g_dead1_l1,g_dead1_l1]
        self.deadl_2_list = [g_dead2_l8,g_dead2_l8,g_dead2_l8,g_dead2_l8,g_dead2_l8,g_dead2_l8,g_dead2_l7,g_dead2_l7,g_dead2_l6,g_dead2_l6,g_dead2_l5,g_dead2_l5,g_dead2_l4,g_dead2_l4,g_dead2_l3,g_dead2_l3,g_dead2_l2,g_dead2_l2,g_dead2_l1,g_dead2_l1]
        self.deadl_3_list = [g_dead3_l7,g_dead3_l7,g_dead3_l7,g_dead3_l7,g_dead3_l7,g_dead3_l7,g_dead3_l6,g_dead3_l6,g_dead3_l5,g_dead3_l5,g_dead3_l4,g_dead3_l4,g_dead3_l3,g_dead3_l3,g_dead3_l2,g_dead3_l2,g_dead3_l1,g_dead3_l1]
        self.deadl_4_list = [g_dead4_l14,g_dead4_l14,g_dead4_l14,g_dead4_l14,g_dead4_l14,g_dead4_l14,g_dead4_l13,g_dead4_l13,g_dead4_l12,g_dead4_l12,g_dead4_l11,g_dead4_l11,g_dead4_l10,g_dead4_l10,g_dead4_l9,g_dead4_l9,g_dead4_l8,g_dead4_l8,g_dead4_l7,g_dead4_l7,g_dead4_l6,g_dead4_l6,g_dead4_l5,g_dead4_l5,g_dead4_l4,g_dead4_l4,g_dead4_l3,g_dead4_l3,g_dead4_l2,g_dead4_l2,g_dead4_l1,g_dead4_l1]
        self.deadl_5_list = [g_dead5_l8,g_dead5_l8,g_dead5_l8,g_dead5_l8,g_dead5_l8,g_dead5_l8,g_dead5_l7,g_dead5_l7,g_dead5_l6,g_dead5_l6,g_dead5_l5,g_dead5_l5,g_dead5_l4,g_dead5_l4,g_dead5_l3,g_dead5_l3,g_dead5_l2,g_dead5_l2,g_dead5_l1,g_dead5_l1]

        self.deadr_1_list = [g_dead1_r8,g_dead1_r8,g_dead1_r8,g_dead1_r8,g_dead1_r8,g_dead1_r8,g_dead1_r7,g_dead1_r7,g_dead1_r6,g_dead1_r6,g_dead1_r5,g_dead1_r5,g_dead1_r4,g_dead1_r4,g_dead1_r3,g_dead1_r3,g_dead1_r2,g_dead1_r2,g_dead1_r1,g_dead1_r1]
        self.deadr_2_list = [g_dead2_r9,g_dead2_r9,g_dead2_r9,g_dead2_r9,g_dead2_r9,g_dead2_r9,g_dead2_r8,g_dead2_r8,g_dead2_r7,g_dead2_r7,g_dead2_r6,g_dead2_r6,g_dead2_r5,g_dead2_r5,g_dead2_r4,g_dead2_r4,g_dead2_r3,g_dead2_r3,g_dead2_r2,g_dead2_r2,g_dead2_r1,g_dead2_r1]
        self.deadr_3_list = [g_dead3_r6,g_dead3_r6,g_dead3_r6,g_dead3_r6,g_dead3_r6,g_dead3_r6,g_dead3_r5,g_dead3_r5,g_dead3_r4,g_dead3_r4,g_dead3_r3,g_dead3_r3,g_dead3_r2,g_dead3_r2,g_dead3_r1,g_dead3_r1]

        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_2]
        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_2]
        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_2]
        
    def fall(self, current_map):
        y = 2*self.time + self.pos[1]
        self.time += 1
        for k in current_map.map_dict.keys():
            if self.pos[1]+200<current_map.map_dict[k]['y_range'] and self.pos[1]+320>current_map.map_dict[k]['y_range']:
                if self.pos[0]+90<current_map.map_dict[k]['x_range'][1] and self.pos[0]+200>current_map.map_dict[k]['x_range'][0]:
                    y = current_map.map_dict[k]['y_range']-260
                    self.current_plat = k
                    self.falling = False
                    self.landing = True
                    self.time = 1
                    
        self.pos = (self.pos[0], y)

    def regenerate(self):
        self.dying = False; self.dying_ch = None
        
##        self.pos = (random.choice([-200, 500, 1100]), -300)
        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_4]
        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_4]
        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_4]
        
    def shift(self, current_map, H):

        if self.dying or self.hurt:
            if self.hurt or self.graphic_ch == 'bl1' or self.graphic_ch == 'bl2' or self.graphic_ch == 'bl3':
                if self.graphic_ch == None:
                    self.graphic_ch = random.choice(['bl1','bl2'])
                if self.graphic_ch == 'bl1':
                    if self.blood_graph1 == []:
                        self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_4]
                        self.graphic_ch = None; self.graphic = None; self.hurt = False
                    else: self.graphic = self.blood_graph1.pop()
                elif self.graphic_ch == 'bl2':
                    if self.blood_graph2 == []:
                        self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_4]
                        self.graphic_ch = None; self.graphic = None; self.hurt = False
                    else: self.graphic = self.blood_graph2.pop()
                elif self.graphic_ch == 'bl3':
                    if self.blood_graph3 == []:
                        self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_4]
                        self.graphic_ch = None; self.graphic = None; self.hurt = False
                    else: self.graphic = self.blood_graph3.pop()
                self.graphic_pos = (self.pos[0]+150, self.pos[1]+110)

                if self.face_r: self.img = g_dead1_r2
                else: self.img = g_dead1_l2

            if self.dying:
                if self.dying_ch == None:
                    if self.face_l: self.dying_ch = random.choice(['dl1','dl2','dl3','dl4','dl5'])
                    else: self.dying_ch = random.choice(['dr1','dr2','dr3'])
                else:
                    if self.dying_ch == 'dl1':
                        if self.deadl_1_list == []:
                            self.img = g_dead1_l8; self.dead = True
                        else: self.img = self.deadl_1_list.pop()
                        
                    elif self.dying_ch == 'dl2':
                        if self.deadl_2_list == []:
                            self.img = g_dead2_l8; self.dead = True
                        else: self.img = self.deadl_2_list.pop()
                        
                    elif self.dying_ch == 'dl3':
                        if self.deadl_3_list == []:
                            self.img = g_dead3_l7; self.dead = True
                        else: self.img = self.deadl_3_list.pop()
                            
                    elif self.dying_ch == 'dl4':
                        if self.deadl_4_list == []:
                            self.img = g_dead4_l14; self.dead = True
                        else: self.img = self.deadl_4_list.pop()
                            
                    elif self.dying_ch == 'dl5':
                        if self.deadl_5_list == []:
                            self.img = g_dead5_l8; self.dead = True
                        else: self.img = self.deadl_5_list.pop()
                            
                    elif self.dying_ch == 'dr1':
                        if self.deadr_1_list == []:
                            self.img = g_dead1_r8; self.dead = True
                        else: self.img = self.deadr_1_list.pop()
                            
                    elif self.dying_ch == 'dr2':
                        if self.deadr_2_list == []:
                            self.img = g_dead2_r9; self.dead = True
                        else: self.img = self.deadr_2_list.pop()
                            
                    else:
                        if self.deadr_3_list == []:
                            self.img = g_dead3_r6; self.dead = True
                        else: self.img = self.deadr_3_list.pop()
##                self.regenerate()
            
        elif self.falling:
            self.fall(current_map)
##            if self.pos[1]>600:
##                self.pos = (200,0)

        elif self.knock_back:
            if self.time > 10: self.time = 1
            if self.face_r:
                if self.time == 10:
                    self.knock_back = False
                    self.time = 1
                else:
                    self.time += 1
                    self.img = g_block4_r
                    self.pos = (self.pos[0]-2*self.time**(1/2), self.pos[1])
            else:
                if self.time == 10:
                    self.knock_back = False
                    self.time = 1
                else:
                    self.time += 1
                    self.img = g_block4_l
                    self.pos = (self.pos[0]+2*self.time**(1/2), self.pos[1])

            # HURT
        elif H.current_plat == self.current_plat and H.hitting and not H.blocking:
            if self.hp < 3: self.is_scared = True
            
            if self.face_r and H.face_l:
                if H.pos[0]+100>self.pos[0]+130 and H.pos[0]+100<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.blocking:
                        self.knock_back = True
                    else:
                        if self.hp < 1: self.dying = True; self.hurt = True
                        else: self.hp -= 1; self.hurt = True
            elif self.face_l and H.face_l:
                if H.pos[0]+100>self.pos[0]+130 and H.pos[0]+100<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.hp < 1: self.dying = True; self.hurt = True
                    else: self.hp -= 1; self.hurt = True
            elif self.face_l and H.face_r:
                if H.pos[0]+300>self.pos[0]+130 and H.pos[0]+300<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.blocking:
                        self.knock_back = True
                    else:
                        if self.hp < 1: self.dying = True; self.hurt = True
                        else: self.hp -= 1; self.hurt = True
            elif self.face_r and H.face_r:
                if H.pos[0]+300>self.pos[0]+130 and H.pos[0]+300<self.pos[0]+270 and H.pos[1]+150>self.pos[1] and H.pos[1]+150<self.pos[1]+300:
                    if self.hp < 1: self.dying = True; self.hurt = True
                    else: self.hp -= 1; self.hurt = True
                    
        # ON PLATFORM
        else:
            if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:

                # HIT THE HERO
                if self.hitting and self.pos[0]+150>H.pos[0]+150 and self.pos[0]+60<H.pos[0]+150 or +\
                   self.hitting and self.pos[0]+150<H.pos[0]+150 and self.pos[0]+240>H.pos[0]+150:
                    if H.blocking and H.face_r:
                        if self.pos[0]+150<H.pos[0]+150: H.hurt = True
                        else: H.knock_back = True
                    elif H.blocking and H.face_l:
                        if self.pos[0]+150>H.pos[0]+150: H.hurt = True
                        else: H.knock_back = True
                    elif H.striking and H.face_r:
                        if self.pos[0]+150>H.pos[0]+150: H.blocked = True
                    elif H.striking and H.face_l:
                        if self.pos[0]+150<H.pos[0]+150: H.blocked = True
                    else: H.hurt = True
                            
                # STRIKE!!!
                if self.striking:
                    if self.striking_ch == None:
                        if self.face_l:
                            self.striking_ch = random.choice(['l_1','l_2','j_l','b_l','b_l','leap'])
                        else: self.striking_ch = random.choice(['r_1','j_r','b_r','b_r'])
                    else:
                        if self.striking_ch == 'l_1':
                            if self.strike1_l_list == []:
                                self.strike1_l_list = [g_strike1_l6,g_strike1_l6,g_strike1_l5,g_strike1_l5,g_strike1_l4,g_strike1_l4,g_strike1_l3,g_strike1_l3,g_strike1_l2,g_strike1_l2,g_strike1_l1,g_strike1_l1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike1_l_list)==3: self.hitting = True
                                self.img = self.strike1_l_list.pop()
                        elif self.striking_ch == 'leap':
                            if self.leap_back_list == []:
                                self.time = 1; self.falling = True
                                self.leap_back_list = [g_leap_back5,g_leap_back5,g_leap_back4,g_leap_back4,g_leap_back3,g_leap_back3,g_leap_back2,g_leap_back2,g_leap_back1,g_leap_back1]
                                self.striking_ch = None; self.striking = False
                            else:
                                self.pos = (self.pos[0]+5,self.pos[1]-(1.5/self.time)**2)
                                self.time += 1
                                self.img = self.leap_back_list.pop()
                        elif self.striking_ch == 'b_l':
                            if self.block_l_list == []:
                                self.block_l_list = [g_block3_l,g_block3_l,g_block3_l,g_block3_l,g_block3_l,g_block3_l,g_block2_l,g_block2_l,g_block1_l,g_block1_l]
                                self.striking_ch = None; self.striking = False; self.blocking = False
                            else:
                                self.blocking = True
                                self.img = self.block_l_list.pop()
                        elif self.striking_ch == 'l_2':
                            if self.strike2_l_list == []:
                                self.strike2_l_list = [g_strike2_l10,g_strike2_l10,g_strike2_l9,g_strike2_l9,g_strike2_l8,g_strike2_l8,g_strike2_l7,g_strike2_l7,g_strike2_l6,g_strike2_l6,g_strike2_l5,g_strike2_l5,g_strike2_l4,g_strike2_l4,g_strike2_l3,g_strike2_l3,g_strike2_l2,g_strike2_l2,g_strike2_l1,g_strike2_l1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike2_l_list)==3: self.hitting = True
                                self.img = self.strike2_l_list.pop()
                        elif self.striking_ch == 'j_l':
                            if self.jump_strike_l_list == []:
                                self.time = 1; self.falling = True
                                self.jump_strike_l_list = [g_jump_strike_l6,g_jump_strike_l6,g_jump_strike_l5,g_jump_strike_l5,g_jump_strike_l4,g_jump_strike_l4,g_jump_strike_l3,g_jump_strike_l3,g_jump_strike_l2,g_jump_strike_l2,g_jump_strike_l1,g_jump_strike_l1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                self.pos = (self.pos[0]-2,self.pos[1]-(1.5/self.time)**2)
                                self.time += 1
                                if len(self.jump_strike_l_list)==3: self.hitting = True
                                self.img = self.jump_strike_l_list.pop()
                            
                        elif self.striking_ch == 'r_1':
                            if self.strike1_r_list == []:
                                self.strike1_r_list = [g_strike1_r7,g_strike1_r7,g_strike1_r6,g_strike1_r6,g_strike1_r5,g_strike1_r5,g_strike1_r4,g_strike1_r4,g_strike1_r3,g_strike1_r3,g_strike1_r2,g_strike1_r2,g_strike1_r1,g_strike1_r1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                if len(self.strike1_r_list)==3: self.hitting = True
                                self.img = self.strike1_r_list.pop()
                        elif self.striking_ch == 'b_r':
                            if self.block_r_list == []:
                                self.block_r_list = [g_block3_r,g_block3_r,g_block3_r,g_block3_r,g_block3_r,g_block3_r,g_block2_r,g_block2_r,g_block1_r,g_block1_r]
                                self.striking_ch = None; self.striking = False; self.blocking = False
                            else:
                                self.blocking = True
                                self.img = self.block_r_list.pop()
                        elif self.striking_ch == 'j_r':
                            if self.jump_strike_r_list == []:
                                self.time = 1; self.falling = True
                                self.jump_strike_r_list = [g_jump_strike_r6,g_jump_strike_r6,g_jump_strike_r5,g_jump_strike_r5,g_jump_strike_r4,g_jump_strike_r4,g_jump_strike_r3,g_jump_strike_r3,g_jump_strike_r2,g_jump_strike_r2,g_jump_strike_r1,g_jump_strike_r1]
                                self.striking_ch = None; self.striking = False; self.hitting = False
                            else:
                                self.pos = (self.pos[0]+2,self.pos[1]-(1.5/self.time)**2)
                                self.time += 1
                                if len(self.jump_strike_r_list)==3: self.hitting = True
                                self.img = self.jump_strike_r_list.pop()

                # IDLE
                else:

                    # HERO SPOTTED
                    if self.current_plat == H.current_plat:
                        self.back = False
                        if self.is_scared:
                            if H.pos[0]+150<self.pos[0]+150:
                                if self.face_r: self.ch = 'walk'
                                else: self.ch = 'turn'
                            else:
                                if self.face_l: self.ch = 'walk'
                                else: self.ch = 'turn'
                            if H.pos[0]+150>self.pos[0]+450 or H.pos[0]+150<self.pos[0]-200:
                                self.is_scared = False
                                
                        else:
                            if self.pos[0]+60<H.pos[0]+150 and self.pos[0]+100>H.pos[0]+150 and not self.striking:
                                if self.face_l: self.striking = True; self.ch = None
                                else: self.ch = 'turn'
                            elif self.pos[0]+200<H.pos[0]+150 and self.pos[0]+240>H.pos[0]+150 and not self.striking:
                                if self.face_r: self.striking = True; self.ch = None
                                else: self.ch = 'turn'
                            if H.pos[0]+110<self.pos[0]:
                                if self.face_r: self.ch = 'turn'
                                else: self.ch = 'walk'
                            elif H.pos[0]+190>self.pos[0]+150 and H.pos[0]+190<self.pos[0]+170:
                                if self.face_l: self.striking = True; self.striking_ch = 'leap'; self.ch = None
                                else: self.ch = 'walk'
                            elif H.pos[0]+190>self.pos[0]+150:
                                if self.face_l: self.ch = 'turn'
                                else: self.ch = 'walk'
                            else: self.ch = 'walk'
                        
                    elif self.current_plat != H.current_plat:
                        if H.pos[1] > self.pos[1]: self.back = True
                        if self.turn_time == self.turn_limit:
                            self.ch = random.choice(['walk','stand','taunt','turn'])
                            self.turn_time = 1
                    
                    if self.ch == 'walk':

                        if self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][1] and self.face_r or +\
                            self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][0] and self.face_l:
                            
                            self.is_scared = False

                            if self.current_plat != H.current_plat:
                                self.back = True
                                self.ch = random.choice(['stand','turn'])
                            else:
                                if self.face_l:
                                    if self.stand_list_l == []:
                                        self.stand_list_l = [g_stand_l5,g_stand_l5,g_stand_l5,g_stand_l4,g_stand_l4,g_stand_l4,g_stand_l3,g_stand_l3,g_stand_l3,g_stand_l2,g_stand_l2,g_stand_l2,g_stand_l1,g_stand_l1,g_stand_l1]
                                    else: self.img = self.stand_list_l.pop()
                                else:
                                    if self.stand_list_r == []:
                                        self.stand_list_r = [g_stand_r5,g_stand_r5,g_stand_r5,g_stand_r4,g_stand_r4,g_stand_r4,g_stand_r3,g_stand_r3,g_stand_r3,g_stand_r2,g_stand_r2,g_stand_r2,g_stand_r1,g_stand_r1,g_stand_r1]
                                    else: self.img = self.stand_list_r.pop()
                        else:
                            if self.face_l:
                                if self.start_walking_l == []:
                                    if self.walk_l_list == []:
                                        self.walk_l_list = [g_walking11_l,g_walking11_l,g_walking11_l,g_walking10_l,g_walking10_l,g_walking10_l,g_walking9_l,g_walking9_l,g_walking9_l,g_walking8_l,g_walking8_l,g_walking8_l,g_walking7_l,
                                                            g_walking7_l,g_walking7_l,g_walking6_l,g_walking6_l,g_walking6_l,g_walking5_l,g_walking5_l,g_walking5_l,g_walking4_l,g_walking4_l,g_walking4_l,g_walking3_l,g_walking3_l,g_walking3_l,]
                                    else: self.img = self.walk_l_list.pop()
                                else: self.img = self.start_walking_l.pop()
                                if self.is_scared: m = -3
                                else: m = -2
                            else:
                                if self.start_walking_r == []:
                                    if self.walk_r_list == []:
                                        self.walk_r_list = [g_walking11_r,g_walking11_r,g_walking11_r,g_walking10_r,g_walking10_r,g_walking10_r,g_walking9_r,g_walking9_r,g_walking9_r,g_walking8_r,g_walking8_r,g_walking8_r,g_walking7_r,
                                                            g_walking7_r,g_walking7_r,g_walking6_r,g_walking6_r,g_walking6_r,g_walking5_r,g_walking5_r,g_walking5_r,g_walking4_r,g_walking4_r,g_walking4_r,g_walking3_r,g_walking3_r,g_walking3_r,]
                                    else: self.img = self.walk_r_list.pop()
                                else: self.img = self.start_walking_r.pop()
                                if self.is_scared: m = 3
                                else: m = 2

                            self.pos = (self.pos[0]+m,self.pos[1])
                        
                    elif self.ch == 'stand':
                        if self.face_l:
                            if self.stand_list_l == []:
                                self.stand_list_l = [g_stand_l5,g_stand_l5,g_stand_l5,g_stand_l4,g_stand_l4,g_stand_l4,g_stand_l3,g_stand_l3,g_stand_l3,g_stand_l2,g_stand_l2,g_stand_l2,g_stand_l1,g_stand_l1,g_stand_l1]
                            else: self.img = self.stand_list_l.pop()
                        else:
                            if self.stand_list_r == []:
                                self.stand_list_r = [g_stand_r5,g_stand_r5,g_stand_r5,g_stand_r4,g_stand_r4,g_stand_r4,g_stand_r3,g_stand_r3,g_stand_r3,g_stand_r2,g_stand_r2,g_stand_r2,g_stand_r1,g_stand_r1,g_stand_r1]
                            else: self.img = self.stand_list_r.pop()

                    elif self.ch == 'taunt':
                        if self.face_l:
                            if self.taunt_l_list == []:
                                self.start_walking_l = [g_walking1_l,g_walking1_l,g_walking1_l,g_walking2_l,g_walking2_l,g_walking2_l]
                                self.taunt_l_list = [g_taunt_l14,g_taunt_l14,g_taunt_l13,g_taunt_l13,g_taunt_l12,g_taunt_l12,g_taunt_l11,g_taunt_l11,g_taunt_l10,g_taunt_l10,g_taunt_l9,g_taunt_l9,g_taunt_l8,g_taunt_l8,
                                                     g_taunt_l7,g_taunt_l7,g_taunt_l6,g_taunt_l6,g_taunt_l5,g_taunt_l5,g_taunt_l4,g_taunt_l4,g_taunt_l3,g_taunt_l3,g_taunt_l2,g_taunt_l2,g_taunt_l1,g_taunt_l1]
                                self.ch = 'walk'
                            else: self.img = self.taunt_l_list.pop()
                        else:
                            if self.taunt_r_list == []:
                                self.start_walking_r = [g_walking1_r,g_walking1_r,g_walking1_r,g_walking2_r,g_walking2_r,g_walking2_r]
                                self.taunt_r_list = [g_taunt_r14,g_taunt_r14,g_taunt_r13,g_taunt_r13,g_taunt_r12,g_taunt_r12,g_taunt_r11,g_taunt_r11,g_taunt_r10,g_taunt_r10,g_taunt_r9,g_taunt_r9,g_taunt_r8,g_taunt_r8,
                                                     g_taunt_r7,g_taunt_r7,g_taunt_r6,g_taunt_r6,g_taunt_r5,g_taunt_r5,g_taunt_r4,g_taunt_r4,g_taunt_r3,g_taunt_r3,g_taunt_r2,g_taunt_r2,g_taunt_r1,g_taunt_r1]
                                self.ch = 'walk'
                            else: self.img = self.taunt_r_list.pop()
                    elif self.ch == 'turn':
                        if self.face_l:
                            if self.l_turn_r_list == []:
                                self.r_turn_l_list = [g_turn1, g_turn1, g_turn1, g_turn2, g_turn2, g_turn2, g_turn3, g_turn3, g_turn3]
                                self.ch = random.choice(['walk','stand','taunt'])
                                self.face_r = True
                                self.face_l = False
                            else: self.img = self.l_turn_r_list.pop()
                        else:
                            if self.r_turn_l_list == []:
                                self.l_turn_r_list = [g_turn3, g_turn3, g_turn3, g_turn2, g_turn2, g_turn2, g_turn1, g_turn1, g_turn1]
                                self.ch = random.choice(['walk','stand','taunt'])
                                self.face_r = False
                                self.face_l = True
                            else: self.img = self.r_turn_l_list.pop()
                    else: self.ch = 'stand'
                            
                self.turn_time += 1
                
            else:
                self.falling = True
        

class Hero(object):
    def __init__(self, pos):
        self.pos = pos
        self.img = stand1
        self.is_talking = False
        self.is_waiting = False
        self.travelling = False
        self.falling = True
        self.landing = False
        self.jumping = False
        self.jump_move = False
        self.on_edge = False
        self.striking = False
        self.jump_striking = False
        self.blocking = False
        self.knock_back = False
        self.blocked = False
        self.hurt = False
        self.climbing = False
        self.hitting = False
        self.on_wall = False
        self.ch = None
        self.graphic_ch = None
        
        self.graphic = None
        self.graphic_pos = None
        
        self.leaping_back = False
        self.leaping_forward = False
        self.is_running_l = False
        self.is_running_r = False
        self.face_r = True
        self.face_l = False
        self.turning_r_l = False
        self.turning_l_r = False

        self.switching = False
        self.sword_out = False
        
        self.time = 1
        self.hurt_time = 1
        self.block_time = 1
        self.current_plat = None

        self.face_r_list = [stand1,stand1,stand1,stand1,stand2,stand2,stand2,stand2,stand3,stand3,stand3,stand3,stand4,stand4,stand4,stand4]
        self.face_l_list = [stand5,stand5,stand5,stand5,stand6,stand6,stand6,stand6,stand7,stand7,stand7,stand7,stand8,stand8,stand8,stand8]
        
        self.turning_r_l_list = [turn3,turn3,turn2,turn2,turn1,turn1]
        self.turning_l_r_list = [turn6,turn6,turn5,turn5,turn4,turn4]
        
        self.landing_r_list = [landing_r3, landing_r3, landing_r3, landing_r2, landing_r2, landing_r2, landing_r1, landing_r1]
        self.landing_l_list = [landing_l3, landing_l3, landing_l3, landing_l2, landing_l2, landing_l2, landing_l1, landing_l1]

        self.landing_r_sword = [sword_landing_r2,sword_landing_r2,sword_landing_r2,sword_landing_r1,sword_landing_r1,sword_landing_r1]
        self.landing_l_sword = [sword_landing_l2,sword_landing_l2,sword_landing_l2,sword_landing_l1,sword_landing_l1,sword_landing_l1]

        self.turn_running_r = [turn_running_r4,turn_running_r4,turn_running_r3,turn_running_r3,turn_running_r2,turn_running_r2,turn_running_r1,turn_running_r1]
        self.turn_running_l = [turn_running_l4,turn_running_l4,turn_running_l3,turn_running_l3,turn_running_l2,turn_running_l2,turn_running_l1,turn_running_l1]

        self.turn_sword_walk_r = [sword_walk_r2,sword_walk_r2,sword_walk_r2,sword_walk_r1,sword_walk_r1,sword_walk_r1]
        self.turn_sword_walk_l = [sword_walk_l2,sword_walk_l2,sword_walk_l2,sword_walk_l1,sword_walk_l1,sword_walk_l1]

        self.running_r = [running_r8,running_r8,running_r8,running_r7,running_r7,running_r7,running_r6,running_r6,running_r6,running_r5,running_r5,running_r5,
                          running_r4,running_r4,running_r4,running_r3,running_r3,running_r3,running_r2,running_r2,running_r2,running_r1,running_r1,running_r1]

        self.running_l = [running_l8,running_l8,running_l8,running_l7,running_l7,running_l7,running_l6,running_l6,running_l6,running_l5,running_l5,running_l5,
                          running_l4,running_l4,running_l4,running_l3,running_l3,running_l3,running_l2,running_l2,running_l2,running_l1,running_l1,running_l1]

        self.sword_walking_r = [sword_walk_r10,sword_walk_r10,sword_walk_r10,sword_walk_r9,sword_walk_r9,sword_walk_r9,sword_walk_r8,sword_walk_r8,sword_walk_r8,
                                sword_walk_r7,sword_walk_r7,sword_walk_r7,sword_walk_r6,sword_walk_r6,sword_walk_r6,sword_walk_r5,sword_walk_r5,sword_walk_r5,sword_walk_r4,sword_walk_r4,sword_walk_r4,
                                sword_walk_r3,sword_walk_r3,sword_walk_r3]
        self.sword_walking_l = [sword_walk_l10,sword_walk_l10,sword_walk_l10,sword_walk_l9,sword_walk_l9,sword_walk_l9,sword_walk_l8,sword_walk_l8,sword_walk_l8,
                                sword_walk_l7,sword_walk_l7,sword_walk_l7,sword_walk_l6,sword_walk_l6,sword_walk_l6,sword_walk_l5,sword_walk_l5,sword_walk_l5,sword_walk_l4,sword_walk_l4,sword_walk_l4,
                                sword_walk_l3,sword_walk_l3,sword_walk_l3]

        self.stop_running_r = [stop_running_r1,stop_running_r2]
        self.stop_running_l = [stop_running_l1,stop_running_l2]

        self.sword_r_list = [sword_r4,sword_r4,sword_r4,sword_r4,sword_r3,sword_r3,sword_r3,sword_r3,sword_r2,sword_r2,sword_r2,sword_r2,sword_r1,sword_r1,sword_r1,sword_r1,]
        self.sword_l_list = [sword_l4,sword_l4,sword_l4,sword_l4,sword_l3,sword_l3,sword_l3,sword_l3,sword_l2,sword_l2,sword_l2,sword_l2,sword_l1,sword_l1,sword_l1,sword_l1]
        self.sword_turning_r_l = [sword_turn_rl3,sword_turn_rl3,sword_turn_rl2,sword_turn_rl2,sword_turn_rl1,sword_turn_rl1]
        self.sword_turning_l_r = [sword_turn_lr3,sword_turn_lr3,sword_turn_lr2,sword_turn_lr2,sword_turn_lr1,sword_turn_lr1]

        self.draw_sword_r = [draw_swordr9,draw_swordr8,draw_swordr7,draw_swordr6,draw_swordr6,draw_swordr5,draw_swordr5,draw_swordr4,draw_swordr4,draw_swordr3,draw_swordr3,draw_swordr2,draw_swordr2,draw_swordr1,draw_swordr1]
        self.draw_sword_l = [draw_swordl9,draw_swordl8,draw_swordl7,draw_swordl6,draw_swordl6,draw_swordl5,draw_swordl5,draw_swordl4,draw_swordl4,draw_swordl3,draw_swordl3,draw_swordl2,draw_swordl2,draw_swordl1,draw_swordl1]

        self.put_away_r = [sword_awayr10,sword_awayr10,sword_awayr9,sword_awayr9,sword_awayr8,sword_awayr8,sword_awayr7,sword_awayr7,sword_awayr6,sword_awayr6,sword_awayr5,sword_awayr5,sword_awayr4,sword_awayr4,sword_awayr3,sword_awayr3,sword_awayr2,sword_awayr2,sword_awayr1,sword_awayr1]
        self.put_away_l = [sword_awayl10,sword_awayl10,sword_awayl9,sword_awayl9,sword_awayl8,sword_awayl8,sword_awayl7,sword_awayl7,sword_awayl6,sword_awayl6,sword_awayl5,sword_awayl5,sword_awayl4,sword_awayl4,sword_awayl3,sword_awayl3,sword_awayl2,sword_awayl2,sword_awayl1,sword_awayl1]

        self.leap_forward_r = [leap_forward_r5,leap_forward_r5,leap_forward_r4,leap_forward_r4,leap_forward_r3,leap_forward_r3,leap_forward_r2,leap_forward_r2,leap_forward_r1,leap_forward_r1]
        self.leap_back_r = [leap_back_r4,leap_back_r4,leap_back_r3,leap_back_r3,leap_back_r2,leap_back_r2,leap_back_r1,leap_back_r1]
        self.leap_forward_l = [leap_forward_l5,leap_forward_l5,leap_forward_l4,leap_forward_l4,leap_forward_l3,leap_forward_l3,leap_forward_l2,leap_forward_l2,leap_forward_l1,leap_forward_l1]
        self.leap_back_l = [leap_back_l4,leap_back_l4,leap_back_l3,leap_back_l3,leap_back_l2,leap_back_l2,leap_back_l1,leap_back_l1]

        self.block_r = [block_r3,block_r3,block_r2,block_r2,block_r1,block_r1]
        self.block_l = [block_l3,block_l3,block_l2,block_l2,block_l1,block_l1]

        self.blocked_r = [blocked_r5,blocked_r5,blocked_r4,blocked_r4,blocked_r3,blocked_r3,blocked_r2,blocked_r2,blocked_r1,blocked_r1] 
        self.blocked_l = [blocked_l5,blocked_l5,blocked_l4,blocked_l4,blocked_l3,blocked_l3,blocked_l2,blocked_l2,blocked_l1,blocked_l1]
    
        self.block_graph1 = [block_graph1_4,block_graph1_3,block_graph1_2,block_graph1_1]
        self.block_graph2 = [block_graph2_4,block_graph2_3,block_graph2_2,block_graph2_1]
        self.block_graph3 = [block_graph3_4,block_graph3_3,block_graph3_2,block_graph3_1]

        self.blood_graph1 = [blood_graph1_4,blood_graph1_3,blood_graph1_2,blood_graph1_4]
        self.blood_graph2 = [blood_graph2_4,blood_graph2_3,blood_graph2_2,blood_graph2_4]
        self.blood_graph3 = [blood_graph3_4,blood_graph3_3,blood_graph3_2,blood_graph3_4]

        self.bubble_close = []
        self.bubble_open = [b_open6,b_open6,b_open5,b_open5,b_open4,b_open4,b_open3,b_open3,b_open2,b_open2,b_open1,b_open1]
        
        self.climbing_list = [climbing7,climbing7,climbing7,climbing6,climbing6,climbing6,climbing5,climbing5,climbing5,climbing4,climbing4,climbing4,climbing3,climbing3,climbing3,climbing2,climbing2,climbing2,climbing1,climbing1,climbing1]

        
    def shift(self,x,y,current_map):

        self.talking(current_map)

        self.graphic_update()

        if self.switching:
            self.jumping=False
            if self.face_r:
                if self.sword_out == False:
                    if self.draw_sword_r == []:
                        self.draw_sword_r = [draw_swordr9,draw_swordr8,draw_swordr7,draw_swordr6,draw_swordr6,draw_swordr5,draw_swordr5,draw_swordr4,draw_swordr4,draw_swordr3,draw_swordr3,draw_swordr2,draw_swordr2,draw_swordr1,draw_swordr1]
                        self.switching = False
                        self.sword_out = True
                    else: self.img = self.draw_sword_r.pop()
                else:
                    if self.put_away_r == []:
                        self.put_away_r = [sword_awayr10,sword_awayr10,sword_awayr9,sword_awayr9,sword_awayr8,sword_awayr8,sword_awayr7,sword_awayr7,sword_awayr6,sword_awayr6,sword_awayr5,sword_awayr5,sword_awayr4,sword_awayr4,sword_awayr3,sword_awayr3,sword_awayr2,sword_awayr2,sword_awayr1,sword_awayr1]
                        self.switching = False
                        self.sword_out = False
                    else: self.img = self.put_away_r.pop()
            else:
                if self.sword_out == False:
                    if self.draw_sword_l == []:
                        self.draw_sword_l = [draw_swordl9,draw_swordl8,draw_swordl7,draw_swordl6,draw_swordl6,draw_swordl5,draw_swordl5,draw_swordl4,draw_swordl4,draw_swordl3,draw_swordl3,draw_swordl2,draw_swordl2,draw_swordl1,draw_swordl1]
                        self.switching = False
                        self.sword_out = True
                    else: self.img = self.draw_sword_l.pop()
                else:
                    if self.put_away_l == []:
                        self.put_away_l = [sword_awayl10,sword_awayl10,sword_awayl9,sword_awayl9,sword_awayl8,sword_awayl8,sword_awayl7,sword_awayl7,sword_awayl6,sword_awayl6,sword_awayl5,sword_awayl5,sword_awayl4,sword_awayl4,sword_awayl3,sword_awayl3,sword_awayl2,sword_awayl2,sword_awayl1,sword_awayl1]
                        self.switching = False
                        self.sword_out = False
                    else: self.img = self.put_away_l.pop()

        # HURT
        elif self.hurt:
            self.hitting = False; self.striking = False; self.blocking = False; self.blocked = False

            if self.hurt_time>10 or self.jumping or self.falling:
                self.hurt = False
                self.hurt_time = 1
            elif self.on_wall: pass
            else:
                self.hurt_time += 1
                if self.face_l:
                    if self.sword_out: self.img = hurt_l
                    else: self.img = nosword_hurt_l
                else:
                    if self.sword_out: self.img = hurt_r
                    else: self.img = nosword_hurt_r
                        
                
        # S - W - O - R - D
        
        elif self.sword_out:

            if self.blocked:
                self.striking = False; self.hitting = False; self.jump_striking = False; self.ch = None
                if self.face_l:
                    if self.blocked_l == []:
                        self.blocked_l = [blocked_l5,blocked_l5,blocked_l5,blocked_l4,blocked_l4,blocked_l4,blocked_l3,blocked_l3,blocked_l2,blocked_l2,blocked_l1,blocked_l1]
                        self.blocked = False; self.graphic_ch == None
                    else:
                        self.img = self.blocked_l.pop()
                else:
                    if self.blocked_r == []:
                        self.blocked_r = [blocked_r5,blocked_r5,blocked_r5,blocked_r4,blocked_r4,blocked_r4,blocked_r3,blocked_r3,blocked_r2,blocked_r2,blocked_r1,blocked_r1] 
                        self.blocked = False; self.graphic_ch == None
                    else:
                        self.img = self.blocked_r.pop()

            # STRIKE FROM GROUND
            elif self.striking and not self.falling and not self.jumping:
                self.strike()

            # BLOCKING
            elif self.knock_back:
                if self.face_l:
                    if self.block_time == 10:
                        self.knock_back = False; self.graphic_ch == None
                        self.block_time = 1
                    else:
                        self.img = random.choice([blocking2_l1,blocking1_l1])
                        self.block_time += 1
                        x = (1/2)*self.block_time**(1/2)
                else:
                    if self.block_time == 10:
                        self.knock_back = False; self.graphic_ch == None
                        self.block_time = 1
                    else:
                        self.img = random.choice([blocking2_r1,blocking1_r1])
                        self.block_time += 1
                        x = -(1/2)*self.block_time**(1/2)
                x = self.movement_toward_wall(x,y,current_map)
                self.pos = (self.pos[0]+x, self.pos[1])
                self.movement_toward_edge(x,y,current_map)
                if self.block_time > 10: self.block_time = 1
            
            elif self.jump_striking:
                if self.face_r: x=3
                else: x=-3
                x = self.movement_toward_wall(x,y,current_map)
                self.jump_strike(x,y,current_map)
                
            elif self.blocking and self.sword_out:
                self.block()
                
            else:
                    # TURNING 
                if self.pos[0] < self.pos[0]+x or self.turning_l_r:
                    if self.face_l:
                        self.turning_l_r = True
                        self.face_l = False; self.face_r = False
                    elif self.turning_l_r:
                        x = 0
                        self.travelling = False
                        if self.sword_turning_l_r == []:
                            self.turning_l_r = False
                            self.face_r = True
                            self.sword_turning_l_r = [sword_turn_lr3,sword_turn_lr3,sword_turn_lr2,sword_turn_lr2,sword_turn_lr1,sword_turn_lr1]
                        self.img = self.sword_turning_l_r.pop()
                        
                elif self.pos[0] > self.pos[0]+x or self.turning_r_l:
                    if self.face_r:
                        self.turning_r_l = True
                        self.face_l = False; self.face_r = False
                    elif self.turning_r_l:
                        x = 0
                        self.travelling = False
                        if self.sword_turning_r_l == []:
                            self.turning_r_l = False
                            self.face_l = True
                            self.sword_turning_r_l = [sword_turn_rl3,sword_turn_rl3,sword_turn_rl2,sword_turn_rl2,sword_turn_rl1,sword_turn_rl1]
                        self.img = self.sword_turning_r_l.pop()

                    # SWORD OUT WALK
                if self.travelling:

                    if self.face_r: x = 5
                    else: x = -5

                    # WALKING ANIMATION
                    if self.turning_r_l == False and self.face_l:
                        if self.turn_sword_walk_l == []:
                            self.is_running_l = True
                            if self.sword_walking_l == []:
                                self.sword_walking_l = [sword_walk_l10,sword_walk_l10,sword_walk_l10,sword_walk_l9,sword_walk_l9,sword_walk_l9,sword_walk_l8,sword_walk_l8,sword_walk_l8,
                                sword_walk_l7,sword_walk_l7,sword_walk_l7,sword_walk_l6,sword_walk_l6,sword_walk_l6,sword_walk_l5,sword_walk_l5,sword_walk_l5,sword_walk_l4,sword_walk_l4,sword_walk_l4,
                                sword_walk_l3,sword_walk_l3,sword_walk_l3]
                                
                            self.img = self.sword_walking_l.pop()
                            
                        else: self.img = self.turn_sword_walk_l.pop()

                    elif self.turning_l_r == False and self.face_r:
                        if self.turn_sword_walk_r == []:
                            self.is_running_r = True
                            if self.sword_walking_r == []:
                                self.sword_walking_r = [sword_walk_r10,sword_walk_r10,sword_walk_r10,sword_walk_r9,sword_walk_r9,sword_walk_r9,sword_walk_r8,sword_walk_r8,sword_walk_r8,
                                sword_walk_r7,sword_walk_r7,sword_walk_r7,sword_walk_r6,sword_walk_r6,sword_walk_r6,sword_walk_r5,sword_walk_r5,sword_walk_r5,sword_walk_r4,sword_walk_r4,sword_walk_r4,
                                sword_walk_r3,sword_walk_r3,sword_walk_r3]
                                
                            self.img = self.sword_walking_r.pop()
                            
                        else: self.img = self.turn_sword_walk_r.pop()

                    x = self.movement_toward_wall(x,y,current_map)
                    self.movement_toward_edge(x,y,current_map)
                    
                    # SWORD OUT STANDING
                else:
                    if self.face_r:
                        if self.sword_r_list == []:
                            self.sword_r_list = [sword_r4,sword_r4,sword_r4,sword_r4,sword_r3,sword_r3,sword_r3,sword_r3,sword_r2,sword_r2,sword_r2,sword_r2,sword_r1,sword_r1,sword_r1,sword_r1,]
                        self.img = self.sword_r_list.pop()
                        
                    elif self.face_l:
                        if self.sword_l_list == []:
                            self.sword_l_list = [sword_l4,sword_l4,sword_l4,sword_l4,sword_l3,sword_l3,sword_l3,sword_l3,sword_l2,sword_l2,sword_l2,sword_l2,sword_l1,sword_l1,sword_l1,sword_l1]
                        self.img = self.sword_l_list.pop()

                    if self.turn_sword_walk_l == [] or self.turn_sword_walk_r == []:
                        self.turn_sword_walk_r = [sword_walk_r2,sword_walk_r2,sword_walk_r2,sword_walk_r1,sword_walk_r1,sword_walk_r1]
                        self.turn_sword_walk_l = [sword_walk_l2,sword_walk_l2,sword_walk_l2,sword_walk_l1,sword_walk_l1,sword_walk_l1]
                        
                    # LEAPING
                if self.leaping_forward or self.leaping_back:
                    self.jumping = False
                    if self.leaping_forward == True:
                        if self.face_r: x=7
                        else: x=-7
        
                        self.travelling = True
                        
                        if self.face_r:
                            if self.leap_forward_r == []:
                                self.leap_forward_r = [leap_forward_r5,leap_forward_r5,leap_forward_r4,leap_forward_r4,leap_forward_r3,leap_forward_r3,leap_forward_r3,leap_forward_r2,leap_forward_r2,leap_forward_r1,leap_forward_r1]
                                self.leaping_forward = False
                                self.travelling = False
                                self.falling = True
                                if self.time != 1: self.time = 1
                            self.img = self.leap_forward_r.pop()
                        else:
                            if self.leap_forward_l == []:
                                self.leap_forward_l = [leap_forward_l5,leap_forward_l5,leap_forward_l4,leap_forward_l4,leap_forward_l3,leap_forward_l3,leap_forward_l3,leap_forward_l2,leap_forward_l2,leap_forward_l1,leap_forward_l1]
                                self.leaping_forward = False
                                self.travelling = False
                                self.falling = True
                                if self.time != 1: self.time = 1
                            self.img = self.leap_forward_l.pop()

                        x = self.movement_toward_wall(x,y,current_map)
                            
                        if self.pos[0]+150 <= 250 and self.pos[0]>self.pos[0]+x:
                            self.movement_toward_edge(x,y,current_map)
                        elif self.pos[0]+150 >= 650 and self.pos[0]<self.pos[0]+x:
                            self.movement_toward_edge(x,y,current_map)
                        else:
                            self.time +=1
                            self.pos = (self.pos[0]+x, self.pos[1]-(1.5/self.time)**2)
                        
                    elif self.leaping_back == True:
                        if self.face_r: x=-7
                        else: x=7

                        self.travelling = True

                        if self.face_l:
                            if self.leap_back_l == []:
                                self.leap_back_l = [leap_back_l4,leap_back_l4,leap_back_l3,leap_back_l3,leap_back_l2,leap_back_l2,leap_back_l2,leap_back_l1,leap_back_l1]
                                self.leaping_back = False
                                self.travelling = False
                            self.img = self.leap_back_l.pop()
                        else:
                            if self.leap_back_r == []:
                                self.leap_back_r = [leap_back_r4,leap_back_r4,leap_back_r3,leap_back_r3,leap_back_r2,leap_back_r2,leap_back_r2,leap_back_r1,leap_back_r1]
                                self.leaping_back = False
                                self.travelling = False
                            self.img = self.leap_back_r.pop()

                        x = self.movement_toward_wall(x,y,current_map)
                            
                        if self.time == 10:
                            self.falling = True
                            self.time = 1
                        elif self.pos[0]+150 <= 250 and self.pos[0]>self.pos[0]+x:
                            self.movement_toward_edge(x,y,current_map)
                        elif self.pos[0]+150 >= 650 and self.pos[0]<self.pos[0]+x:
                            self.movement_toward_edge(x,y,current_map)
                        else:
                            self.time +=1
                            self.pos = (self.pos[0]+x, self.pos[1]-(1.5/self.time)**2)
                
                    # JUMPING WITH SWORD
                if self.jumping and self.pos[1]+100 <= 150:
                    y = 0
                    self.pos = (self.pos[0], 50)
                    current_map = self.shift_background(current_map, 0, (10/self.time)**2)
                    for g in current_map.gob_list + current_map.dead_list + current_map.P.gob_list: g.pos = (g.pos[0],g.pos[1]+(10/self.time)**2)
                    for k in current_map.map_dict.keys():
                        if k in current_map.wall_dict.keys():
                            current_map.wall_dict[k]['y_range'] = (current_map.wall_dict[k]['y_range'][0]+(10/self.time)**2,current_map.wall_dict[k]['y_range'][1]+(10/self.time)**2)
                        elif k in current_map.climb_dict.keys():
                            current_map.climb_dict[k]['y_range'] = current_map.climb_dict[k]['y_range']+(10/self.time)**2
                        else:
                            current_map.map_dict[k]['img_pos'] = [(i[0],i[1]+(10/self.time)**2) for i in current_map.map_dict[k]['img_pos']]
                            current_map.map_dict[k]['y_range'] = current_map.map_dict[k]['y_range']+(10/self.time)**2

                if self.jumping:
                        
                    self.leaping_forward = False
                    self.leaping_back = False
                    self.on_edge = False
                    
                    if self.travelling == True:
                        if self.face_r: self.img = sword_in_air_r
                        else: self.img = sword_in_air_l
                    else:
                        if self.img != in_air_l or self.img != in_air_r:
                            if self.face_r: self.img = sword_jump_r
                            else: self.img = sword_jump_l

                    if self.time == 10:
                        self.jumping = False
                        self.falling = True
                        self.time = 1
                    else:
                        if self.pos[0]+150 <= 150 or self.pos[0]+150 >= 750: x = 0
                        self.time +=1
                        self.pos = (self.pos[0]+x, self.pos[1]-(15/self.time)**2)
                    if self.time>10: self.time = 1

                elif self.falling:
                    self.fall(x, y, current_map)

                # ON PLATFORM, CALCULATE POS
                elif self.pos[0]+70>current_map.map_dict[self.current_plat]['x_range'][1]-70:
                    if self.face_r:
                        self.img = sword_edge_r
                        self.on_edge = True
                        if self.pos[1] < self.pos[1]+y:
                            self.on_edge = False; self.on_wall = False; self.falling = True
                            self.pos = (self.pos[0]+30, self.pos[1]+10)
                    else:
                        self.on_edge = False
                        if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:
                            self.pos = (self.pos[0] + x, self.pos[1])
                        else:
                            self.falling = True
                            self.current_plat = None
                            
                elif self.pos[0]+230<current_map.map_dict[self.current_plat]['x_range'][0]+70:
                    if self.face_l:
                        self.img = sword_edge_l
                        self.on_edge = True
                        if self.pos[1]< self.pos[1]+y:
                            self.on_edge = False; self.on_wall = False; self.falling = True
                            self.pos = (self.pos[0]-30, self.pos[1]+10)
                    else:
                        self.on_edge = False
                        if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:
                            self.pos = (self.pos[0] + x, self.pos[1])
                        else:
                            self.falling = True
                            self.current_plat = None
                else:
                    if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:
                        if self.on_wall == False: y = 0
                        self.pos = (self.pos[0] + x, self.pos[1] + y)

                    else:
                        self.falling = True
                        self.current_plat = None

                if self.striking: self.strike()

                    # LANDING ANIMATION
                if self.landing == True:
                    if self.face_r:
                        if self.landing_r_sword == []:
                            self.landing = False
                            self.landing_r_sword = [sword_landing_r2,sword_landing_r2,sword_landing_r2,sword_landing_r1,sword_landing_r1,sword_landing_r1]
                        else: self.img = self.landing_r_sword.pop()
                    else:
                        if self.landing_l_sword == []:
                            self.landing = False
                            self.landing_l_sword = [sword_landing_l2,sword_landing_l2,sword_landing_l2,sword_landing_l1,sword_landing_l1,sword_landing_l1]
                        else: self.img = self.landing_l_sword.pop()

        # NO SWORD
        else:
        
            # TURNING 
            if self.pos[0] < self.pos[0]+x or self.turning_l_r:
                if self.face_l:
                    self.turning_l_r = True
                    self.face_l = False; self.face_r = False
                elif self.turning_l_r:
                    x = 0; self.travelling = False
                    if self.turning_l_r_list == []:
                        self.turning_l_r = False
                        self.face_r = True
                        self.turning_l_r_list = [turn6,turn6,turn5,turn5,turn4,turn4]
                    self.img = self.turning_l_r_list.pop()
                    
                    
            elif self.pos[0] > self.pos[0]+x or self.turning_r_l:
                if self.face_r:
                    self.turning_r_l = True
                    self.face_l = False; self.face_r = False
                elif self.turning_r_l:
                    x = 0; self.travelling = False
                    if self.turning_r_l_list == []:
                        self.turning_r_l = False
                        self.face_l = True
                        self.turning_r_l_list = [turn3,turn3,turn2,turn2,turn1,turn1]
                    self.img = self.turning_r_l_list.pop()
                    

            if self.travelling:
                # RUNNING ANIMATION
                if self.turning_r_l == False and self.turning_l_r == False:
                    if self.face_l:
                        if self.turn_running_l == []:
                            self.is_running_l = True
                            if self.running_l == []:
                                self.running_l = [running_l8,running_l8,running_l8,running_l7,running_l7,running_l7,running_l6,running_l6,running_l6,running_l5,running_l5,running_l5,
                                                  running_l4,running_l4,running_l4,running_l3,running_l3,running_l3,running_l2,running_l2,running_l2,running_l1,running_l1,running_l1]
                            self.img = self.running_l.pop()
                        else: self.img = self.turn_running_l.pop()

                    else:
                        if self.turn_running_r == []:
                            self.is_running_r = True
                            if self.running_r == []:
                                self.running_r = [running_r8,running_r8,running_r8,running_r7,running_r7,running_r7,running_r6,running_r6,running_r6,running_r5,running_r5,running_r5,
                                                  running_r4,running_r4,running_r4,running_r3,running_r3,running_r3,running_r2,running_r2,running_r2,running_r1,running_r1,running_r1]
                            self.img = self.running_r.pop()
                        else: self.img = self.turn_running_r.pop()

                    x = self.movement_toward_wall(x,y,current_map)
                    self.movement_toward_edge(x,y,current_map)
                
            # STANDING
            else:
                if self.face_r:
                    if self.face_r_list == []:
                        self.face_r_list = [stand1,stand1,stand1,stand1,stand2,stand2,stand2,stand2,stand3,stand3,stand3,stand3,stand4,stand4,stand4,stand4]
                    self.img = self.face_r_list.pop()
                    
                elif self.face_l:
                    if self.face_l_list == []:
                        self.face_l_list = [stand5,stand5,stand5,stand5,stand6,stand6,stand6,stand6,stand7,stand7,stand7,stand7,stand8,stand8,stand8,stand8]
                    self.img = self.face_l_list.pop()

                if self.is_running_l:
                    if self.stop_running_l == []:
                        self.is_running_l = False;
                        self.stop_running_l = [stop_running_l2,stop_running_l2,stop_running_l1,stop_running_l1]  
                    else: self.img = self.stop_running_l.pop()
                    
                elif self.is_running_r:
                    if self.stop_running_r == []:
                        self.is_running_r = False;
                        self.stop_running_r = [stop_running_r2,stop_running_r2,stop_running_r1,stop_running_r1]
                    else: self.img = self.stop_running_r.pop()
                
                if self.turn_running_l == [] or self.turn_running_r == []:
                    self.turn_running_l = [turn_running_l4,turn_running_l4,turn_running_l3,turn_running_l3,turn_running_l2,turn_running_l2,turn_running_l1,turn_running_l1]
                    self.turn_running_r = [turn_running_r4,turn_running_r4,turn_running_r3,turn_running_r3,turn_running_r2,turn_running_r2,turn_running_r1,turn_running_r1]
                
            # JUMPING
            if self.jumping and self.pos[1]+100 <= 150:
                y = 0
                self.pos = (self.pos[0], 50)
                
                current_map = self.shift_background(current_map, 0, (10/self.time)**2)
                for g in current_map.gob_list + current_map.dead_list + current_map.P.gob_list: g.pos = (g.pos[0],g.pos[1]+(10/self.time)**2)
                for k in current_map.map_dict.keys():
                    if k in current_map.wall_dict.keys():
                        current_map.wall_dict[k]['y_range'] = (current_map.wall_dict[k]['y_range'][0]+(10/self.time)**2,current_map.wall_dict[k]['y_range'][1]+(10/self.time)**2)
                    elif k in current_map.climb_dict.keys():
                        current_map.climb_dict[k]['y_range'] = current_map.climb_dict[k]['y_range']+(10/self.time)**2
                    else:
                        current_map.map_dict[k]['img_pos'] = [(i[0],i[1]+(10/self.time)**2) for i in current_map.map_dict[k]['img_pos']]
                        current_map.map_dict[k]['y_range'] = current_map.map_dict[k]['y_range']+(10/self.time)**2


            if self.jumping:
                self.on_edge = False
                
                if self.travelling or self.jump_move:
                    if self.face_r: self.img = in_air_r
                    else: self.img = in_air_l
                    self.jump_move = True
                elif self.jump_move == False:
                    if self.face_r: self.img = in_air_standing_r
                    else: self.img = in_air_standing_l
                if self.time == 10:
                    self.jumping = False
                    self.jump_move = False
                    self.falling = True
                    self.time = 1
                else:
                    if self.pos[0]+150 <= 150 or self.pos[0]+150 >= 750: x = 0
                    self.time +=1
                    self.pos = (self.pos[0]+x, self.pos[1]-(15/self.time)**2)

            # FALLING
            elif self.falling:
                self.fall(x, y, current_map)

            # CLIMBING
            elif self.climbing:
                self.movement_up_wall(x,y,current_map)
                if self.on_wall:
                    
                    if self.climbing_list == []:
                        self.climbing_list = [climbing7,climbing7,climbing7,climbing6,climbing6,climbing6,climbing5,climbing5,climbing5,climbing4,climbing4,climbing4,climbing3,climbing3,climbing3,climbing2,climbing2,climbing2,climbing1,climbing1,climbing1]
                    self.img = self.climbing_list.pop()

                    self.current_plat = None

                    if self.pos[1]+100 <= 150:
                        y = 0
                        
                        current_map = self.shift_background(current_map, 0, 5)
                        for g in current_map.gob_list + current_map.dead_list + current_map.P.gob_list: g.pos = (g.pos[0],g.pos[1]+5)
                        for k in current_map.map_dict.keys():
                            current_map.map_dict[k]['img_pos'] = [(i[0],i[1]+5) for i in current_map.map_dict[k]['img_pos']]
                            current_map.map_dict[k]['y_range'] = current_map.map_dict[k]['y_range']+5

                    self.pos = (self.pos[0], self.pos[1] + y)

            elif self.climbing == False and self.current_plat == None:
                self.on_wall = False
                self.falling = True

            # ON PLATFORM
            elif self.pos[0]+70>current_map.map_dict[self.current_plat]['x_range'][1]-70:
                if self.face_r:
                    self.img = on_edge_r
                    self.on_edge = True
                    if self.pos[1] < self.pos[1]+y:
                        self.on_edge = False; self.on_wall = False; self.falling = True
                        self.pos = (self.pos[0]+30, self.pos[1]+10)
                else:
                    self.on_edge = False
                    if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:
                        self.pos = (self.pos[0] + x, self.pos[1])
                    else:
                        self.falling = True
                        self.current_plat = None
                        
            elif self.pos[0]+230<current_map.map_dict[self.current_plat]['x_range'][0]+70:
                if self.face_l:
                    self.img = on_edge_l
                    self.on_edge = True
                    if self.pos[1]< self.pos[1]+y:
                        self.on_edge = False; self.on_wall = False; self.falling = True
                        self.pos = (self.pos[0]-30, self.pos[1]+10)
                else:
                    self.on_edge = False
                    if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:
                        self.pos = (self.pos[0] + x, self.pos[1])
                    else:
                        self.falling = True
                        self.current_plat = None
            else:
                if self.pos[0]+70<current_map.map_dict[self.current_plat]['x_range'][1] and self.pos[0]+230>current_map.map_dict[self.current_plat]['x_range'][0]:
                    if self.on_wall == False: y = 0
                    self.pos = (self.pos[0] + x, self.pos[1] + y)

                else:
                    self.falling = True
                    self.current_plat = None

            #LANDING ANIMATION
            if self.landing == True:
                if self.face_r:
                    if self.landing_r_list == []:
                        self.landing = False
                        self.landing_r_list = [landing_r3, landing_r3, landing_r3, landing_r2, landing_r2, landing_r2, landing_r1, landing_r1]
                    else: self.img = self.landing_r_list.pop()
                else:
                    if self.landing_l_list == []:
                        self.landing = False
                        self.landing_l_list = [landing_l3, landing_l3, landing_l3, landing_l2, landing_l2, landing_l2, landing_l1, landing_l1]
                    else: self.img = self.landing_l_list.pop()
        
    def strike(self):
        if self.ch == None:
            if self.falling or self.jumping:
                if self.face_r:
                    self.ch = 'a_r'; self.strike_list = [air_strike_r5,air_strike_r5,air_strike_r4,air_strike_r4,air_strike_r3,air_strike_r3,air_strike_r2,air_strike_r2,air_strike_r1,air_strike_r1]
                else:
                    self.ch = 'a_l'; self.strike_list = [air_strike_l5,air_strike_l5,air_strike_l4,air_strike_l4,air_strike_l3,air_strike_l3,air_strike_l2,air_strike_l2,air_strike_l1,air_strike_l1]
            else:
                if self.face_r:
                    self.ch = random.choice(['r1','r2','r3','r4'])
                    if self.ch == 'r1': self.strike_list = [strike1_r7,strike1_r7,strike1_r6,strike1_r6,strike1_r5,strike1_r5,strike1_r4,strike1_r3,strike1_r2,strike1_r1]
                    elif self.ch == 'r2': self.strike_list = [strike2_r7,strike2_r7,strike2_r6,strike2_r6,strike2_r5,strike2_r5,strike2_r4,strike2_r3,strike2_r2,strike2_r1]
                    elif self.ch == 'r3': self.strike_list = [strike3_r5,strike3_r5,strike3_r4,strike3_r4,strike3_r3,strike3_r3,strike3_r2,strike3_r2,strike3_r1,strike3_r1]
                    else: self.strike_list = [strike4_r7,strike4_r7,strike4_r6,strike4_r6,strike4_r5,strike4_r5,strike4_r4,strike4_r4,strike4_r3,strike4_r3,strike4_r2,strike4_r1]

                else:
                    self.ch = random.choice(['l1','l2','l3','l4'])
                    if self.ch == 'l1': self.strike_list = [strike1_l7,strike1_l7,strike1_l6,strike1_l6,strike1_l5,strike1_l5,strike1_l4,strike1_l3,strike1_l2,strike1_l1]
                    elif self.ch == 'l2': self.strike_list = [strike2_l7,strike2_l7,strike2_l6,strike2_l6,strike2_l5,strike2_l5,strike2_l4,strike2_l3,strike2_l2,strike2_l1]
                    elif self.ch == 'l3': self.strike_list = [strike3_l5,strike3_l5,strike3_l4,strike3_l4,strike3_l3,strike3_l3,strike3_l2,strike3_l2,strike3_l1,strike3_l1]
                    else: self.strike_list = [strike4_l7,strike4_l7,strike4_l6,strike4_l6,strike4_l5,strike4_l5,strike4_l4,strike4_l4,strike4_l3,strike4_l3,strike4_l2,strike4_l1]

        else:
            if self.strike_list == []:
                self.ch = None; self.striking = False
                self.hitting = False
            else:
                if len(self.strike_list)<3:
                    self.hitting = True
                self.img = self.strike_list.pop()
                
    def jump_strike(self, x, y, current_map):
        if self.time>5: self.time = 1
        if self.ch == None:
            if self.face_r:
                self.ch = random.choice(['r1','r2'])
                if self.ch == 'r1': self.strike_list = [jump_strike1_r7,jump_strike1_r7,jump_strike1_r6,jump_strike1_r6,jump_strike1_r5,jump_strike1_r5,jump_strike1_r4,jump_strike1_r4,jump_strike1_r3,jump_strike1_r3,jump_strike1_r2,jump_strike1_r2,jump_strike1_r1,jump_strike1_r1]
                else: self.strike_list = [jump_strike2_r6,jump_strike2_r6,jump_strike2_r5,jump_strike2_r5,jump_strike2_r4,jump_strike2_r4,jump_strike2_r3,jump_strike2_r3,jump_strike2_r2,jump_strike2_r2,jump_strike2_r1,jump_strike2_r1]

            else:
                self.ch = random.choice(['l1','l2'])
                if self.ch == 'l1': self.strike_list = [jump_strike1_l7,jump_strike1_l7,jump_strike1_l6,jump_strike1_l6,jump_strike1_l5,jump_strike1_l5,jump_strike1_l4,jump_strike1_l4,jump_strike1_l3,jump_strike1_l3,jump_strike1_l2,jump_strike1_l2,jump_strike1_l1,jump_strike1_l1]
                else: self.strike_list = [jump_strike2_l6,jump_strike2_l6,jump_strike2_l5,jump_strike2_l5,jump_strike2_l4,jump_strike2_l4,jump_strike2_l3,jump_strike2_l3,jump_strike2_l2,jump_strike2_l2,jump_strike2_l1,jump_strike2_l1]
        else:
            if self.strike_list == []:
                self.ch = None; self.jump_striking = False; self.hitting = False
                
            else:
                self.img = self.strike_list.pop()
                
                if len(self.strike_list)<3:
                    self.hitting = True
                    
                if self.time == 5:
                    self.falling = True
                    self.time = 1
                elif self.pos[0]+150 <= 250 and self.pos[0]>self.pos[0]+x:
                    self.movement_toward_edge(x,y,current_map)
                elif self.pos[0]+150 >= 650 and self.pos[0]<self.pos[0]+x:
                    self.movement_toward_edge(x,y,current_map)
                else:
                    self.time +=1
                    self.pos = (self.pos[0]+x, self.pos[1]-(1.5/self.time)**2)
                    
    def block(self):
        if self.face_r:
            if self.block_r == []:
                self.img = block_r3
            else: self.img = self.block_r.pop()
        else:
            if self.block_l == []:
                self.img = block_l3
            else: self.img = self.block_l.pop()
            
    def refresh_block(self):
        self.block_r = [block_r3,block_r3,block_r2,block_r2,block_r1,block_r1]
        self.block_l = [block_l3,block_l3,block_l2,block_l2,block_l1,block_l1]

    def leap_right(self):
        if self.face_r:
            self.leaping_forward = True
        else:
            self.leaping_back = True
        
    def leap_left(self):
        if self.face_r:
            self.leaping_back = True
        else:
            self.leaping_forward = True

    def switch(self):
        if self.jumping == False and self.falling == False or self.sword_out:
            self.switching = True

    def fall(self, x, y, current_map):
        if self.sword_out == False:
            if self.face_r: self.img = in_air_standing_r2
            else: self.img = in_air_standing_l2
        else:
            if self.face_r: self.img = sword_in_air_r
            else: self.img = sword_in_air_l
        
        y = 5*self.time + self.pos[1]
        if self.time < 4: self.time +=1
                
        if self.pos[1]+350 >= 600:
            self.pos = (self.pos[0], 250)

            current_map = self.shift_background(current_map, 0, -2*self.time*5)
            for g in current_map.gob_list + current_map.dead_list + current_map.P.gob_list: g.pos = (g.pos[0],g.pos[1]-2*self.time*5)
            for k in current_map.map_dict.keys():
                if k in current_map.wall_dict.keys():
                    current_map.wall_dict[k]['y_range'] = (current_map.wall_dict[k]['y_range'][0]-2*self.time*5,current_map.wall_dict[k]['y_range'][1]-2*self.time*5)
                elif k in current_map.climb_dict.keys():
                    current_map.climb_dict[k]['y_range'] = current_map.climb_dict[k]['y_range']-2*self.time*5
                else:
                    current_map.map_dict[k]['img_pos'] = [(i[0],i[1]-2*self.time*5) for i in current_map.map_dict[k]['img_pos']]
                    current_map.map_dict[k]['y_range'] = current_map.map_dict[k]['y_range']-2*self.time*5
    
        
        for k in current_map.map_dict.keys():
            if self.pos[1]+200<current_map.map_dict[k]['y_range'] and self.pos[1]+320>current_map.map_dict[k]['y_range']:
                if self.pos[0]+90<current_map.map_dict[k]['x_range'][1] and self.pos[0]+200>current_map.map_dict[k]['x_range'][0]:
                    if k not in current_map.climb_dict.keys():
                        y = current_map.map_dict[k]['y_range']-260
                        self.current_plat = k
                        self.jumping = False
                        self.falling = False
                        self.landing = True
                        self.time = 1

        self.pos = (self.pos[0] + x/2, y)

    def movement_toward_wall(self, x, y, current_map):
        for wall in current_map.wall_dict.keys():
            if self.pos[0]+x<self.pos[0]:
                if self.pos[0]+100<=current_map.wall_dict[wall]['x_range'][0] and self.pos[0]+150>=current_map.wall_dict[wall]['x_range'][1]:
                    if self.pos[1]+200<current_map.wall_dict[wall]['y_range'][0] and self.pos[1]+150>=current_map.wall_dict[wall]['y_range'][1]:
                        x = 0
            elif self.pos[0]+x>self.pos[0]:
                if self.pos[0]+150<=current_map.wall_dict[wall]['x_range'][0] and self.pos[0]+200>=current_map.wall_dict[wall]['x_range'][1]:
                    if self.pos[1]+200<current_map.wall_dict[wall]['y_range'][0] and self.pos[1]+150>=current_map.wall_dict[wall]['y_range'][1]:
                        x = 0
        return x

    def movement_toward_edge(self, x, y, current_map):
        m = 0
            
        if self.on_edge == False:
            if self.pos[0]+150 <= 250 and self.pos[0]>self.pos[0]+x:
                self.pos = (100, self.pos[1])
                if self.jump_striking: m = 3
                elif self.sword_out == False: m = 10
                else: m = 7

            elif self.pos[0]+150 >= 650 and self.pos[0]<self.pos[0]+x:
                self.pos = (500, self.pos[1])
                if self.jump_striking: m = -3
                elif self.sword_out == False: m = -10
                else: m = -7

        current_map = self.shift_background(current_map, m, 0)
        for g in current_map.gob_list + current_map.dead_list + current_map.P.gob_list: g.pos = (g.pos[0]+m,g.pos[1]) 
        for k in current_map.map_dict.keys():
            if k in current_map.wall_dict.keys():
                current_map.wall_dict[k]['x_range'] = (current_map.wall_dict[k]['x_range'][0]+m,current_map.wall_dict[k]['x_range'][1]+m)
            elif k in current_map.climb_dict.keys():
                current_map.climb_dict[k]['x_range'] = (current_map.climb_dict[k]['x_range'][0]+m,current_map.climb_dict[k]['x_range'][1]+m)
            else:
                current_map.map_dict[k]['img_pos'] = [(i[0]+m,i[1]) for i in current_map.map_dict[k]['img_pos']]
                current_map.map_dict[k]['x_range'] = (current_map.map_dict[k]['x_range'][0]+m,current_map.map_dict[k]['x_range'][1]+m)

    def movement_up_wall(self, x, y, current_map):
        for k in current_map.climb_dict.keys():
            if self.pos[0]+150<current_map.climb_dict[k]['x_range'][1]-50 and self.pos[0]+150>current_map.climb_dict[k]['x_range'][0]-50:
                if self.pos[1]+150>current_map.climb_dict[k]['y_range']:
                    self.on_wall = True
                else: self.climbing = False
            else: self.on_wall = False

    def shift_background(self,current_map,x,y):
        
        current_map.background_pos = (current_map.background_pos[0]+x,current_map.background_pos[1]+y)
        if current_map.background2: current_map.background2_pos = (current_map.background2_pos[0]+x/5,current_map.background2_pos[1]+y/5)
        if current_map.background3: current_map.background3_pos = (current_map.background3_pos[0]+x/10,current_map.background3_pos[1]+y/10)
        
        return current_map

    def talking(self, current_map):
        if current_map.textbox.is_message:
            if self.pos[1]+350<=600:
                m = 15
                self.pos = (self.pos[0],self.pos[1]+m)
                current_map = self.shift_background(current_map, 0, m)
                for g in current_map.gob_list + current_map.dead_list + current_map.P.gob_list: g.pos = (g.pos[0],g.pos[1]+m) 
                for k in current_map.map_dict.keys():
                    if k in current_map.wall_dict.keys():
                        current_map.wall_dict[k]['y_range'] = (current_map.wall_dict[k]['y_range'][0]+m,current_map.wall_dict[k]['y_range'][1]+m)
                    elif k in current_map.climb_dict.keys():
                        current_map.climb_dict[k]['y_range'] = current_map.climb_dict[k]['y_range']+m
                    else:
                        current_map.map_dict[k]['img_pos'] = [(i[0],i[1]+m) for i in current_map.map_dict[k]['img_pos']]
                        current_map.map_dict[k]['y_range'] = current_map.map_dict[k]['y_range']+m
        else:
            if self.is_talking:
                current_map.script(self)

    def graphic_update(self):

        if self.knock_back or self.blocked or self.graphic_ch == 'b1' or self.graphic_ch == 'b2' or self.graphic_ch == 'b3':
            if self.graphic_ch == None:
                self.graphic_ch = random.choice(['b1','b2','b3'])
            if self.graphic_ch == 'b1':
                if self.block_graph1 == []:
                    self.block_graph1 = [block_graph1_4,block_graph1_3,block_graph1_2,block_graph1_1]
                    self.graphic = None
                else: self.graphic = self.block_graph1.pop()
            elif self.graphic_ch == 'b2':
                if self.block_graph2 == []:
                    self.block_graph2 = [block_graph2_4,block_graph2_3,block_graph2_2,block_graph2_1]
                    self.graphic = None
                else: self.graphic = self.block_graph2.pop()
            else:
                if self.block_graph3 == []:
                    self.block_graph3 = [block_graph3_4,block_graph3_3,block_graph3_2,block_graph3_1]
                    self.graphic = None
                else: self.graphic = self.block_graph3.pop()
            if self.face_r: self.graphic_pos = (self.pos[0]+190, self.pos[1]+130)
            elif self.face_l: self.graphic_pos = (self.pos[0]+100, self.pos[1]+130)
            
            
        elif self.hurt or self.graphic_ch == 'bl1' or self.graphic_ch == 'bl2' or self.graphic_ch == 'bl3':
            if self.graphic_ch == None:
                self.graphic_ch = random.choice(['bl1','bl2','bl3'])
            if self.graphic_ch == 'bl1':
                if self.blood_graph1 == []:
                    self.blood_graph1 = [blood_graph1_4,blood_graph1_4,blood_graph1_3,blood_graph1_3,blood_graph1_2,blood_graph1_4]
                    self.graphic_ch = None; self.graphic = None; self.hurt = False
                else: self.graphic = self.blood_graph1.pop()
            elif self.graphic_ch == 'bl2':
                if self.blood_graph2 == []:
                    self.blood_graph2 = [blood_graph2_4,blood_graph2_4,blood_graph2_3,blood_graph2_3,blood_graph2_2,blood_graph2_4]
                    self.graphic_ch = None; self.graphic = None; self.hurt = False
                else: self.graphic = self.blood_graph2.pop()
            elif self.graphic_ch == 'bl3':
                if self.blood_graph3 == []:
                    self.blood_graph3 = [blood_graph3_4,blood_graph3_4,blood_graph3_3,blood_graph3_3,blood_graph3_2,blood_graph3_4]
                    self.graphic_ch = None; self.graphic = None; self.hurt = False
                else: self.graphic = self.blood_graph3.pop()
            self.graphic_pos = (self.pos[0]+150, self.pos[1]+110)

    def blit(self, screen):
        screen.blit(self.img, self.pos)
        if self.graphic != None:
            screen.blit(self.graphic, self.graphic_pos)
