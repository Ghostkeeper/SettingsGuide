#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import enum #To implement fillMode.
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

	class FillMode(enum.IntEnum):
		"""
		The different fill modes available.

		This mirrors the fill modes in QML in the Image object. However that
		object is not exposed to Python by PyQt (as far as I know) so that data
		is mirrored here. This data was obtained by setting the fillMode
		property of SVGImage to different values from the Image.fillMode enum
		and logging the integer parameter provided to setFillMode.
		"""
		Stretch = 0
		PreserveAspectFit = 1
		PreserveAspectCrop = 2
		Tile = 3
		TileVertically = 4
		TileHorizontally = 5
		Pad = 6

	def __init__(self, parent=None) -> None:
		"""
		Initialises with out any SVG image. The image is set with setSource().
		:param parent: The parent QML item this image is contained in.
		"""
		super(SVGImage, self).__init__(parent)

		self._svg_item = None
		self._source = PyQt5.QtCore.QUrl("")
		self._style_options = PyQt5.QtWidgets.QStyleOptionGraphicsItem() #Defaults.
		self._fill_mode = self.FillMode.Stretch

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
		self.resize(self.width, self.height)

		self._svg_item.renderer().repaintNeeded.connect(self.update)
		self.update()

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

	def resize(self, width: float, height: float) -> None:
		"""
		Resizes the image to a certain size.

		The actual size of the drawn image depends on the fillMode property. It
		may be smaller than the desired width and height.
		:param width: The new width of the drawing area.
		:param height: The new height of the drawing area.
		"""
		if self.defaultSize.width() <= 0 or self.defaultSize.height() <= 0: #Can't rescale to infinite ratio to fill the desired area. Leave it at 0.
			return
		if width <= 0 or height <= 0: #Invalid parameters. Don't give an error though because it'll get called from QML which can't handle the Python errors.
			return
		scale_x = width / self.defaultSize.width()
		scale_y = height / self.defaultSize.height()
		if self._fill_mode == self.FillMode.Stretch or self._fill_mode == self.FillMode.Tile or self._fill_mode == self.FillMode.TileHorizontally or self._fill_mode == self.FillMode.TileVertically:
			#Tile is not supported.
			pass
		elif self._fill_mode == self.FillMode.PreserveAspectCrop:
			scale_x = max(scale_x, scale_y)
			scale_y = scale_x
		elif self._fill_mode == self.FillMode.PreserveAspectFit:
			scale_x = min(scale_x, scale_y)
			scale_y = scale_x
		elif self._fill_mode == self.FillMode.Pad:
			scale_x = 1
			scale_y = 1
		viewbox = self._svg_item.renderer().viewBox()
		view_x = viewbox.x() / scale_x
		view_y = viewbox.y() / scale_y
		view_w = viewbox.width() / scale_x
		view_h = viewbox.height() / scale_y
		self._svg_item.renderer().setViewBox(PyQt5.QtCore.QRectF(view_x, view_y, view_w, view_h))
		self.sizeChanged.emit()

	def setWidth(self, width: float) -> None:
		"""
		Changes the width of the image.
		:param width: The new width.
		"""
		super().setWidth(width)
		self.resize(width, self.height)

	def setHeight(self, height: float) -> None:
		"""
		Changes the height of the image.
		:param height: The new height.
		"""
		super().setHeight(height)
		self.resize(self.width, height)

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

	fillModeChanged = PyQt5.QtCore.pyqtSignal()

	def setFillMode(self, fill_mode: FillMode) -> None:
		"""
		Changes the way in which the image fills the space allotted for the
		image.
		:param fill_mode: The new fill mode to use.
		"""
		self._fill_mode = fill_mode
		self.resize(self.width, self.height)

	@PyQt5.QtCore.pyqtProperty(int, fset=setFillMode, notify=fillModeChanged)
	def fillMode(self):
		"""
		Returns the current fill mode to fill the allotted area for the image.
		:return: The current fill mode to fill the allotted area for the image.
		"""
		return self._fill_mode