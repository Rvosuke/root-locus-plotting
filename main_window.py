import sys
from PySide2.QtWidgets import QApplication, QMainWindow,\
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from Plot import plot_root_locus
import numpy as np
import re
from cmath import polar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Root Locus Plotter")

        # Create widgets
        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        label = QLabel("Open-loop Transfer Function (e.g., K(0.5s+1)/(0.5s^2+s+1)):")
        self.input_tf = QLineEdit()
        input_layout.addWidget(label)
        input_layout.addWidget(self.input_tf)

        self.plot_button = QPushButton("Plot Root Locus")
        self.plot_button.clicked.connect(self.plot_root_locus)

        layout.addLayout(input_layout)
        layout.addWidget(self.plot_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def parse_tf(self, tf_text):
        zeros = []
        poles = []

        num = re.search(r"K\((.*?)\)/", tf_text).group(1)
        den = re.search(r"/\((.*?)\)", tf_text).group(1)

        num_terms = re.findall(r"s([\+\-][\d\.]+[j]?[\d\.]*)?", num)
        den_terms = re.findall(r"s([\+\-][\d\.]+[j]?[\d\.]*)?", den)

        for term in num_terms:
            if term == "":
                zeros.append(-0)
            else:
                zeros.append(-complex(term))
        for term in den_terms:
            if term == "":
                poles.append(-0)
            else:
                poles.append(-complex(term))

        return np.array(poles), np.array(zeros)

    def plot_root_locus(self):
        tf_text = self.input_tf.text()

        # Parse the input transfer function
        poles, zeros = self.parse_tf(tf_text)

        # Plot root locus
        K = np.linspace(0, 20, 1000)
        plot_root_locus(K, poles, zeros)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
