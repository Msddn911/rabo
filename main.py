from microbit import *
import radio
import robotbit   # Biblioteca kiteeebott

# ====================== CONFIGURAÇÃO INICIAL PEGA NO MEU PAL ======================
comando = 0
radio.config(group=1)
radio.on()

# Inicialização sonora olha o zap de teste kkkkk
music.pitch(165, 1000)
sleep(50)
music.pitch(165, 1000)

display.show(Image.SQUARE_SMALL)

# ====================== FUNÇÃO DE CONTROLE DOS MOTORES (AQUI TALVEZ DE ERRO) ======================
def motor_run(m1_speed: int, m2_speed: int):
    """Controla os dois motores (compatível com M1A e M2A do original)"""
    robotbit.RobotBit().motor(1, m1_speed)   # M1A
    robotbit.RobotBit().motor(2, m2_speed)   # M2A

def stop_motors():
    """Para ambos os motores"""
    robotbit.RobotBit().motor(1, 0)
    robotbit.RobotBit().motor(2, 0)

# ====================== LOOP PRINCIPAL (TA FUNCIONANDO É O QUE IMPORTA MIGUEL DO FUTURO NAO MEXE NESSA MERDA OU VAI DAR ERRO NOVAMENTE) ======================
while True:
    # 1. Recebe comando remoto via rádio (envie como string: "1", "2", "3", "4" ou "0")  (AQUI TA LEGAL O CODIGO FUNCIONAL MAS PODE DA ERRO OU ATRASO DE COMANDO NAO SEI O PQ TAMBEM)
    msg = radio.receive()
    if msg is not None:
        try:
            comando = int(msg)
        except ValueError:
            pass

    # 2. Controle local (prioridade máxima)  (NAO MEXER SEU PUTO CURIOSO)
    if button_a.is_pressed() and button_b.is_pressed():
        stop_motors()
        display.clear()
        display.show(Image.SQUARE_SMALL)

    elif pin_logo.is_touched():
        motor_run(150, 150)
        display.show(Image.ARROW_N)

    elif accelerometer.current_gesture() == "logo up":
        motor_run(-150, -150)
        display.show(Image.ARROW_S)

    elif button_a.is_pressed():
        motor_run(150, 0)
        display.show(Image.ARROW_W)

    elif button_b.is_pressed():
        motor_run(0, 150)
        display.show(Image.ARROW_E)

    # 3. Controle remoto (só executa se não houver comando local ativo)  (AQUI EU JA ESTAVA ETEDIADO ENTAO DEVO DIZER QUE BEM PROVAVEL DE PRECISAR DE AJUSTE NA LINHA 25)
    elif comando == 1:
        motor_run(150, 150)
        display.show(Image.ARROW_N)
    elif comando == 2:
        motor_run(-150, -150)
        display.show(Image.ARROW_S)
    elif comando == 3:
        motor_run(150, 0)
        display.show(Image.ARROW_W)
    elif comando == 4:
        motor_run(0, 150)
        display.show(Image.ARROW_E)
    else:
        stop_motors()
        display.show(Image.SQUARE_SMALL)

    sleep(20)  # Evita sobrecarga da CPU (eu acho que vai dar bom)
