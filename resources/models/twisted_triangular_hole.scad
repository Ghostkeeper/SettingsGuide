difference() {
	cylinder(r=10, h=5, $fn=3);
	translate([0, 0, -1]) {
		rotate([0, 0, 6]) {
			cylinder(r=6, h=7, $fn=3);
		}
	}
}