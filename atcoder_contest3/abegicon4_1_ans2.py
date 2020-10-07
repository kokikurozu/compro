K = int(input())
cnt = 0
i = 0

def lun_num(ax):
    if ax != 0:
        ax1 = ax - 1
        cnt += 1
    else:
        return
    ax2 = ax
    cnt += 1
    if ax != 9:
        ax3 = ax + 1
        cnt += 1
    else:
        return
    lun_num(ax1)
    
