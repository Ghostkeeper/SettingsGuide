$fs = 0.3;
$fa = 1;

module arc() {
	rotate([0, 90, 0]) {
		difference() {
			cylinder(r=20, h=5);
			cylinder(r=17, h=6);
			translate([0, -21, 0]) {
				cube([21, 42, 6]);
			}
		}
	}
}

middle_remove = 3;
intersection() {
	arc();
	translate([0, -20, 0]) {
		cube([5, 20 - middle_remove, 20]);
	}
}
translate([0, -middle_remove * 2, 0]) {
	intersection() {
		arc();
		translate([0, middle_remove, 0]) {
			cube([5, 20 - middle_remove, 20]);
		}
	}
}

translate([5, -20, 0]) {
	cube([10, 3, 3]);
}
translate([5, 17, 0]) {
	cube([10, 3, 3]);
}
intersection() {
	translate([5, 17, 0]) {
		rotate([0, 0, -70]) {
			cube([40, 40, 3]);
		}
	}
	translate([5, -20, 0]) {
		cube([10, 40, 3]);
	}
}
translate([5, -20, 3]) {
	cube([10, 40, 1]);
}
translate([10, 18, 4]) {
	rotate([0, 0, 30]) {
		for(i = [0:10]) {
			translate([0, 0, i/2]) {
				cylinder($fn=3, r1=3, r2=5 + i / 2, h=6 - i / 2);
			}
		}
	}
}
translate([2.5, -middle_remove, 19]) {
	cylinder(r1=2.5, r2=0, h=10);
}