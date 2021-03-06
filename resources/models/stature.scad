$fs = 1;
$fa = 2;

difference() {
	cylinder(r=40, h=40);
	translate([0, 0, -1]) {
		cylinder(r=30, h=42);
	}
	translate([-41, 0, 0]) {
		rotate([0, 90, 0]) {
			cylinder(r=25, h=82);
		}
	}
	translate([0, 41, 0]) {
		rotate([90, 0, 0]) {
			cylinder(r=25, h=82);
		}
	}
	translate([-41, -41, 80]) {
		rotate([-90, 0, -45]) {
			cylinder(r=50, h=120);
		}
	}
}