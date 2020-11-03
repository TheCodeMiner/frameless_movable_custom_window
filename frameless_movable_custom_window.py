import sys

from PySide2.QtWidgets import (
	QApplication, QMainWindow, QToolBar,
	QPushButton, QWidget, QLabel,
	QSizePolicy
	)
from PySide2.QtCore import (
	Qt, QPoint, QPointF
	) 


class MainUI(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowFlags(Qt.FramelessWindowHint)
		#self.setAttribute(Qt.WA_TranslucentBackground, True)
		self.setFixedSize(601, 401)
		self.toolbar_selected = False

		self.toolbar = QToolBar()
		self.toolbar.setObjectName("toolbar")
		self.toolbar.setMovable(False)
		self.toolbar.setFloatable(False)
		self.toolbar.setContextMenuPolicy(Qt.PreventContextMenu) # no right-click on toolbar
		self.addToolBar(self.toolbar)
		self.toolbar.setStyleSheet("background-color: khaki")

		self.admin_btn = QPushButton("Admin", self)
		self.admin_btn.setObjectName("admin_btn")
		self.admin_btn.setFixedSize(65,30)

		self.info_btn = QPushButton("Info", self)
		self.info_btn.setObjectName("info_btn")
		self.info_btn.setFixedSize(35,30)

		self.spacer = QWidget()
		self.spacer.setObjectName("toolbar_spacer")
		self.spacer.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Fixed)

		self.toolbar_label = QLabel("")
		self.toolbar_label.setObjectName("toolbar_label")
		self.toolbar_label.setAlignment(Qt.AlignCenter)
		self.toolbar_label.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Fixed)

		self.close_btn = QPushButton(" X")
		self.close_btn.setObjectName("close_btn")
		self.close_btn.setFixedSize(30,30)

		self.toolbar.addWidget(self.admin_btn)
		# self.toolbar.addWidget(self.spacer)
		self.toolbar.addWidget(self.toolbar_label)
		# self.toolbar.addWidget(self.spacer)
		self.toolbar.addWidget(self.info_btn)
		self.toolbar.addWidget(self.close_btn)

		self.toolbar_label.mousePressEvent = self.mousePressEvent # to move window 
		self.mousePressEvent = self.mousePressEvent_ # to check if window content is selected or not
		self.close_btn.pressed.connect(self.close_window)


	def mousePressEvent_(self, e):
		""" to be able to drag window just via toolbar
		I made this custome mousePressEvent to filter any click,
		other than toolbar.
		If we click on any place on the window(except the toolbar),
		this method will be activated and set the toolbar_selected=false,
		so that we won't be able do anything in normal mousePressEvent			
		"""
		self.toolbar_selected = False

	def mousePressEvent(self, e):
		self.toolbar_selected = True
		""" If defiend section is pressed 
		Activate the mouseMoveEvent to
		get the mouse positions
		"""
		self.mouse_pressed = True
		self.old_pos = e.globalPos()

	def mouseMoveEvent(self, e):
		""" move the whole window to mouse position
		"""
		if self.toolbar_selected:
			delta = QPoint(e.globalPos() - self.old_pos)
			self.move(self.x()+delta.x(), self.y()+delta.y())
			self.old_pos = e.globalPos()

	def close_window(self):
		self.close()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = MainUI()
	w.show()
	app.exec_()