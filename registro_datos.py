from PyQt5 import uic 
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys 

class Principal(QMainWindow):

	def __init__(self):
		self.column = 0
		self.row = 0
		self.count_row = 2
		super(Principal, self).__init__()
		uic.loadUi("registro_datos.ui", self)
		self.datos.setColumnWidth(0, 145)
		self.datos.setColumnWidth(1, 145)
		self.datos.setColumnWidth(2, 65)
		self.imprimir.clicked.connect(self.imprimir_datos)

	#debe permitir avanzar de fila
	def imprimir_datos(self):
		name = self.nombre.text()
		lastname = self.apellido.text()
		age = self.edad.text()

		self.datos.setRowCount(self.count_row)
		self.row = 0

		self.datos.setItem(self.column, self.row, QTableWidgetItem(name))
		self.row +=1
		self.datos.setItem(self.column, self.row, QTableWidgetItem(lastname))
		self.row +=1
		self.datos.setItem(self.column, self.row, QTableWidgetItem(age))
		self.column += 1
		self.count_row += 1

		self.nombre.setText("")
		self.apellido.setText("")
		self.edad.setText("")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = Principal()
	main.show()
	sys.exit(app.exec())

