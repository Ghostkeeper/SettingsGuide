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
	Generates an STL file representing the "External Attachment" model.

	This model consists of a big and a small cube. The small cube is attached to the big cube without properly being
	merged into one shape. The small cube has only 5 sides, leaving the face open on the side where it is attached to
	the big cube.
	:param filename: The file to write the model to.
	"""
	# Sizes of the two cubes.
	big = 20
	small = 10

	# Pre-calculate all of the vertices.
	small_miny = big / 2 - small / 2  # The small cube is centred along Y on the +X side of the big cube.
	small_maxy = big / 2 + small / 2
	small_maxx = big + small
	big_verts = [
		[0, 0, 0],
		[big, 0, 0],
		[big, big, 0],
		[0, big, 0],
		[0, 0, big],
		[big, 0, big],
		[big, big, big],
		[0, big, big]
	]
	small_verts = [
		[big, small_miny, 0],
		[small_maxx, small_miny, 0],
		[small_maxx, small_maxy, 0],
		[big, small_maxy, 0],
		[big, small_miny, small],
		[small_maxx, small_miny, small],
		[small_maxx, small_maxy, small],
		[big, small_maxy, small],
	]

	# Then write all surfaces to the file.
	with open(filename, "w") as f:
		f.write("solid extra_surface\n")

		for verts in (big_verts, small_verts):
			write_face(f, verts[0], verts[2], verts[1])  # -Z
			write_face(f, verts[2], verts[0], verts[3])
			write_face(f, verts[4], verts[5], verts[6])  # +Z
			write_face(f, verts[6], verts[7], verts[4])
			write_face(f, verts[0], verts[1], verts[5])  # -Y
			write_face(f, verts[5], verts[4], verts[0])
			write_face(f, verts[3], verts[6], verts[2])  # +Y
			write_face(f, verts[6], verts[3], verts[7])
			if verts != small_verts:  # Leave -X face open for the small cube.
				write_face(f, verts[0], verts[7], verts[3])  # -X
				write_face(f, verts[0], verts[4], verts[7])
			write_face(f, verts[1], verts[6], verts[5])  # +X
			write_face(f, verts[1], verts[2], verts[6])

		f.write("endsolid extra_surface")