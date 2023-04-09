import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def plot_root_locus_scipy(K, poles, zeros):
    # 构造开环传递函数
    num_zeros = len(zeros)
    num_poles = len(poles)

    if num_zeros > 0:
        num = np.poly(zeros)
    else:
        num = np.array([1.0])

    den = np.poly(poles)

    # 使用 np.pad 填充 num 以使其与 den 具有相同的长度
    if num_poles > num_zeros:
        num_expanded = np.pad(num, (num_poles - num_zeros, 0), mode='constant')
    else:
        num_expanded = num

    sys = signal.TransferFunction(num_expanded, den)
    rlist, klist = signal.root_locus(sys, kvect=K, xlim=None, ylim=None)
    # 绘制根轨迹
    plt.figure()
    plt.plot(rlist.real, rlist.imag, 'b-', linewidth=1)
    plt.title('Root Locus')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.axvline(x=0, color='k', linewidth=1)
    plt.grid(True, which='both', linestyle='--', alpha=0.5)

    # 绘制极点和零点
    plt.scatter(poles.real, poles.imag, marker='x', color='red', label='Poles', s=50)
    plt.scatter(zeros.real, zeros.imag, marker='o', color='green', label='Zeros', s=50)

    plt.legend()
    plt.show()
    # 计算根轨迹
    # num_points = len(K)
    # real = np.zeros((num_poles, num_points))
    # imag = np.zeros((num_poles, num_points))
    #
    # # 扩展分子多项式以使其与分母多项式具有相同的长度
    # num_expanded = np.concatenate((np.zeros(num_poles - num_zeros), num))
    #
    # for i, k in enumerate(K):
    #     char_eq = den + k * num_expanded
    #     roots = np.roots(char_eq)
    #     real[:, i] = np.real(roots)
    #     imag[:, i] = np.imag(roots)
    #
    # # 绘制根轨迹图
    # plt.figure()
    # for i in range(num_poles):
    #     plt.plot(real[i], imag[i], color='blue')  # 使用单一颜色
    # plt.xlabel("Re")
    # plt.ylabel("Im")
    # plt.title("Root Locus")
    # plt.grid()
    #
    # # 标记开环零点和极点
    # plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='red', label='Open-loop Zeros')
    # plt.scatter(np.real(poles), np.imag(poles), marker='x', color='blue', label='Open-loop Poles')
    #
    # # 添加箭头
    # arrow_spacing = 50  # 调整此值以改变箭头的密度
    # for i in range(num_poles):
    #     for j in range(0, num_points - 1, arrow_spacing):
    #         dx = real[i, j + 1] - real[i, j]
    #         dy = imag[i, j + 1] - imag[i, j]
    #         plt.arrow(real[i, j], imag[i, j], dx, dy, shape='full', lw=0, length_includes_head=True,
    #                   head_width=0.03, head_length=0.05, color='green', alpha=0.7)
    #
    # plt.legend()
    #
    # # 确保图形中心在坐标原点（0,0）
    # real_min, real_max = np.min(real), np.max(real)
    # imag_min, imag_max = np.min(imag), np.max(imag)
    # plt.xlim(real_min - (real_max - real_min) * 0.1, real_max + (real_max - real_min) * 0.1)
    # plt.ylim(imag_min - (imag_max - imag_min) * 0.1, imag_max + (imag_max - imag_min) * 0.1)
    #
    # plt.show()


if __name__ == '__main__':
    # 示例
    K = np.linspace(0, 20, 1000)
    poles = np.roots([0.5, 1, 1])
    zeros = np.roots([0.5, 1])

    plot_root_locus_scipy(K, poles, zeros)


