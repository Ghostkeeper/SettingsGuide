width = 20;
$fs = 0.4;
$fa = 1;

difference() {
	hull() {
		cylinder(r=2, h=3);
		translate([width, 0, 0]) {
			cylinder(r=2, h=3);
		}
		translate([width, width, 0]) {
			cylinder(r=2, h=3);
		}
		translate([0, width, 0]) {
			cylinder(r=2, h=3);
		}
	}
	translate([2, 2, -1]) {
		cylinder(r=2, h=5);
	}
	translate([width - 2, 2, -1]) {
		cylinder(r=2, h=5);
	}
	translate([width - 2, width - 2, -1]) {
		cylinder(r=2, h=5);
	}
	translate([2, width - 2, -1]) {
		cylinder(r=2, h=5);
	}
	translate([width / 2, width / 2, -1]) {
		cylinder(r=5, h=5);
	}
}