# Copyright (C) 2021 Ghostkeeper
# This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
# You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

def write_face(stream, *vertices):
	stream.write("facet\n")
	stream.write("outer loop\n")
	for vertex in vertices:
		stream.write("vertex {0} {1} {2}\n".format(*vertex))
	stream.write("endloop\n")
	stream.write("endfacet\n")

def generate(filename):
	"""
	Generates an STL file representing the "Cube Missing Corner" model.

	This model resembles a cube, but one eighth of the cube is missing, the corner in the +X, +Y, +Z direction. The
	missing corner is not closed up, resulting in a non-manifold mesh where you can see the innards of the cube through
	the missing corner.
	:param filename: The file to write the model to.
	"""
	# Size of the cube.
	width = 20

	# Pre-calculate all of the vertices.
	verts = [
		[0, 0, 0],  # Bottom side.
		[width, 0, 0],
		[width, width, 0],
		[0, width, 0],
		[0, 0, width],  # Top side.
		[width, 0, width],
		[0, width, width],
		[width / 2, width / 2, width],  # Around the missing corner.
		[width, width / 2, width],
		[width, width / 2, width / 2],
		[width, width, width / 2],
		[width / 2, width, width / 2],
		[width / 2, width, width]
	]

	# Then write all surfaces to the file.
	with open(filename, "w") as f:
		f.write("solid extra_surface\n")

		write_face(f, verts[0], verts[2], verts[1])  # -Z
		write_face(f, verts[2], verts[0], verts[3])
		write_face(f, verts[0], verts[1], verts[5])  # -Y
		write_face(f, verts[5], verts[4], verts[0])
		write_face(f, verts[0], verts[6], verts[3])  # -X
		write_face(f, verts[0], verts[4], verts[6])

		write_face(f, verts[4], verts[5], verts[6])  # +Z
		write_face(f, verts[5], verts[8], verts[7])
		write_face(f, verts[7], verts[12], verts[6])
		write_face(f, verts[2], verts[3], verts[6])  # +Y
		write_face(f, verts[2], verts[11], verts[10])
		write_face(f, verts[11], verts[6], verts[12])
		write_face(f, verts[1], verts[2], verts[5])  # +X
		write_face(f, verts[2], verts[10], verts[9])
		write_face(f, verts[9], verts[8], verts[5])

		f.write("endsolid extra_surface")