import numpy as np


def drop(stack, skip=None):
    peaks = np.zeros((12,12))
    falls = 0

    for i, (u,v,w, x,y,z) in enumerate(stack):
        if i == skip: continue

        peak = peaks[u:x, v:y].max()
        peaks[u:x, v:y] = peak + z-w

        stack[i] = u,v,peak, x,y,peak + z-w
        falls += peak < w

    return not falls, falls


stack = np.fromregex('input_22.txt', r'\d+', [('',int)]
            ).reshape(-1, 6).astype(int)
stack = stack[stack[:, 2].argsort()] + [0,0,0,1,1,1]

drop(stack)

print(*np.sum([drop(stack.copy(), skip=i)
    for i in range(len(stack))], axis=0))