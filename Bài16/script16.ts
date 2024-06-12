let logMessage = (message: string): void => {  // khai báo hàm kiểu rút gọn
    console.log("--> ouput logMessage: ", message);
}


function add(a: number, b: number): number {
    return a + b;
}


function doNothing(): void {

}

// Gọi hàm logMessage
logMessage("Sơn Tùng MTP");


// Gọi hàm add
let sum = add(4, 5);
console.log("--> ouput add: ", sum);


// Gọi hàm doNothing
doNothing();


/*------------Giải Thích------------- */

/*
    - Hàm logMessage:
        + Đầu vào: Nhận vào một chuỗi message.
        + Hành động: In ra console giá trị của message.
        + Kiểu trả về: void, nghĩa là hàm này không trả về bất kỳ giá trị nào.


    - Hàm add:
        + Đầu vào: Nhận vào hai số a và b.
        + Hành động: Tính tổng của a và b.
        + Kiểu trả về: number, hàm này trả về giá trị của tổng a và b.

    
    - Hàm doNothing:
        + Đầu vào: Không có.
        + Hành động: Không làm gì cả.
        + Kiểu trả về: void, hàm này không trả về bất kỳ giá trị nào.

    *Kiểu void trong TypeScript chủ yếu được sử dụng để chỉ ra rằng một hàm
        không trả về giá trị nào. Điều này giúp mã của bạn trở nên rõ ràng hơn 
        và dễ hiểu hơn, đồng thời tận dụng lợi thế của hệ thống kiểu mạnh mẽ của
        TypeScript để tránh lỗi runtime.
*/