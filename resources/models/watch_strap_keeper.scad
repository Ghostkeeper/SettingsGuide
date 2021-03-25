gap_width = 25.5;
gap_height = 9;
size = 6;
thickness = 1;

$fa = 1;
$fs = 0.1;

difference() {
	hull() {
		cylinder(r=gap_height / 2 + thickness, h=size);
		translate([gap_width - gap_height, 0, 0]) {
			cylinder(r=gap_height / 2 + thickness, h=size);
		}
	}
	hull() {
		translate([0, 0, -1]) {
			cylinder(r=gap_height / 2, h=size + 2);
		}
		translate([gap_width - gap_height, 0, -1]) {
			cylinder(r=gap_height / 2, h=size + 2);
		}
	}
}