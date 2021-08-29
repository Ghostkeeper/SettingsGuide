module yen(size,thickness) {
    linear_extrude(thickness) {
        text(text="¥", size=size);
    }
}

yen(100, 1);