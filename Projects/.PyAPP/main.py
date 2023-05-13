import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 400, 200)

        # 设置身高和体重的标签和文本框
        self.height_label = QLabel("Height (cm)", self)
        self.height_label.move(50, 50)
        self.height_textbox = QLineEdit(self)
        self.height_textbox.move(150, 50)
        self.height_textbox.resize(200, 30)

        self.weight_label = QLabel("Weight (kg)", self)
        self.weight_label.move(50, 90)
        self.weight_textbox = QLineEdit(self)
        self.weight_textbox.move(150, 90)
        self.weight_textbox.resize(200, 30)

        # 设置计算按钮
        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.move(150, 140)
        self.calculate_button.resize(100, 30)

        # 绑定计算按钮的点击事件
        self.calculate_button.clicked.connect(self.calculate_bmi)

        # 显示窗口
        self.show()

    def calculate_bmi(self):
        # 获取身高和体重的值
        height = float(self.height_textbox.text())
        weight = float(self.weight_textbox.text())

        # 计算 BMI 值
        bmi = weight / (height / 100) ** 2

        # 显示计算结果
        result_label = QLabel(f"BMI: {bmi:.2f}", self)
        result_label.move(150, 180)
        result_label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
