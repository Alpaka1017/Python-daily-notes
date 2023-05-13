import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D


def get_color_projection_mpl():
    cmaps = plt.colormaps()
    # cmaps = mpl.cm.cmap_d.keys()  # 也可用 cmamps = plt.colormaps()
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    fig = plt.figure(figsize=(42, 82),
                     facecolor='lightyellow',
                     dpi=256
                     )
    axes = fig.subplots(len(cmaps) // 2, 2)  # 增加绘图子区

    #
    for cmap, ax in zip(sorted(cmaps), axes.ravel()):
        # 绘制图形
        ax.imshow(gradient,
                  aspect='auto',
                  cmap=plt.get_cmap(cmap)
                  )

        # 在每个图形中添加文本
        ax.text(x=260, y=1,  # 文本所在坐标位置
                s=cmap,  # 文本内容
                fontsize=28,  # 文本字体大小
                color='k',  # 文本颜色
                weight='bold',  # 字体粗细风格
                )

        # 不显示坐标轴
        ax.set_axis_off()

    # 设置子区布局
    fig.subplots_adjust(left=0.1, right=0.8,
                        top=1, bottom=0,
                        hspace=0.5, wspace=0.4)
    plt.show()
    # plt.savefig('color_bar.png', dpi=64)


def scatter_example():
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.scatter(X, Y, s=75, c=T, cmap='gist_heat', alpha=.5)

    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    # savefig('../figures/scatter_ex.png',dpi=48)
    plt.colorbar()
    plt.show()


def Example_histogram():
    n = 12
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    print(X)
    print(Y1)
    print(Y2)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.bar(X, +Y1, width=.85, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, width=.85, facecolor='#ff9999', edgecolor='white')

    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')

    for x, y in zip(X, Y2):
        plt.text(x, -y - 0.05, '%.2f' % y, ha='center', va='top')

    plt.xlim(-.5, n), plt.xticks([])
    plt.ylim(-1.25, +1.25), plt.yticks([])

    # savefig('../figures/bar_ex.png', dpi=48)
    plt.show()


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


def contour_ex():
    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)

    plt.axes([0.025, 0.025, 0.95, 0.95])

    plt.contourf(X, Y, f(X, Y), 16, alpha=.75, cmap=plt.cm.hot)
    C = plt.contour(X, Y, f(X, Y), 16, colors='black', linewidth=.5)
    plt.clabel(C, inline=0, fontsize=10)

    plt.xticks([]), plt.yticks([])
    # savefig('../figures/contour_ex.png',dpi=48)
    plt.show()


def imshow_ex():
    n = 10
    x = np.linspace(-3, 3, int(4.5 * n))
    y = np.linspace(-3, 3, int(4.0 * n))
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.imshow(Z, cmap='bone', origin='lower')
    plt.colorbar(shrink=.92)

    plt.xticks([]), plt.yticks([])
    # savefig('../figures/imshow_ex.png', dpi=48)
    plt.show()


def pie_ex():
    n = 12
    Z = np.ones(n)
    Z[-1] *= 2

    plt.axes([0.025, 0.025, 0.95, 0.95])

    plt.pie(Z, explode=Z * .05, colors=['%f' % (i / float(n)) for i in range(n)],
            wedgeprops={"linewidth": 1, "edgecolor": "black"})
    plt.gca().set_aspect('equal')
    plt.xticks([]), plt.yticks([])

    # savefig('../figures/pie_ex.png',dpi=48)
    plt.show()


def quiver_plot_ex():
    n = 8
    X, Y = np.mgrid[0:n, 0:n]
    T = np.arctan2(Y - n / 2.0, X - n / 2.0)
    R = 10 + np.sqrt((Y - n / 2.0) ** 2 + (X - n / 2.0) ** 2)
    U, V = R * np.cos(T), R * np.sin(T)

    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.quiver(X, Y, U, V, R, alpha=.5)
    plt.quiver(X, Y, U, V, edgecolor='k', facecolor='None', linewidth=.5)

    plt.xlim(-1, n), plt.xticks([])
    plt.ylim(-1, n), plt.yticks([])

    # savefig('../figures/quiver_ex.png',dpi=48)
    plt.show()


def grid_ex():
    ax = plt.axes([0.025, 0.025, 0.95, 0.95])

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 3)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
    ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # savefig('../figures/grid_ex.png',dpi=48)
    plt.show()


def manuscript_ex():
    eqs = []
    eqs.append((
        r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$"))
    eqs.append(
        (r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
    eqs.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$"))
    eqs.append((r"$E = mc^2 = \sqrt{{m_0}^2c^4 + p^2c^2}$"))
    eqs.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))

    plt.axes([0.025, 0.025, 0.95, 0.95])

    for i in range(24):
        index = np.random.randint(0, len(eqs))
        eq = eqs[index]
        size = np.random.uniform(12, 32)
        x, y = np.random.uniform(0, 1, 2)
        alpha = np.random.uniform(0.25, .75)
        plt.text(x, y, eq, ha='center', va='center', color="#11557c", alpha=alpha,
                 transform=plt.gca().transAxes, fontsize=size, clip_on=True)

    plt.xticks([]), plt.yticks([])
    # savefig('../figures/text_ex.png',dpi=48)
    plt.show()


if __name__ == '__main__':
    # get_color_projection_mpl()
    # scatter_example()
    # Example_histogram()
    # contour_ex()
    # imshow_ex()
    # pie_ex()
    # quiver_plot_ex()
    # grid_ex()
    # manuscript_ex()
    # 生成数据
    x = 10
    y = -5
    # # Which of the two variables above has the smallest absolute value?
    smallest_abs = min(abs(x), abs(y))
    # result = (x, y)[abs(y) < abs(x)]
    result = (lambda a, b: a if abs(a) < abs(b) else b)(y, x)
    print(f'The smallest absolute value of {x} and {y} is {result}, which is {smallest_abs}')


print(range(2*3))
