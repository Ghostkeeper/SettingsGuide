$fs = 0.2;
$fa = 1;

intersection() {
	rotate([0, 90, 0]) {
		cylinder(r=20, h=60);
	}
	translate([0, -20, 0]) {
		cube([60, 40, 20]);
	}
}
translate([60, 0, 0]) {
	cylinder(r=20, h=40);
	translate([0, 0, 40]) {
		cylinder(r1=20, r2=5, h=5);
	}
	translate([0, 0, 45]) {
		cylinder(r=5, h=5);
	}
	translate([0, 0, 50]) {
		sphere(r=5);
	}
}