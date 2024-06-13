function getDiscount(gia: number): number {
    let voucher: number;

    if (gia > 100 && gia < 120) {
        voucher = 20;
    } else if (gia > 50 && gia <= 100) {
        voucher = 10;
    } else {
        voucher = 5;
    }
    return voucher;
}

console.log("--> Check getDiscount: ", getDiscount(50));




let age: number = 17;

if (age >= 18) {
    console.log("Đủ Tuổi Quất...");
} else if (age >= 16 && age < 18) {
    console.log("Cần Sự Đồng Ý Của Đối Phương Mới Được...");
} else {
    console.log("Bóc Lịch Đó Con");
}
