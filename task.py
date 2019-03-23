import pygame
import requests
import sys
import os

response = None
running = True
coord = []
pygame.init()
scales = []
scale = 26
while running:
    try:
        coord = ["133.795384", "-25.694768"]
        scales = [str(scale), str(scale)]
        scaler = ','.join(scales)
        map_request = "http://static-maps.yandex.ru/1.x/?ll=" + coord[0] + "," + coord[1] + "&spn=" + scaler + "&l=sat&z=17"
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
            if event.key == 280:
                if scale < 30:
                    scale += 1
                    print("Now scale = ",str(scale))
            elif event.key == 281:
                if scale > 1:
                    scale -= 1
                    print("Now scale = ", str(scale))
pygame.quit()
os.remove(map_file)
#up 280, down 281
