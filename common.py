import random
import sys
import itertools
import math
from taco import *

NDIM = 2

class MyParticle(Particle):
    def __init__(self, pos, m=0.0, f=None):
        super(MyParticle, self).__init__(pos)
        self.m = m
        self.f = f
        if f is None:
            self.f = Vector([0.0] * len(pos))
        assert len(pos) == len(self.f)

    def __str__(self):
        return "particle{ pos: " + ", ".join(str(i) for i in self.pos) \
            + ", force: " + ", ".join(str(i) for i in self.f) + "}"
    pass
    
def gen_particle_list(np):
    particles = []
    random.seed(0)
    for i in range(np):
        pos = [random.random() for i in range(NDIM)]
        m = 1.0 / np
        p = MyParticle(pos, m)
        particles.append(p)
    return particles

def direct(p1, p2, reaction=False):
    for i, p in enumerate(p1):
        if reaction:
            j = i + 1
        else:
            j = 0
        for q in p2[j:]:
            if p is q: continue
            R2 = distance_r2(p, q)
            invR2 = 1.0 / R2
            invR = q.m * math.sqrt(invR2)
            invR3 = invR2 * invR
            for i in range(NDIM):
                f = - (p.pos[i] - q.pos[i]) * invR3
                p.f[i] -= f
                q.f[i] += f
    return

def reference_compute(np):
    particles = gen_particle_list(np)
    direct(particles, particles, True)
    return particles

def diff(p1, p2):
    total_diff = 0.0
    for i, j in itertools.izip(p1, p2):
        total_diff += reduce(lambda x, y: x + y,
                             ((f - g) ** 2 for f, g in itertools.izip(i.f, j.f)))
    total_diff /= len(p1)
    return total_diff
    
def run_test(test_method, descriptor_str):
    np = 100 # default number of particles
    # the first argument, if given, overrides the default value of np
    if len(sys.argv) > 1:
        np = int(sys.argv[1])

    reference_result = reference_compute(np)
    taco_result = test_method(np)

    print "Reference (Direct)"
    for p in reference_result: print p

    print descriptor_str
    for p in taco_result: print p

    # compare results    
    print "Diff: " + str(diff(reference_result, taco_result))
        
    return
