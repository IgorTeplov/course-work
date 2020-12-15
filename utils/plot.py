from matplotlib import pyplot as plt
import numpy as np
import time

def timer(func):
    
    def wrap(x, y, *args, show=False, save=True, name='img', **kvargs):
        t_s = time.time()

        print(f"PLOT NAME: {name}, {args}, {kvargs}")
        print(f"START: {t_s}")
        v = func(x, y, *args, show=show, save=save, name=name, **kvargs)
        t_e = time.time()
        print(f"END: {t_e}")
        print(f"DELTA: {t_e-t_s}")
        return v
    return wrap

# fig, ax = plt.subplots()
# ax.plot(x, y, linewidth = 1,color = 'crimson')
# plt.yticks(np.arange(0,75,1))
# ax.set_ylim(0, 5)
# plt.ticklabel_format(style='plain', axis='y', useOffset=False)

@timer
def plot(x, y, *args, show=False, save=True, name='img', steeps={}, **kvargs):
    fig, ax = plt.subplots()
    if steeps != {}:
        if 'x' in steeps.keys():
            plt.xticks(np.arange(steeps['x']['from'],
                steeps['x']['to'],steeps['x']['steep']))
        if 'y' in steeps.keys():
            plt.yticks(np.arange(steeps['y']['from'],
                steeps['y']['to'],steeps['y']['steep']))
    if 'color' in kvargs.keys():
        kvargs['color'] == '#000000'
    ax.plot(x,y, *args, **kvargs)
    if show:
        plt.show()
    if save:
        fig.savefig(f'img/{name}.png')
    plt.close(fig)

def plots(pl):
    for p in pl:
        fig, ax = plt.subplots()
        ax.plot(p[0],p[1], linewidth = 1, color = 'crimson')
    plt.show()