difference() {
	cube([40, 40, 8]);
	translate([20, 20, 2]) {
		cylinder(r=8, $fn=3, h=7);
	}
	translate([20, 12, 2]) {
		cylinder(r=8, $fn=3, h=7);
	}
	translate([14.5, 17, 2]) {
		cube([1, 10, 7]);
	}
	translate([13, 17, 2]) {
		cube([1, 10, 7]);
	}
	translate([11.5, 17, 2]) {
		cube([1, 10, 7]);
	}
	translate([11.5, 12.5, 2]) {
		cube([4, 4, 7]);
	}
}
translate([5, 8.6605, 8]) {
	cylinder(r1=10, r2=0, h=30, $fn=3);
}
translate([32, 32, 8]) {
	sphere(r=8, $fn=100);
}