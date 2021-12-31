def find_target_area_start_vels(left, right, bottom, top):
    # above a certain positive maximum y velocity, the probe will go up and come back down, hitting the water (y = 0)
    # with such a high velocity that after one step, the probe's y position will already be below the target bottom and
    # so any y velocities above this maximum can be skipped, since the probe will never reach the target area
    # since the x and y positions of the probe are independent, this maximum is the same for all x velocities
    # this maximum is found by iterating through y velocities, and simulating the probe's positions for each one
    # if the probe is below the water (y < 0) and above the target bottom at any step, that y velocity is below the max,
    # and so the max y velocity is one less than the first y velocity where this is not true
    max_y_vel = 0
    for start_y_vel in range(10 ** 10):
        cur_y_pos = 0
        cur_y_vel = start_y_vel
        y_above_target_bottom = False
        while bottom <= cur_y_pos:
            if bottom <= cur_y_pos < 0:
                y_above_target_bottom = True
                break
            cur_y_pos += cur_y_vel
            cur_y_vel -= 1
        if not y_above_target_bottom:
            max_y_vel = start_y_vel - 1
            break

    target_area_start_vels = []
    for start_x_vel in range(right + 1):
        # we know the x velocity is never negative, and it decreases at each step, so once the probe's x position
        # reaches its maximum, the x velocity will be 0, and it will stay 0, so the x position will be constant
        # we can calculate the maximum x position using simple math, since if the x velocity starts at n, it will
        # decrease by 1 until it reaches 0, and this means max_x = n + (n - 1) + (n - 2) .... + 3 + 2 + 1 + 0
        # the well known formula for this sum is max_x = n * (n + 1) / 2 and if max_x is less than the target area left,
        # we know the probe will never reach the target area, so we can skip checking this x velocity
        if start_x_vel * (start_x_vel + 1) // 2 < left:
            continue
        for start_y_vel in range(bottom, max_y_vel + 1):
            cur_pos = (0, 0)
            cur_vel = (start_x_vel, start_y_vel)
            max_y = -10 ** 10
            reaches_target = False
            # if the probe's position is below the target area bottom or right of the target area right, we can stop
            # simulating since the probe will never go left (x velocity is never negative) and while it is possible for
            # the probe to go up, the target area is below the water (y < 0) and once the probe is below the water, the
            # y velocity will never be positive (positive y velocity means the probe goes up above the water, reaches
            # a maximum y where the velocity is zero, and comes back down to hit the water with a negative y velocity)
            while cur_pos[0] <= right and bottom <= cur_pos[1]:
                if left <= cur_pos[0] <= right and bottom <= cur_pos[1] <= top:
                    reaches_target = True
                    break

                cur_pos = (cur_pos[0] + cur_vel[0], cur_pos[1] + cur_vel[1])
                # the x velocity cannot go below 0, and max(a, 0) = a if a >= 0 and = 0 otherwise, so this is ensured
                cur_vel = (max(cur_vel[0] - 1, 0), cur_vel[1] - 1)

                max_y = max(max_y, cur_pos[1])
            if reaches_target:
                target_area_start_vels.append((start_x_vel, start_y_vel, max_y))
    return target_area_start_vels


with open("InputFiles/Day_17.txt") as f:
    target_x, target_y = f.readline().rstrip().split(': ')[1].split(', ')
    target_x_left, target_x_right = map(int, target_x.split('=')[1].split('..'))
    target_y_bottom, target_y_top = map(int, target_y.split('=')[1].split('..'))

start_vels = find_target_area_start_vels(target_x_left, target_x_right, target_y_bottom, target_y_top)

part_1_ans = -10 ** 10
for _, _, target_area_max_y in start_vels:
    part_1_ans = max(part_1_ans, target_area_max_y)
print(part_1_ans)

part_2_ans = len(start_vels)
print(part_2_ans)
