#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import PyQt5.QtCore #For QUrl.
import PyQt5.QtGui #An image to display the graphic.
import PyQt5.QtQuick
import PyQt5.QtSvg #To render the SVG image.
import PyQt5.QtWidgets #To have a GraphicsView to render on.

class SVGImage(PyQt5.QtQuick.QQuickPaintedItem):
	"""
	QML widget that displays an SVG image.

	Unlike the normal Image widget, this widget can display animated SVGs.
	Unlike the normal AnimatedImage widget, this widget can display SVGs. Best
	of both worlds.
	"""

	def __init__(self, parent=None) -> None:
		"""
		Initialises with out any SVG image. The image is set with setSource().
		:param parent: The parent QML item this image is contained in.
		"""
		super(SVGImage, self).__init__(parent)

		self._svg_item = None
		self._source = PyQt5.QtCore.QUrl("")
		self._style_options = PyQt5.QtWidgets.QStyleOptionGraphicsItem() #Defaults.

	sourceChanged = PyQt5.QtCore.pyqtSignal()

	def setSource(self, source: PyQt5.QtCore.QUrl) -> None:
		"""
		Changes the source SVG image to display.
		:param source: A URL to the new SVG image to display.
		"""
		if self._svg_item is not None:
			self._svg_item.renderer().repaintNeeded.disconnect(self.update)

		self._source = source
		self._svg_item = PyQt5.QtSvg.QGraphicsSvgItem(self._source.toLocalFile())
		if self.defaultSize.width() != 0 and self.defaultSize.height() != 0 and self.width != 0 and self.height != 0:
			scale_x = self.width / self.defaultSize.width()
			scale_y = self.height / self.defaultSize.height()
			viewbox = self._svg_item.renderer().viewBox()
			view_x = viewbox.x() / scale_x
			view_y = viewbox.y() / scale_y
			view_w = viewbox.width() / scale_x
			view_h = viewbox.height() / scale_y
			self._svg_item.renderer().setViewBox(PyQt5.QtCore.QRectF(view_x, view_y, view_w, view_h))

		self._svg_item.renderer().repaintNeeded.connect(self.update)

		self.sourceChanged.emit()

	@PyQt5.QtCore.pyqtProperty(PyQt5.QtCore.QUrl, fset=setSource, notify=sourceChanged)
	def source(self) -> PyQt5.QtCore.QUrl:
		"""
		Returns the current source SVG image that is being displayed.
		:return: The current source SVG image.
		"""
		return self._source

	def paint(self, painter: PyQt5.QtGui.QPainter) -> None:
		"""
		Updates the image.

		This is a resource-heavy operation, especially for complex SVG images.
		:param painter: The painter to paint the image with.
		"""
		if self._svg_item is not None:
			self._svg_item.paint(painter, self._style_options)

	@PyQt5.QtCore.pyqtProperty(PyQt5.QtCore.QSize, notify=sourceChanged)
	def defaultSize(self) -> PyQt5.QtCore.QSize:
		"""
		Returns the size of the actual image in the SVG file.
		:return: The size of the image in the SVG file.
		"""
		if self._svg_item is None:
			return PyQt5.QtCore.QSize(0, 0)
		return self._svg_item.renderer().defaultSize()

	sizeChanged = PyQt5.QtCore.pyqtSignal()

	def setWidth(self, width: float) -> None:
		"""
		Changes the width of the image.
		:param width: The new width.
		"""
		super().setWidth(width)
		if self.defaultSize.width() <= 0 or self.defaultSize.height() <= 0 or self.height <= 0 or width <= 0:
			return
		scale_x = width / self.defaultSize.width()
		scale_y = self.height / self.defaultSize.height()
		viewbox = self._svg_item.renderer().viewBox()
		view_x = viewbox.x() / scale_x
		view_y = viewbox.y() / scale_y
		view_w = viewbox.width() / scale_x
		view_h = viewbox.height() / scale_y
		self._svg_item.renderer().setViewBox(PyQt5.QtCore.QRectF(view_x, view_y, view_w, view_h))
		self.sizeChanged.emit()

	def setHeight(self, height: float) -> None:
		"""
		Changes the height of the image.
		:param height: The new height.
		"""
		super().setHeight(height)
		if self.defaultSize.width() <= 0 or self.defaultSize.height() <= 0 or self.width <= 0 or height <= 0:
			return
		scale_x = self.width / self.defaultSize.width()
		scale_y = height / self.defaultSize.height()
		viewbox = self._svg_item.renderer().viewBox()
		view_x = viewbox.x() / scale_x
		view_y = viewbox.y() / scale_y
		view_w = viewbox.width() / scale_x
		view_h = viewbox.height() / scale_y
		self._svg_item.renderer().setViewBox(PyQt5.QtCore.QRectF(view_x, view_y, view_w, view_h))
		self.sizeChanged.emit()

	@PyQt5.QtCore.pyqtProperty(float, fset=setWidth, notify=sizeChanged)
	def width(self) -> float:
		"""
		Gets the current width.

		Due to the fixed-ratio scaling, the image might appear smaller than this
		width.
		:return: The current width.
		"""
		return super().width()

	@PyQt5.QtCore.pyqtProperty(float, fset=setHeight, notify=sizeChanged)
	def height(self):
		"""
		Gets the current height.

		Due to the fixed-ratio scaling, the image might appear smaller than this
		height.
		:return: The current height.
		"""
		return super().height()
