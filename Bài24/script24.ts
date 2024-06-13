
let dowhile: number = 6
do {
    console.log("--> check dowhile = ", dowhile)
    if (dowhile % 2 === 1) break;
    dowhile++;
} while (dowhile < 5);





function dowhileLoop(limit: number): void {
    let count: number = 0
    do {
        console.log("--- Check dowhileLoop = ", count)
        count++;
    } while (count < limit);
}
dowhileLoop(2)

/*
    Giải thích ví dụ:
        - Khởi tạo biến count:
            + Biến count được khai báo với kiểu dữ liệu number và được khởi tạo giá trị bằng 0.

        - Vòng lặp do...while:
            + Thân vòng lặp:
                ` console.log("--- Check dowhileLoop = ", count);: In ra giá trị hiện tại của count.
                ` count++: Tăng giá trị của count lên 1 sau mỗi lần lặp.

            + Điều kiện:
                ` count < limit: Vòng lặp sẽ tiếp tục chạy miễn là count nhỏ hơn giá trị của limit.
*/