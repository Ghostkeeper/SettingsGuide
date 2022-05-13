base_width = 5;
min_tooth = 2.5;
max_tooth = 15;
inc_tooth = 2.5;
tooth_size = 30;

function sum(list) = list ? [for(p = list) 1] * list : 0;

module tooth(angle) {
	width = sin(angle / 2) * tooth_size * 2;
	difference() {
		translate([width / 2, 0, 0]) {
			scale([width / 2 / tooth_size, 1, 1]) {
				cylinder(h=1, r=tooth_size, $fn=4);
			}
		}
		translate([0, -tooth_size, -1]) {
			cube([width, tooth_size, 3]);
		}
	}
}

cube([sum([for(prev_a = [min_tooth : inc_tooth : max_tooth]) sin(prev_a / 2) * 2 * tooth_size]), base_width, 1]);
for(a = [min_tooth : inc_tooth : max_tooth]) {
	x = sum([for(prev_a = [min_tooth : inc_tooth : a - inc_tooth]) sin(prev_a / 2) * 2 * tooth_size]);
	translate([x, base_width, 0]) {
		tooth(a);
	}
}