import numpy as np
import matplotlib.pyplot as plt
import control


def plot_root_locus(K, poles, zeros):
    # 构造开环传递函数
    num_zeros = len(zeros)
    num_poles = len(poles)

    if num_zeros > 0:
        num = np.poly(zeros)
    else:
        num = np.array([1.0])

    den = np.poly(poles)

    if num_poles > num_zeros:
        num_expanded = np.pad(num, (num_poles - num_zeros, 0), mode='constant')
    else:
        num_expanded = num

    sys = control.TransferFunction(num_expanded, den)

    # 计算根轨迹
    rlist, klist = control.root_locus(sys, kvect=K, plot=False)

    # 绘制根轨迹图
    plt.figure()
    plt.plot(rlist.real, rlist.imag, 'b-', linewidth=1)
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.title("Root Locus")
    plt.axvline(x=0, color='k', linewidth=1)
    plt.grid(True, which='both', linestyle='--', alpha=0.5)

    # 标记开环零点和极点
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='red', label='Zeros', s=50)
    plt.scatter(np.real(poles), np.imag(poles), marker='x', color='blue', label='Poles', s=50)

    plt.legend()
    plt.show()


# 示例
if __name__ == '__main__':
    K = np.linspace(0, 10, 1000)
    poles = np.array([-1, -2, -3])
    zeros = np.array([-0.5, -1.5])
    plot_root_locus(K, poles, zeros)

