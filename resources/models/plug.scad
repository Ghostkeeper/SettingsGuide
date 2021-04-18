module buttplug(fn) {
    union() {
        translate([-5, -5, 0]) {
            cube([10, 10, 35]);
        }
        translate([-25, -5, 0]) {
            cube([50, 10, 5]);
        }
        translate([0, 0, 20]) {
            difference() {
                sphere(r=25, $fn=fn);
                translate([3, 0, -10]) {
                    sphere(r=25, $fn=fn);
                }
                translate([-25, -25, -20]) {
                    cube([50, 50, 15]);
                }
            }
        }
    }
}

buttplug(fn=50);