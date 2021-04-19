$fs = 0.4;
$fa = 1;

minkowski() {
	difference() {
		union() {
			cube([60, 30, 5]);
			translate([7, 30, 0]) {
				cylinder(r=7, h=5);
			}
			translate([53, 30, 0]) {
				cylinder(r=7, h=5);
			}
		}
		translate([7, 30, 0]) {
			cylinder(r=5, h=5);
		}
		translate([53, 30, 0]) {
			cylinder(r=5, h=5);
		}
		translate([30, 7, 0]) {
			cylinder(r=5, h=5);
		}
		translate([30, 30, 0]) {
			cylinder(r=16, h=5);
		}
	}
	cylinder(r1=2, r2=0, h=2);
}
translate([3, 3, 7]) {
	hook();
}
translate([57, 3, 7]) {
	mirror([1, 0, 0]) {
		hook();
	}
}


module hook() {
	cube([10, 20, 10]);
	translate([-4, 0, 10]) {
		cube([14, 20, 4]);
	}
	translate([-2, 0, 8]) {
		difference() {
			cube([2, 20, 2]);
			rotate([-90, 0, 0]) {
				cylinder(r=2, h=20);
			}
		}
	}
}