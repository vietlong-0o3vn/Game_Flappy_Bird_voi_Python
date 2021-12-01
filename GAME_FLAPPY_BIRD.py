import pygame
pygame.init()

import random

# ham cua tro choi

# san

def hamtaosan():
    manhinhgame.blit(san,(toadoxcuasan,650))
    manhinhgame.blit(san,(toadoxcuasan+432,650))

#ong nuoc

def hamsinhraongnuoc():
    vitringaunhiencuaong = random.choice(chieucaocuaongnuoc)
    ongnuocmoi_benduoi = caiongnuoc.get_rect(midtop =(700,vitringaunhiencuaong))
    ongnuocmoi_bentren = caiongnuoc.get_rect(midtop =(700,vitringaunhiencuaong-800))
    return ongnuocmoi_benduoi, ongnuocmoi_bentren

def hamdichuyenongnuoc(ongnuoc):
    for moiongnuoc in ongnuoc:
        moiongnuoc.centerx -= 5
    return ongnuoc

def hamtaoongnuoc(ongnuoc):
    for moiongnuoc in ongnuoc:
        if moiongnuoc.bottom >= 768:
            manhinhgame.blit(caiongnuoc,moiongnuoc)
        else:
            ongnuocbixoaynguoc = pygame.transform.flip(caiongnuoc,False,True)
            manhinhgame.blit(ongnuocbixoaynguoc,moiongnuoc)

# dong xu

def taovitridongxu():
    phamvicuadongxu.centerx= 450
    phamvicuadongxu.centery= random.randint(200,600)

def anduocdongxu():
    if phamvicuaconchim.colliderect(phamvicuadongxu):
        tiengandongxu.play()
        return True
    return False


#va cham

def xulyvacham(ongnuoc):
    for moiongnuoc in ongnuoc:
        if phamvicuaconchim.colliderect(moiongnuoc):
            tiengvacham.play()
            return False
        if phamvicuaconchim.top <= -75:
            tiengbayquamanhinh.play()
            return False
        if phamvicuaconchim.bottom >= 650:
            tiengroixuong.play()
            return False
    return True

#diem so

def congdiem(ongnuoc):
    diqua = False
    for moiongnuoc in ongnuoc:
        if moiongnuoc.centerx == phamvicuaconchim.centerx:
            tiengtinhdiem.play()
            return True
    return False


def hienthidiem(trangthaigame):
    if trangthaigame == "dang hoat dong":
        diemso = fontchucuagame.render((f"điểm số : {int(diem)}"),True,(255,255,255))
        phamvicuadiemso = diemso.get_rect(center = (216,100))
        manhinhgame.blit(diemso,phamvicuadiemso)
    if trangthaigame == "khong hoat dong":
        diemso = fontchucuagame.render((f"điểm số : {int(diem)}"),True,(255,255,255))
        phamvicuadiemso = diemso.get_rect(center = (216,100))
        manhinhgame.blit(diemso,phamvicuadiemso)
        
        diemsocao = fontchucuagame.render((f"điểm cao : {int(diemcao)}"),True,(255,255,255))
        phamvicuadiemsocao = diemsocao.get_rect(center = (216,620))
        manhinhgame.blit(diemsocao,phamvicuadiemsocao)

def capnhatdiemcao(diem,diemcao):
    if diem > diemcao:
        diemcao = diem
    return diemcao


manhinhgame = pygame.display.set_mode((432,768))
pygame.display.set_caption("Flappy Bird")
khunghinhtrengiay = pygame.time.Clock()
fontchucuagame = pygame.font.Font('arial.ttf',40)


# cac bien tro choi
diem = 0
diemcao = 0 
trongluc = 0.25
trochoihoatdong = True

# hinh nen
hinhnen = pygame.image.load('hinhanh/hinhnen.png')
hinhnen = pygame.transform.scale2x(hinhnen)

# san
san = pygame.image.load('hinhanh/san.png')
san = pygame.transform.scale2x(san)
toadoxcuasan = 0

