$fn = 30;
first_distance = 1.2;
first_radius = 5;
second_distance = 0.4;
second_radius = 3;

difference() {
	cube([20, 15, 3]);
	translate([first_distance + first_radius, 7.5, 0])
		cylinder(r=first_radius, h=3);
	translate([first_distance + first_radius * 2 + second_distance + second_radius, 7.5, 0])
		cylinder(r=second_radius, h=3);
}