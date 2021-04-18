$fs = 0.3;
$fa = 1;
num_bars = 6;

module gear(height, radius, teeth_depth, teeth=30) {
	cylinder(h=height, r=radius, $fn=teeth);
	for(tooth = [0:teeth]) {
		rotate([0, 0, tooth * 360 / teeth]) {
			linear_extrude(height=height) {
				polygon(points=[[radius, 0], [cos(360 / teeth) * radius, sin(360 / teeth) * radius], [cos(180 / teeth) * (radius + teeth_depth), sin(180 / teeth) * (radius + teeth_depth)]], convexity=1);
			}
		}
	}
}

module bar(height, length, maxwidth, minwidth) {
	linear_extrude(height=height) {
		translate([0, -maxwidth / 2]) {
			difference() {
				square([length, maxwidth]);

				deltawidth = (maxwidth - minwidth) / 2;
				//Calculate the appropriate radius for the circles to subtract.
				//Over the course of half the length in Y, the circle must drop by the difference between min and max in X.
				//cos(a) * R = R - deltawidth
				//cos(-a) * R = R - deltawidth
				//sin(a) * R = length / 2
				//sin(-a) * R = -length / 2
				//Thanks to WolframAlpha:
				//R = (4 * deltawidth^2 + length^2) / (8 * deltawidth)
				radius = (4 * deltawidth * deltawidth + length * length) / (8 * deltawidth);
				translate([length / 2, radius + maxwidth - minwidth / 2]) {
					circle(r=radius);
				}
				translate([length / 2, -radius + deltawidth]) {
					circle(r=radius);
				}
			}
		}
	}
}

difference() {
	gear(height=4, radius=20, teeth_depth=3);
	translate([0, 0, -1]) {
		cylinder(r=18, h=6);
	}
}
difference() {
	cylinder(r=5, h=4);
	translate([0, 0, -1]) {
		cylinder(r=3, h=6);
	}
}

angle_step = 360 / num_bars;
for(a = [0:angle_step:360 - angle_step]) {
	rotate([0, 0, a]) {
		translate([4, 0, 0]) {
			bar(4, 15, 2, 1);
		}
	}
}