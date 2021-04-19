width = 15;
thickness = 2;
length = 70;
screw_radius = 1.5;

$fs = 0.3;
$fa = 1;

difference() {
	hull() {
		cylinder(r=width / 2, h=thickness);
		translate([length, 0, 0]) {
			cylinder(r=width / 2, h=thickness);
		}
	}
	translate([length, 0, -1]) {
		cylinder(r=screw_radius, h=thickness + 2);
	}
	translate([0, 0, -1]) {
		hull() {
			cylinder(r=screw_radius, h=thickness + 2);
			translate([screw_radius * 2, width + screw_radius * 3, 0]) {
				cylinder(r=screw_radius * 3, h=thickness + 2);
			}
		}
	}
}