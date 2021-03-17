$fs = 1;
$fa = 2;

cylinder(r=30, h=10);
translate([0, 0, 10]) {
	cylinder(r1=30, r2=25, h=5);
}
difference() {
	intersection() {
		hull() {
			sphere(r=25);
			translate([0, 0, 30]) {
				sphere(r=25);
			}
		}
		translate([-25, -5, 0]) {
			cube([50, 10, 55]);
		}
	}
	translate([0, 6, 30]) {
		rotate([90, 0, 0]) {
			cylinder(r=10, h=12);
		}
	}
}