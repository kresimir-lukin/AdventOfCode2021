import sys, re

def find_hit_velocities(xfrom, xto, yfrom, yto):
    hit_velocities = []
    for x_initial_velocity in range(1, xto+1):
        for y_initial_velocity in range(yfrom, -yfrom+1):
            x = y = 0
            x_velocity, y_velocity = x_initial_velocity, y_initial_velocity
            hit = False
            while x <= xto and y >= yfrom and not hit:
                x += x_velocity
                y += y_velocity
                x_velocity = max(x_velocity-1, 0)
                y_velocity -= 1
                if xfrom <= x <= xto and yfrom <= y <= yto:
                    hit = True
                    hit_velocities.append((x_initial_velocity, y_initial_velocity))
    return hit_velocities

assert len(sys.argv) == 2
target_area = open(sys.argv[1]).read()
re_match = re.match('target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)..(-?\d+)', target_area)
xfrom, xto, yfrom, yto = map(int, re_match.groups())

hit_velocities = find_hit_velocities(xfrom, xto, yfrom, yto)
maxy = max(y for _, y in hit_velocities)
part1 = maxy * (maxy + 1) // 2
part2 = len(hit_velocities)

print(f'Part 1: {part1}, Part 2: {part2}')