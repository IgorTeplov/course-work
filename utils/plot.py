from matplotlib import pyplot as plt
import time

def timer(func):
    
    def wrap(x, y, *args, show=False, save=True, name='img', **kvargs):
        t_s = time.time()
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
def plot(x, y, *args, show=False, save=True, name='img', **kvargs):
    fig, ax = plt.subplots()
    ax.plot(x,y, *args, **kvargs)
    if show:
        fig.show()
    if save:
        fig.savefig(f'img/{name}.png')
    plt.close(fig)