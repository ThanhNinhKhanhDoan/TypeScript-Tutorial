function tinhtong(x, y, z) {
    if (z) {
        return x + y + z;
    }

    return x + y;
}

console.log("--- Tổng: ", tinhtong(1, 2, 3))