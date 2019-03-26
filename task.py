import pygame
import requests
import sys
import os

response = None
running = True
pygame.init()
scales = []
scale = 17
coord = [133.795384, -25.694768]
types = ["map", "sat", "sat,skl"]
type = types[0]
while running:
    try:
        scales = [str(scale), str(scale)]
        scaler = ','.join(scales)
        map_request = "http://static-maps.yandex.ru/1.x/?ll=" + str(coord[0]) + "," + str(coord[1]) + "&spn=" + scaler + "&l="+ type +"&z=17"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(geocoder_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
    except:
        print("Запрос не удалось выполнить. Проверьте наличие сети Интернет.")
        print(map_request)
        sys.exit(1)

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.truncate(0)
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == 280:
                if scale < 17:
                    scale += 1
                    print("Now scale = ",str(scale))
            elif event.key == 281:
                if scale > 1:
                    scale -= 1
                    print("Now scale = ", str(scale))
            elif event.key == 273:
                if coord[1] + 0.5 < -21:
                    coord[1] = coord[1] + 0.5 #-21
                    print("Now coord = ", str(coord[1]))
            elif event.key == 274:
                if coord[1] + 0.5 > -29:
                    coord[1] = coord[1] - 0.5 #-29
                    print("Now coord = ", str(coord[1]))
            elif event.key == 276:
                if coord[0] - 0.5 > 130:
                    coord[0] = coord[0] - 0.5 #130
                    print("Now coord = ", str(coord[0]))
            elif event.key == 275:
                if coord[0] + 0.5 < 140:
                    coord[0] = coord[0] + 0.5 #140
                    print("Now coord = ", str(coord[0]))
            elif event.key == 116:
                if type == types[0]:
                    type = types[1]
                elif type == types[1]:
                    type = types[2]
                elif type == types[2]:
                    type = types[0]
pygame.quit()
os.remove(map_file)
#up 280, down 281
# вверх-273 вниз-274 влево-276 вправо-275
