from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

janela = Window(612, 344)
janela.set_title('Isis Meira - Pong') 
background = GameImage('gramado_tenis.jpg')
teclado = janela.get_keyboard()

bolinha = Sprite('bolinha.png', 1)        
pad_jogador = Sprite('raquete_jogador.png', 1)          
pad_ia = Sprite('raquete_ia.png', 1)             

pad_jogador.set_position(janela.width - pad_jogador.width - 5, janela.height/2 - pad_jogador.height/2)  
pad_ia.set_position(5, janela.height/2 - pad_ia.height/2)            
bolinha.set_position(janela.width/2 - bolinha.width/2, janela.height/2 - bolinha.height/2)

score_jogador = 0    
score_ia = 0          
vel_x = 0            
vel_y = 0           
vel_pad = 400        
hit_contador = 0     
esperando_saque = True  

while True:
    # Controle da raquete do jogador
    if teclado.key_pressed("up") and pad_jogador.y > 0:
        pad_jogador.y -= vel_pad * janela.delta_time()
    if teclado.key_pressed("down") and pad_jogador.y + pad_jogador.height < janela.height:
        pad_jogador.y += vel_pad * janela.delta_time()

    # IA 
    if pad_ia.y + pad_ia.height/2 > bolinha.y:
        pad_ia.y -= vel_pad/1.5 * janela.delta_time()
    else:
        pad_ia.y += vel_pad/1.5 * janela.delta_time()

    # Lógica do saque 
    if esperando_saque:
        if teclado.key_pressed("SPACE"):
            vel_x = -250 
            vel_y = 250
            esperando_saque = False
    else:
        bolinha.move_x(vel_x * janela.delta_time())
        bolinha.move_y(vel_y * janela.delta_time())

    # Colisões
    if bolinha.y <= 0 or bolinha.y + bolinha.height >= janela.height:
        vel_y *= -1
        bolinha.y += 5 if bolinha.y <= 0 else -5

    if bolinha.collided(pad_jogador):
        vel_x = -abs(vel_x) * 1.1  
        bolinha.x -= 5
        hit_contador += 1
        
    if bolinha.collided(pad_ia):
        vel_x = abs(vel_x) * 1.1  
        bolinha.x += 5
        hit_contador += 1

    # Sistema de pontuação
    if bolinha.x < 0:  
        score_jogador += 1
        esperando_saque = True
        bolinha.set_position(janela.width/2 - bolinha.width/2, janela.height/2 - bolinha.height/2)
        vel_x, vel_y = 0, 0
        
    if bolinha.x + bolinha.width > janela.width:
        score_ia += 1
        esperando_saque = True
        bolinha.set_position(janela.width/2 - bolinha.width/2, janela.height/2 - bolinha.height/2)
        vel_x, vel_y = 0, 0

    background.draw()
    janela.draw_text(f"{score_ia} x {score_jogador}", janela.width/2.25, 20, 30, (0,0,0), bold=True)
    bolinha.draw()
    pad_jogador.draw()
    pad_ia.draw()
    janela.update()