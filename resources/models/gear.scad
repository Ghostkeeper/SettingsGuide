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

gear(height=4, radius=20, teeth_depth=3);