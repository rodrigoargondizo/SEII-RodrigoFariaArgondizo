import numpy as np
import matplotlib.pyplot as plt

def f(t, x, u):
    #State vector
    x1 = x[0]
    x2 = x[1]

    l1 =.75
    l2 = 1.2
    J = 1e-2
    p = .85*9.81
    ua = .1

    x_dot = np.array( [ x2, (-p*l1/J)*np.sin(x1) + (-ua/J)*x2 + (l2/J)*u ],dtype='float64')

    return x_dot


# Runge Kutta de 4ª ordem, responsável pela simulação do sistema
def rk4(tk, h, xk, uk):

    k1 = f(tk , xk , uk)
    k2 = f(tk + h/2.0, xk + h*k1/2.0, uk)
    k3 = f(tk + h/2.0, xk + h*k2/2.0, uk)
    k4 = f(tk + h , xk + h*k3 , uk)
    xkp1 = xk + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)

    return xkp1 

def controle(angulo_input, angulo_inicial, tempo_sim, fps):
    # PARÂMETROS DE SIMULAÇÃO
    ta = 1/fps # tempo de amostragem
    t_total = np.arange(0,tempo_sim,ta) # vetor tempo
    tam = len(t_total) #tamanho vetor tempo


    # Vetor de estados [x1 x2]^T = [theta omega]^T
    x = np.zeros([2, tam],dtype='float64')

    #Inicialização da condição inicial
    x[:,0] = np.array([angulo_inicial*np.pi/180.,0])

    # Determinar um valor para a força de controle de equilíbrio
    l1 =.75
    l2 = 1.2
    J = 1e-2
    p = .85*9.81
    ua = .1
    u_eq = np.sin(angulo_inicial*np.pi/180)*p*l1/l2

    # Vetor de entrada
    u = u_eq*np.ones([tam],dtype='float64')

    #Vetores de erro da ação de controle
    erro = np.ones([tam],dtype='float64')
    erro_int = np.ones([tam],dtype='float64')

    #Parâmetros de controle
    Kp=0.3
    Ki=1.5
    Kv=0

    #Limites de saturação
    limite_superior= 15 #estabelecidos de maneira empírica
    limite_inferior= -15

    # Execução da simulação
    for k in range(tam-1):
        
        #PI+V- Ação de controle com aproximação Forward Euler e realimentação de velocidade
        erro[k] =  (angulo_input*np.pi/180) - x[0,k] #erro angulo, U_eq=inputangulo
        erro_int[k]= erro_int[k-1] + erro[k]*ta # erro da parte integral da ação de controle

        u[k] = Kp*erro[k] + Ki*erro_int[k] - Kv*x[1,k] #controle PIV utilizando o estado x2=teta_ponto=omega
        
        # Saturação
        u[k] = min(u[k], limite_superior)  # superior
        u[k] = max(u[k], limite_inferior)  # inferior

    
        # Atualização do estado
        x[:,k+1] = rk4(t_total[k], ta, x[:,k], u[k])

    # plt.subplot(2, 1, 1)
    # plt.plot(t_total,x[0,:]*180/np.pi)
    # plt.ylabel('$x_1$ - i ')
    # plt.subplot(2, 1, 2)
    # plt.plot(t_total,x[1,:]*180/np.pi)
    # plt.ylabel('$x_2$ - q')
    # plt.xlabel('t [s]')
    # plt.show()

    return (x[0,:]*180/np.pi) #função retorna o estado x1=theta da simulação com o controle


