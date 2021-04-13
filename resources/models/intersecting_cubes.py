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
	Generates an STL file representing the "Intersecting Cubes" model.

	This model consists of two cubes, one of which is moved diagonally such that the two cubes intersect in one corner.
	:param filename: The file to write the model to.
	"""
	# Sizes of the two cubes.
	width = 20
	offset = 10  # The second cube is moved this distance in X, Y and Z.

	# Generate the vertices of one cube, which gets duplicated for both cubes.
	verts = [[
		[0, 0, 0],
		[width, 0, 0],
		[width, width, 0],
		[0, width, 0],
		[0, 0, width],
		[width, 0, width],
		[width, width, width],
		[0, width, width]
	]]
	verts.append([[coord + offset for coord in vert] for vert in verts[0]])

	# Then write all surfaces to the file.
	with open(filename, "w") as f:
		f.write("solid extra_surface\n")

		for i in range(len(verts)):  # Write two cubes, with 0 and 10 offset.
			write_face(f, verts[i][0], verts[i][2], verts[i][1])  # -Z
			write_face(f, verts[i][2], verts[i][0], verts[i][3])
			write_face(f, verts[i][4], verts[i][5], verts[i][6])  # +Z
			write_face(f, verts[i][6], verts[i][7], verts[i][4])
			write_face(f, verts[i][0], verts[i][1], verts[i][5])  # -Y
			write_face(f, verts[i][5], verts[i][4], verts[i][0])
			write_face(f, verts[i][3], verts[i][6], verts[i][2])  # +Y
			write_face(f, verts[i][6], verts[i][3], verts[i][7])
			write_face(f, verts[i][0], verts[i][7], verts[i][3])  # -X
			write_face(f, verts[i][0], verts[i][4], verts[i][7])
			write_face(f, verts[i][1], verts[i][6], verts[i][5])  # +X
			write_face(f, verts[i][1], verts[i][2], verts[i][6])

		f.write("endsolid extra_surface")