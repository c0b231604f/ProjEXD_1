import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png") #練習１
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    bg_img2 = pg.transform.flip(bg_img, True, False) #練習7－1
    kk_ret = kk_img.get_rect() #練習8－1
    kk_ret.center = [300, 200] #練習8－2
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_ret.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            kk_ret.move_ip((0, 1))
        if key_lst[pg.K_LEFT]:
            kk_ret.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            kk_ret.move_ip((1, 0))
        x = tmr%4800
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0]) #練習7-1
        screen.blit(bg_img, [-x + 3200, 0]) #練習7－2
        screen.blit(bg_img2, [-x + 4800, 0]) #練習7-2

        screen.blit(kk_img, kk_ret) #練習４
        pg.display.update()
        tmr += 1
        clock.tick(200) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()