$fn = 120;
radius = 7.5;
taper_frac = 0.2;
text_depth = 1;

difference() {
	sphere(r=radius);
	translate([-radius, -radius, -radius]) {
		cube([radius * 2, radius * 2, radius * taper_frac]);
	}
	translate([0, 0, radius - text_depth]) {
		linear_extrude(height = text_depth) {
			text("1", halign="center", valign="center", size=6);
		}
	}
}