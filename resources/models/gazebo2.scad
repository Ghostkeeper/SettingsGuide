$fn=40;
difference() {
	cube(40);
	translate([20, 5, 10])
		sphere(r=20);
	translate([10, 25, 14])
		sphere(r=25);
}