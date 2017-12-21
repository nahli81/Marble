
# for importing images

from marble_maps import *

pygame.init()

clock = pygame.time.Clock()
FPS = 40
pygame.display.set_caption("Window")



def main():
    
    H = Hero((250,250))
    
##    M = Rocky_Beach()
##    M = Map_cave11()
##    M = Battle_gate1()
    M = Citycity()
        
    x_change = 0; y_change = 0
    left = False; right = False
    up = False; down = False

    
    pygame.display.set_caption('lordof100s')
##    screen = pygame.display.set_mode((800,600) , pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1000,650))

    crashed = False

    while not crashed:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    H.is_talking = True
                    if M.textbox.is_message:
                        M.blit_gobs(screen, M, H)
                        if len(M.textbox.message_list)<1:
                            for g in M.gob_list: g.is_talking = False
                            M.textbox.graphic_ch = 'bubble_close'
                        else: M.textbox.next_message()

                if not M.textbox.is_message:

                    if event.key == pygame.K_SPACE:
                        if H.jumping != True and H.falling != True and H.current_plat != None:
                            H.jumping = True
                    if event.key == pygame.K_a:
                        H.climbing = False
                        left = True
                    if event.key == pygame.K_d:
                        H.climbing = False
                        right = True
                    if event.key == pygame.K_w:
                        H.climbing = True
                        up = True
                    if event.key == pygame.K_s:
                        down = True

                    if event.key == pygame.K_p:
                        if not H.jumping and not H.falling:
                            H.switch()

                    if event.key == pygame.K_e:
                        if not H.falling and not H.jumping and not H.jump_striking and not H.striking:
                            H.blocking = False
                            H.leap_right()
                            
                    if event.key == pygame.K_q:
                        if not H.falling and not H.jumping and not H.jump_striking and not H.striking:
                            H.blocking = False
                            H.leap_left()
                        
                    if event.key == pygame.K_o:
                        if not H.falling and not H.jumping and not H.jump_striking:
                            if H.sword_out:
                                H.blocking = True
                                H.striking = False
                                H.jump_striking = False
                            else: pass
                        
                    if event.key == pygame.K_k:
                        if not H.jump_striking and not H.striking and not H.blocking:
                            H.leaping_forward = False; H.leaping_back = False
                            H.blocking = False
                            H.jump_striking = False
                            H.striking = True

                    if event.key == pygame.K_j:
                        if not H.falling and not H.jumping and not H.jump_striking and not H.striking and not H.blocking:
                            H.blocking = False
                            H.striking = False
                            H.jump_striking = True
                    
            if event.type == pygame.KEYUP:
                if not M.textbox.is_message:
                    H.travelling = False
                    if event.key == pygame.K_r:
                        H.is_talking = False
                    if event.key == pygame.K_a:
                        left = False
                    if event.key == pygame.K_d:
                        right = False
                    if event.key == pygame.K_w:
                        H.climbing = False
                        up = False
                    if event.key == pygame.K_s:
                        down = False
                    if event.key == pygame.K_o:
                        if H.sword_out:
                            H.blocking = False
                            H.refresh_block()
                        else: pass
                        
        if not H.turning_l_r and not H.turning_r_l:    
            if left and right:
                x_change = 0; up = False; down = False; H.travelling = False
            elif left:
                x_change = -10; up = False; down = False; H.travelling = True
            elif right:
                x_change = 10; up = False; down = False; H.travelling = True
            else: x_change = 0; H.travelling = False
            
            if up and down:
                y_change = 0; left = False; right = False
            elif up:
                y_change = -5; left = False; right = False
            elif down:
                y_change = 5; left = False; right = False
            else: y_change = 0

        H.shift(x_change, y_change, M)
        screen.fill((0,0,0))
        if M.background3: screen.blit(M.background3,M.background3_pos)
        if M.background2: screen.blit(M.background2,M.background2_pos)
        screen.blit(M.background,M.background_pos)
##        M.blit_platform(screen)
        M.blit_dead_list(screen, M, H)
        H.blit(screen)
        M.blit_gobs(screen, M, H)


        if M.textbox.is_message:
            M.textbox.blit_current_message(screen)
        
        pygame.display.flip()

if __name__ == '__main__':
    main()
pygame.quit()
quit()
