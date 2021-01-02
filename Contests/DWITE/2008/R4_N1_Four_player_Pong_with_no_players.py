for i in range(5):
    h_vel = int(input())
    v_vel = int(input())
    pos = [50, 25]
    while 0 < pos[0] < 100 and 0 < pos[1] < 50:
        pos = [pos[0] + h_vel, pos[1] + v_vel]
    print(",".join([str(p) for p in pos]))
