import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

current_dir = os.path.dirname(os.path.abspath(__file__))

# ========== UserWidget Part ==========

class WindowDragger(QWidget) :
	mousePos = []
	winPos = []
	mousePressed = False

	def __init__(self, parent = None) :
		super(self.__class__, self).__init__(parent)
		self.mousePressed = False

	def mousePressEvent(self, event) :
		self.mousePressed = True
		self.mousePos = event.globalPos()

		parent = self.parentWidget()

		if parent :
			parent = parent.parentWidget()

		if parent :
			self.wndPos = parent.pos()

	def mouseMoveEvent(self, event) :
		parent = self.parentWidget()
		if parent :
			parent = parent.parentWidget()

		if parent and self.mousePressed :
			parent.move(self.wndPos + (event.globalPos() - self.mousePos))

	def mouseReleaseEvent(self, event) :
		self.mousePressed = False

	def paintEvent(self, event) :
		styleOption = QStyleOption()
		painter = QPainter(self)
		self.style().drawPrimitive(QStyle.PE_Widget, styleOption, painter, self)
