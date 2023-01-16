import pygame
import numpy as np
import sistema_controlado

class Button:
    def __init__(self,text,width,height,pos,elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos,(width,height)) #criando rect de cima (position),(w,h)
        self.top_color = CINZA# '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = CINZA_ESCURO2
        #text
        self.text_surf = BOTOES_FONTE.render(text,True,BRANCO) #FFFFFF -> Branco
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

        self.pos = pos
        self.width = width
        self.height = height
        self.text = text

    def draw(self):
        #elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(WIN,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(WIN,self.top_color, self.top_rect,border_radius = 12)
        WIN.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = CINZA_ESCURO#'#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    print('click')
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = CINZA#'#475F77'

    def cursor_over_button(self, position):
        #Checa se o mouse esta na posicao do botao em questao
        if position[0] > self.pos[0] and position[0] < self.pos[0] + self.width:
            if position[1] > self.pos[1] and position[1] < self.pos[1] + self.height:
                return True

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 600,700 #Largura e altura da janela 
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #definição de uma janela -surface - window
pygame.display.set_caption("Simulação Pygame Aeropêndulo ")

#Paleta de Cores
BRANCO = (255,255,255)
PRETO = (0,0,0)
CINZA = (128,128,128)
CINZA_ESCURO = (90,90,90)
CINZA_ESCURO2 = (30,30,30)

FPS = 60 #FRAMES PER SECONDS
TEMPO_SIM = 100 #tempo padrão da simulação

AEROPENDULO_LARGURA, AEROPENDULO_ALTURA = 78,425 #Proporção padrão 1.95 por 11.26 (x40)

#Carregando Frames do aeropêndulo que simulam a rotação da hélice
AEROPENDULO_IMAGE_0 = pygame.transform.scale(pygame.image.load('imagens/Frame1.png'),(AEROPENDULO_LARGURA, AEROPENDULO_ALTURA))
AEROPENDULO_IMAGE_1 = pygame.transform.scale(pygame.image.load('imagens/Frame2.png'),(AEROPENDULO_LARGURA, AEROPENDULO_ALTURA))
AEROPENDULO_IMAGE_2 = pygame.transform.scale(pygame.image.load('imagens/Frame3.png'),(AEROPENDULO_LARGURA, AEROPENDULO_ALTURA))
AEROPENDULO_IMAGE_3 = pygame.transform.scale(pygame.image.load('imagens/Frame4.png'),(AEROPENDULO_LARGURA, AEROPENDULO_ALTURA))
AEROPENDULO_IMAGE_4 = pygame.transform.scale(pygame.image.load('imagens/Frame5.png'),(AEROPENDULO_LARGURA, AEROPENDULO_ALTURA))
INICIO_IMG = (150, 50) #distancia do furo para borda
VETOR = pygame.math.Vector2(18, 180.5) # x=dist_x_furo_propria_imagem, y= (altura_img/2) - dist_y_furo_propria_imagem


BOTOES_FONTE = pygame.font.SysFont('Calibri',30)
POS_COMECAR = (10,600)
POS_BOTAO = (10,500)
POS_ENTRADA = (250,500)
POS_ENTRADA2 = (250,600)

BotaoComecar = Button('Comecar',200,80,POS_BOTAO,5)
BotaoZerar = Button('Zerar Angulo',200,80,(POS_BOTAO[0], POS_BOTAO[1]+100),5)

def draw_window(imagem_aeropendulo, retangulo_aeropendulo, angulo_input_str, angulo_atual):
    WIN.fill(BRANCO)
    BotaoComecar.draw()
    BotaoZerar.draw()
    WIN.blit(imagem_aeropendulo, retangulo_aeropendulo) #expõe a imagem do aeropendulo

    entrada_texto = BOTOES_FONTE.render("Ângulo Desejado: " + angulo_input_str + "°", 1, PRETO)
    WIN.blit(entrada_texto, POS_ENTRADA)

    entrada_texto2 = BOTOES_FONTE.render("Ângulo Atual: " + angulo_atual + "°", 1, PRETO)
    WIN.blit(entrada_texto2, POS_ENTRADA2)

    pygame.display.update()


