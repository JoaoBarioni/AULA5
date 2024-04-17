import math

def calculate_wheels_velocity(v, L, R, w):
    wl = (1.0 / R) * (v - ((w * L) / 2))
    wr = (1.0 / R) * (v + ((w * L) / 2))
    return wl, wr

def calculate_real_velocity(R, L, wr, wl):
    v = (R / 2) * (wr + wl)
    w = (R / L) * (wr - wl)
    return v, w

def calculate_global_convert(O, v, w):
    E1 = [
        [math.cos(math.radians(O)), -math.sin(math.radians(O)), 0],
        [math.sin(math.radians(O)), math.cos(math.radians(O)), 0],
        [0, 1, 0]
    ]

    vector = [v, 0, w]

    result = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            result[i] += E1[i][j] * vector[j]

    return result


def calculate_next_position(x, y, O, result, delta_t):
    new_x = x + result[0] * delta_t
    new_y = y + result[1] * delta_t
    new_O = O + result[2] * delta_t

    print("------------------------------")
    print("Initial Position:")
    print(f"x: {x}, y: {y}, Orientation: {O} degrees")

    print("\nWheels Velocity:")
    print(f"Left wheel: {result[0]}, Right wheel: {result[1]}")

    print("\nReal Velocity:")
    print(f"Linear velocity (v): {result[0]}, Angular velocity (w): {result[1]}")

    print("\nResultant vector after global conversion:")
    print(f"Resultant vector: {result}")

    print("\nNew Position:")
    print(f"x: {new_x}, y: {new_y}, Orientation: {new_O} degrees")
    print("------------------------------")



def main():
    # Posição inicial do robô
    x, y, O = 1, 1, 22

    # Configuração das rodas
    L, R = 1.0, 2.0

    # Velocidade linear (v) e angular (w)
    v, w = 30.0, 20.0

    # Função para calcular velocidade das rodas
    wl, wr = calculate_wheels_velocity(v, L, R, w)

    # Função para calcular a velocidade real
    v, w = calculate_real_velocity(R, L, wr, wl)

    # Função para calcular a coordenada global
    result = calculate_global_convert(O, v, w)

    # Valor do delta
    delta_t = 0.1

    # Função para calcular a próxima posição
    calculate_next_position(x, y, O, result, delta_t)

if __name__ == "__main__":
    main()
