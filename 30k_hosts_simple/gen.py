#!/usr/bin/env python

x = 0
y = 0
z = 0
for i in xrange(0, 35000):
    z += 1
    if z > 255:
        z = 0
        y += 1
    if y > 255:
        x += 1
    if x > 255:
        print("Fuck x is too high {}".format(x))
        raise RuntimeError()
    host = "127.{}.{}.{}".format(x, y, z)
    print("localhost-{} ansible_host={} ansible_user=meyers".format(i, host))

