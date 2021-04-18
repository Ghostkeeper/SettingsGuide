$fs = 0.4;
$fa = 1;

difference() {
	translate([0, 0, -30]) {
		sphere(r=40);
	}
	translate([-40, -40, -70]) {
		cube([80, 80, 70]);
	}
	translate([-8, 0, -1]) {
		cylinder(r=8, h=12);
	}
	translate([8, 0, -1]) {
		cylinder(r=8, h=12);
	}
	translate([0, 0, -1]) {
		cylinder(r=5, h=12, $fn=4);
	}
	translate([0, 30, 10]) {
		sphere(r=12);
	}
	translate([0, -30, 10]) {
		sphere(r=12);
	}
}