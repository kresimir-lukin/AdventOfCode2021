import sys, re

def intersect(cuboid1, cuboid2):
    xfrom, xto = max(cuboid1[1], cuboid2[1]), min(cuboid1[2], cuboid2[2])
    yfrom, yto = max(cuboid1[3], cuboid2[3]), min(cuboid1[4], cuboid2[4])
    zfrom, zto = max(cuboid1[5], cuboid2[5]), min(cuboid1[6], cuboid2[6])
    if xfrom > xto or yfrom > yto or zfrom > zto:
        return None
    return (-cuboid1[0] * cuboid2[0], xfrom, xto, yfrom, yto, zfrom, zto)

def count_cubes(reboot_steps):
    cuboids = []
    for step in reboot_steps:
        new_cuboids = [step] if step[0] == 1 else []
        for cuboid in cuboids:
            intersection = intersect((1,) + step[1:], cuboid)
            if intersection is not None:
                new_cuboids.append(intersection)
        cuboids.extend(new_cuboids)
    cubes = 0
    for sign, xfrom, xto, yfrom, yto, zfrom, zto in cuboids:
        cubes += sign * (xto - xfrom + 1) * (yto - yfrom + 1) * (zto - zfrom + 1)
    return cubes

assert len(sys.argv) == 2
reboot_input = open(sys.argv[1]).read().splitlines()
reboot_steps = []
for line in reboot_input:
    re_match = re.match('(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', line)
    action, xfrom, xto, yfrom, yto, zfrom, zto = re_match.groups()
    reboot_steps.append(tuple(map(int, [action == 'on', xfrom, xto, yfrom, yto, zfrom, zto])))

part1 = count_cubes([step for step in reboot_steps if all(-50 <= value <= 50 for value in step[1:])])
part2 = count_cubes(reboot_steps)

print(f'Part 1: {part1}, Part 2: {part2}')