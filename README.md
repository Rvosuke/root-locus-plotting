# root-locus-plotting
Use SymPy to draw the root locus diagram, which is convenient for learning the principle of automatic control.
# 根轨迹绘制工具

这个项目提供了一个用于绘制根轨迹图的Python工具。它可以帮助您快速分析开环传递函数的系统性能，特别是在控制系统设计中。

## 功能

- 输入开环传递函数的极点和零点
- 计算根轨迹
- 使用matplotlib绘制根轨迹图

## 安装

确保您已经安装了以下Python库：

- control
- matplotlib
- numpy
- PySide2

您可以使用以下命令安装这些库：

pip install control matplotlib numpy PySide2


## 使用方法

1. 克隆此仓库到本地，或者下载ZIP文件并解压。

2. 在终端中，导航到项目目录，然后运行以下命令启动图形界面：

python main_window.py

3. 在弹出的窗口中，输入开环传递函数的极点和零点。

4. 点击 "Plot Root Locus" 按钮，程序将绘制根轨迹图。

## 示例

例如，对于以下开环传递函数：
G(s) = K(s+1.5)(s+2+j)(s+2-j)/(s(s+2.5)(s+0.5+1.5j)(s+0.5-1.5j))

输入对应的极点和零点，然后点击 "Plot Root Locus" 按钮，程序将生成相应的根轨迹图。

## 支持

如果您在使用过程中遇到任何问题或需要帮助，请提交一个Issue，我们将尽快回复。

## 许可证

本项目基于 [MIT License](LICENSE) 开源。

