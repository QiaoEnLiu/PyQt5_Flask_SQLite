import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import QTimer
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        print('UI Activate1')

        self.init_ui()

    def init_ui(self):
        print('UI Activate2')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel('Datas:')
        self.layout.addWidget(self.label)

        self.btn_refresh = QPushButton('Refresh Datas')
        self.btn_refresh.clicked.connect(self.refresh_datas)
        self.layout.addWidget(self.btn_refresh)

        self.central_widget.setLayout(self.layout)

        self.setWindowTitle('PyQt5 with Flask API')
        self.setGeometry(300, 300, 400, 1000)

    def refresh_datas(self):
        print('Get Datas')
        # 發送GET請求到Flask API端點
        response = requests.get('http://localhost:5000')

        if response.status_code == 200:
            datas = response.json().get('R4X', [])
            data_text = '\n'.join([f"Reg: {data['Reg']}, Name: {data['Name']}, Value: {data['Value']}" for data in datas])
            self.label.setText(f'R4X:\n{data_text}')
        else:
            self.label.setText('Error fetching datas.')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 建立Qt應用程式和主視窗
    ex = MyApp()
    ex.show()

    # 使用定時器來檢查Flask API是否已經啟動
    timer = QTimer()
    timer.timeout.connect(ex.refresh_datas)
    timer.start(1000)  # 1秒檢查一次

    sys.exit(app.exec_())