# con chim
conchim = pygame.image.load('hinhanh/conchim.png')
conchim = pygame.transform.scale2x(conchim)
phamvicuaconchim = conchim.get_rect(center = (150,384))
sudichuyencuaconchim = 0

#dong xu
dongxu = pygame.image.load('hinhanh/dongxu.png')
phamvicuadongxu = dongxu.get_rect(center = (400, 384))

# ong nuoc
caiongnuoc = pygame.image.load('hinhanh/ongnuocxanh.png')
caiongnuoc = pygame.transform.scale2x(caiongnuoc)
danhsachcacongduoctaora = []
chieucaocuaongnuoc = [350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550]
taoraongnuoc = pygame.USEREVENT
pygame.time.set_timer(taoraongnuoc,1200) #thoi gian tao ra ong nuoc 

# man hinh ket thuc
manhinhketthuc = pygame.image.load('hinhanh/manhinhbatdau.png')
manhinhketthuc = pygame.transform.scale2x(manhinhketthuc)
phamvicuamanhinhketthuc = manhinhketthuc.get_rect(center=(216,384))

#am thanh tro choi
tiengconchim = pygame.mixer.Sound('amthanh/tiengconchim.wav')
tiengvacham = pygame.mixer.Sound('amthanh/tiengchamcot.wav')
tiengroixuong = pygame.mixer.Sound('amthanh/tiengroixuong.wav')
tiengbayquamanhinh = pygame.mixer.Sound('amthanh/tiengbayquamanhinh.wav')
tiengandongxu = pygame.mixer.Sound('amthanh/tiengandongxu.wav')
tiengtinhdiem = pygame.mixer.Sound('amthanh/tiengtinhdiem.wav')


#tro choi hoat dong
while True:
    # cac su kien xay ra trong game
    for sukien in pygame.event.get():
        if sukien.type == pygame.QUIT:
            pygame.quit()

        if sukien.type == pygame.KEYDOWN:
            if sukien.key == pygame.K_SPACE and trochoihoatdong:
                sudichuyencuaconchim = 0
                sudichuyencuaconchim -= 8
                tiengconchim.play()
            if sukien.key == pygame.K_SPACE and trochoihoatdong == False:
                trochoihoatdong = True
                danhsachcacongduoctaora.clear()
                phamvicuaconchim.center = (150,384)
                sudichuyencuaconchim = 0
                diem = 0
        if sukien.type == taoraongnuoc:
            danhsachcacongduoctaora.extend(hamsinhraongnuoc())
            
    # phan hien thi len man hinh tro choi
    manhinhgame.blit(hinhnen,(0,0))
    
    if trochoihoatdong:
        # con chim
        sudichuyencuaconchim += trongluc
        phamvicuaconchim.centery += sudichuyencuaconchim
        manhinhgame.blit(conchim,phamvicuaconchim)
        trochoihoatdong = xulyvacham(danhsachcacongduoctaora)
        
        #dong xu
        manhinhgame.blit(dongxu,phamvicuadongxu)
        phamvicuadongxu.centerx -= 1
        if phamvicuadongxu.centerx == 0:
            taovitridongxu()
        #ong nuoc
        danhsachcacongduoctaora = hamdichuyenongnuoc(danhsachcacongduoctaora)
        hamtaoongnuoc(danhsachcacongduoctaora)
        if congdiem(danhsachcacongduoctaora):
            diem += 1
        if anduocdongxu():
            diem += 3
            taovitridongxu()
        hienthidiem("dang hoat dong")
    else:
        manhinhgame.blit(manhinhketthuc,phamvicuamanhinhketthuc)
        diemcao = capnhatdiemcao(diem,diemcao)
        hienthidiem("khong hoat dong")
    
    #san
    toadoxcuasan -= 1
    hamtaosan()
    if toadoxcuasan <= - 432:
        toadoxcuasan = 0
    
    pygame.display.update()
    khunghinhtrengiay.tick(120)