def mover_aeropendulo(angulo, imagem_indice):
    if imagem_indice == 0:
        imagem_rotacionada = pygame.transform.rotate(AEROPENDULO_IMAGE_0, angulo)  
        vetor_rotacionado = VETOR.rotate(-angulo)  
        retangulo = imagem_rotacionada.get_rect(center=INICIO_IMG+vetor_rotacionado)
    elif imagem_indice == 1:
        imagem_rotacionada = pygame.transform.rotate(AEROPENDULO_IMAGE_1, angulo)  
        vetor_rotacionado = VETOR.rotate(-angulo)  
        retangulo = imagem_rotacionada.get_rect(center=INICIO_IMG+vetor_rotacionado)
    elif imagem_indice == 2:
        imagem_rotacionada = pygame.transform.rotate(AEROPENDULO_IMAGE_2, angulo)  
        vetor_rotacionado = VETOR.rotate(-angulo)  
        retangulo = imagem_rotacionada.get_rect(center=INICIO_IMG+vetor_rotacionado)
    elif imagem_indice == 3:
        imagem_rotacionada = pygame.transform.rotate(AEROPENDULO_IMAGE_3, angulo)  
        vetor_rotacionado = VETOR.rotate(-angulo)  
        retangulo = imagem_rotacionada.get_rect(center=INICIO_IMG+vetor_rotacionado)
    else:
        imagem_rotacionada = pygame.transform.rotate(AEROPENDULO_IMAGE_4, angulo)  
        vetor_rotacionado = VETOR.rotate(-angulo)  
        retangulo = imagem_rotacionada.get_rect(center=INICIO_IMG+vetor_rotacionado)
    
    return imagem_rotacionada, retangulo

def main():
    clock = pygame.time.Clock()  # controla a velocidade do while loop
    run = True

    ta = 1/FPS # tempo de amostragem
    vetor_tempo = np.arange(0,TEMPO_SIM,ta) # vetor tempo
    tamanho_vetor = len(vetor_tempo) #tamanho vetor tempo
    output = 0*np.ones([tamanho_vetor],dtype='float64') #alocação vetor output
    k = 0
    angulo_input_str = '0'
    contador = 0
    angulo_inicial = 0

    while run:
        clock.tick(FPS)

        for event in pygame.event.get(): #pega todos os eventos
            pos_mouse = pygame.mouse.get_pos()

            if event.type == pygame.QUIT: #se algum dos eventos for de saída
                run = False #saí do while com run falso
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                #46 - ponto no unicode
                if (ord(event.unicode)>=48 and ord(event.unicode)<= 57) or ord(event.unicode)==46: 
                    if angulo_input_str == '0':
                        angulo_input_str = event.unicode
                    else:
                        angulo_input_str += event.unicode

                if ord(event.unicode) == 8: #8 - backspace no unicode (para corrigir valor desejado)
                    angulo_input_str = angulo_input_str[:-1] 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BotaoComecar.cursor_over_button(pos_mouse):
                    if angulo_input_str == '':
                        angulo_input_str = '0'
            
                    angulo_input = float(angulo_input_str)
                    output = sistema_controlado.controle(angulo_input, angulo_inicial, TEMPO_SIM, FPS)
                    k=0
                
                if BotaoZerar.cursor_over_button(pos_mouse):
                    output = sistema_controlado.controle(0, angulo_inicial, TEMPO_SIM, FPS)
                    k=0
        
        if contador == 5: #reinicia contador que altera os frames
            contador = 0

        try: # try/except - devido ao valor de k
            imagem_aeropendulo, retangulo_aeropendulo = mover_aeropendulo(output[k], contador)
            angulo_inicial = output[k]
            angulo_atual = round(output[k],3)
        except:
            pass
        
        #incrementa indice do output e o contador
        k += 1
        contador = contador + 1

        #Atualiza a janela/ desenha novo frame
        draw_window(imagem_aeropendulo, retangulo_aeropendulo, angulo_input_str, str(angulo_atual))


if __name__ == "__main__":
    main()
