import sys;
import requests;
from currency_converter import CurrencyConverter
from PyQt6.QtCore import QSize, Qt;
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QLabel, QVBoxLayout;


url = 'https://api.exchangerate-api.com/v4/latest/USD';

response = requests.get(url);
conv = CurrencyConverter();
    
if response.status_code == 200:
  data = response.json();
else:
  print(f"Ошибка получения данных '{response.status_code}'");

class App(QMainWindow):
  def __init__(self):
    super().__init__();
    self.setWindowTitle("Конвертор валют");
    self.width = 800;
    self.height = 250;
    self.initUI();

  def initUI(self):
    self.label1 = QLabel("Введите исходное значение в долларах:");
    self.label2 = QLabel();
    
    self.inputBox = QLineEdit();
    self.inputBox.setMaxLength(18);
    self.inputBox.setPlaceholderText('пример: "1500" ');

    self.button = QPushButton("Нажми)", self);
    self.button.move(10,10)
    self.button.clicked.connect(self.on_click);

    layout = QVBoxLayout();
    layout.addWidget(self.label1);
    layout.addWidget(self.inputBox);
    layout.addWidget(self.label2);
    layout.addWidget(self.button);

    container = QWidget();
    container.setLayout(layout);

    self.setCentralWidget(container);
    self.setMinimumSize(QSize(300, 150));
    self.show();

  def on_click(self):
    srcValue = int(self.inputBox.text());
    finValue = str(conv.convert(srcValue, 'USD', 'RUB'));

    self.label2.setText(f"Значение в российских рублях: {finValue}");
    print(f"итог: {finValue}");
    
  
  

if __name__=='__main__':
  app = QApplication(sys.argv);
  ex = App();
  sys.exit(app.exec());