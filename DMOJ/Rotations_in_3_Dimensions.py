import math

t = int(input())
test_cases = [[float(num) for num in input().split(" ")] for i in range(t)]
for case in test_cases:
    x, y, z, r_x, r_y, r_z, theta = case

    r_mag = math.sqrt((r_x ** 2) + (r_y ** 2) + (r_z ** 2))
    r_x_nom = r_x / r_mag
    r_y_nom = r_y / r_mag
    r_z_nom = r_z / r_mag
    theta_c = math.cos(theta)
    theta_s = math.sin(theta)

    x_prime = (theta_c + (r_x_nom ** 2) * (1 - theta_c)) * x + \
              (r_x_nom * r_y_nom * (1 - theta_c) - r_z_nom * theta_s) * y + \
              (r_x_nom * r_z_nom * (1 - theta_c) + r_y_nom * theta_s) * z

    y_prime = (r_x_nom * r_y_nom * (1 - theta_c) + r_z_nom * theta_s) * x + \
              (theta_c + (r_y_nom ** 2) * (1 - theta_c)) * y + \
              (r_y_nom * r_z_nom * (1 - theta_c) - r_x_nom * theta_s) * z

    z_prime = (r_x_nom * r_z_nom * (1 - theta_c) - r_y_nom * theta_s) * x + \
              (r_y_nom * r_z_nom * (1 - theta_c) + r_x_nom * theta_s) * y + \
              (theta_c + (r_z_nom ** 2) * (1 - theta_c)) * z

    print('{:.6f}'.format(round(x_prime, 6)), '{:.6f}'.format(round(y_prime, 6)), '{:.6f}'.format(round(z_prime, 6)))
