# Copyright (C) 2021 Ghostkeeper
# This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
# You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

import math

def write_face(stream, *vertices):
	stream.write("facet\n")
	stream.write("outer loop\n")
	for vertex in vertices:
		stream.write("vertex {0} {1} {2}\n".format(*vertex))
	stream.write("endloop\n")
	stream.write("endfacet\n")

def generate(filename):
	"""
	Generates an STL file representing the "Extra Surface" model.

	This model contains a non-manifold surface that can't be generated with OpenSCAD, so it needs to be generated using
	a more powerful tool, such as Python.
	:param filename: The file to write the model to.
	"""
	# Some dimensions.
	circle_resolution = 360  # How many vertices approximate the circle.
	base_radius = 20
	base_top_radius = 18  # Slightly sloping for effect.
	base_thickness = 5
	pipe_radius = 10
	pipe_thickness = 1
	pipe_height = 30
	surface_angle = 120  # How big a part of a circle is spanned by the extra surface, in degrees.

	# Pre-calculate all of the vertices. We're going to re-use them.
	base_verts = []
	base_top_verts = []
	pipe_bottom_outside_verts = []
	pipe_bottom_inside_verts = []
	pipe_top_outside_verts = []
	pipe_top_inside_verts = []
	surface_top_verts = []  # Will not be of equal length! Just enough to span the surface_angle.
	for step in range(circle_resolution):
		angle = math.pi * 2 / circle_resolution * step
		cos_angle = math.cos(angle)
		sin_angle = math.sin(angle)

		base_verts.append((cos_angle * base_radius, sin_angle * base_radius, 0))
		base_top_verts.append((cos_angle * base_top_radius, sin_angle * base_top_radius, base_thickness))
		pipe_bottom_outside_verts.append((cos_angle * pipe_radius, sin_angle * pipe_radius, base_thickness))
		pipe_bottom_inside_verts.append((cos_angle * (pipe_radius - pipe_thickness), sin_angle * (pipe_radius - pipe_thickness), base_thickness))
		pipe_top_outside_verts.append((cos_angle * pipe_radius, sin_angle * pipe_radius, base_thickness + pipe_height))
		pipe_top_inside_verts.append((cos_angle * (pipe_radius - pipe_thickness), sin_angle * (pipe_radius - pipe_thickness), base_thickness + pipe_height))
		if angle <= math.pi * 2 * surface_angle / 360.0:
			surface_top_verts.append((cos_angle * base_top_radius, sin_angle * base_top_radius, base_thickness + pipe_height))

	# For simplicity, we'll just have vertices in the middle of the round flat surfaces.
	base_bottom_centre = (0, 0, 0)
	base_top_centre = (0, 0, base_thickness)

	# Then write all surfaces to the file.
	with open(filename, "w") as f:
		f.write("solid extra_surface\n")

		for step in range(circle_resolution):
			next = (step + 1) % circle_resolution

			write_face(f, base_verts[step], base_verts[next], base_bottom_centre)  # Bottom of the base.
			write_face(f, base_verts[step], base_verts[next], base_top_verts[step])  # Side of the base.
			write_face(f, base_verts[next], base_top_verts[next], base_top_verts[step])
			write_face(f, base_top_verts[step], base_top_verts[next], pipe_bottom_outside_verts[step])  # Outside top of the base.
			write_face(f, base_top_verts[next], pipe_bottom_outside_verts[next], pipe_bottom_outside_verts[step])
			write_face(f, pipe_bottom_inside_verts[step], pipe_bottom_inside_verts[next], base_top_centre)  # Inside top of the base.
			write_face(f, pipe_bottom_outside_verts[step], pipe_bottom_outside_verts[next], pipe_top_outside_verts[step])  # Outside of pipe.
			write_face(f, pipe_bottom_outside_verts[next], pipe_top_outside_verts[next], pipe_top_outside_verts[step])
			write_face(f, pipe_top_inside_verts[step], pipe_top_inside_verts[next], pipe_bottom_inside_verts[step])  # Inside of pipe.
			write_face(f, pipe_top_inside_verts[next], pipe_bottom_inside_verts[next], pipe_bottom_inside_verts[step])
			write_face(f, pipe_top_outside_verts[step], pipe_top_outside_verts[next], pipe_top_inside_verts[step])  # Top of pipe.
			write_face(f, pipe_top_outside_verts[next], pipe_top_inside_verts[next], pipe_top_inside_verts[step])
			if step < len(surface_top_verts) - 1:
				write_face(f, base_top_verts[step], base_top_verts[next], surface_top_verts[step])  # Extra surface.
				write_face(f, base_top_verts[next], surface_top_verts[next], surface_top_verts[step])

		f.write("endsolid extra_surface")