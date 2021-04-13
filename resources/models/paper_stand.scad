paper_thickness = 0.6;
thickness = 1;
paper_height = 230;
max_width = 30;
min_width = 5;
stand_angle = 20;
stand_length = 80;

$fn = 30;
$fs = 0.3;
$fa = 1;

intersection() {
	difference() {
		hull() {
			cylinder(r=thickness + paper_thickness / 2, h=max_width);
			translate([thickness * 2 + paper_height, 0, 0]) {
				cylinder(r=thickness + paper_thickness / 2, h=max_width);
			}
		}
		translate([thickness, -paper_thickness / 2, -1]) {
			cube([paper_height, paper_thickness, max_width + 2]);
		}
	}
	union() {
		hull() { //Base height of min_width.
			cylinder(r=thickness + paper_thickness / 2, h=min_width);
			translate([thickness * 2 + paper_height, 0, 0]) {
				cylinder(r=thickness + paper_thickness / 2, h=min_width);
			}
		}
		//The curve is a stack of cones.
		curve_width = paper_height + thickness;
		for(i = [1:$fn]) {
			frac_lower = 1 / (i / $fn) / $fn;
			frac_higher = 1 / ((i + 1) / $fn) / $fn;
			translate([0, 0, min_width + (i - 1) / $fn * (max_width - min_width)]) {
				cylinder(r1=(thickness + paper_thickness / 2) * (1 - frac_lower) + curve_width * frac_lower, r2=(thickness + paper_thickness / 2) * (1 - frac_higher) + curve_width * frac_higher, h=(max_width - min_width) / $fn);
			}
		}
	}
}

rotate([0, 0, -stand_angle]) {
	hull() {
		cylinder(r=thickness + paper_thickness / 2, h=max_width);
		translate([0, stand_length, 0]) {
			cylinder(r=thickness + paper_thickness / 2, h=min_width);
		}
	}
}