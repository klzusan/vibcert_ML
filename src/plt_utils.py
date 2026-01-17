import matplotlib.pyplot as plt
import os
import utils as ut

# type: 'raw' or 'proc' or 'ori'
def visual_data(csv, type, person, n1, n2):
        contain_subset = 0 # flag
        pngdir = os.path.join(ut.get_staticPath(f'img_{type}'), person)
        if not os.path.exists(pngdir):
            os.mkdir(pngdir)

        path = os.path.join(pngdir, f"{n1}_{n2}.png")

        fig = plt.figure(figsize=(15, 8))
        ax_left = fig.add_subplot(1, 2, 1)
        ax_right = fig.add_subplot(1, 2, 2)

        if set(['ax', 'ay', 'az']).issubset(csv.columns):  
            contain_subset = 1
            csv[['ax', 'ay', 'az']].plot(ax=ax_left)
            ax_left.set_title("Acceleration")
            ax_left.grid(True)

        if set(['gx', 'gy', 'gz']).issubset(csv.columns):
            contain_subset = 1
            csv[['gx', 'gy', 'gz']].plot(ax=ax_right)
            ax_right.set_title("Gyro")
            ax_right.grid(True)

        if contain_subset == 1:
            fig.suptitle(f"{person}_{type} {n1}_{n2}")
            fig.tight_layout()
            plt.savefig(path)
            plt.close(fig)
        else:
             print("Nothing to plot")

def visual_seg(segments, person, n1, n2):
    pngdir = os.path.join(ut.get_staticPath(f'img_proc'), person)
    if not os.path.exists(pngdir):
        os.mkdir(pngdir)

    path = os.path.join(pngdir, f"{n1}_{n2}.png")

    fig = plt.figure(figsize=(15, 8))
    ax_left = fig.add_subplot(1, 2, 1)
    ax_right = fig.add_subplot(1, 2, 2)
    for s in segments:
        ax_left.plot(s[:, 0:3])
        ax_right.plot(s[:, 3:6])

    ax_left.set_title('Acceleration')
    ax_left.legend(['ax', 'ay', 'az'])
    ax_left.grid(True)
    ax_right.set_title('Gyro')
    ax_right.legend(['gx', 'gy', 'gz'])
    ax_right.grid(True)

    fig.suptitle(f"{person}_seg {n1}_{n2}")
    fig.tight_layout()
    plt.savefig(path)
    plt.close()