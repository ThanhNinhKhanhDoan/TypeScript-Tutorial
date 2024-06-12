function throwError(message: string): never {
    throw new Error(message);
}


function infiniteLoop(): void {
    // console.log("aaaa")
    while (true) {
        //vòng lặp vô hạn
        console.log("running...")

    }
}


function checkType(x: string | number) {
    if (typeof x === "string") {
        console.log("X là chuỗi string");
    } else if (typeof x === "number") {
        console.log("X là số");
    } else {
        // Đây là nơi chúng ta sử dụng `never` để kiểm tra loại biến.
        const check: never = x;
    }
}



// throwError("NTN");
// infiniteLoop();
checkType("20");


/*----------Giải Thích-----------------*
    - Hàm throwError:
        + Đầu vào: Nhận vào một chuỗi message.
        + Hành động: Ném ra một ngoại lệ với thông báo lỗi.
        + Kiểu trả về: never, vì hàm này không bao giờ trả về giá trị nào do nó luôn ném ra ngoại lệ.



    - Hàm infiniteLoop:
        + Đầu vào: Không có.
        + Hành động: Chạy vòng lặp vô tận.
        + Kiểu trả về: never, vì hàm này không bao giờ hoàn thành.


    
    - Hàm checkType:
        + Đầu vào: Nhận vào một biến x có thể là chuỗi hoặc số.
        + Hành động: Kiểm tra kiểu của x và thực hiện hành động tương ứng.
        + Kiểu trả về: Ở đây không có kiểu trả về cụ thể, nhưng chúng ta sử dụng never để kiểm tra 
            tính đầy đủ của các trường hợp. Nếu x không phải là chuỗi hoặc số (một điều không thể 
            xảy ra theo định nghĩa của hàm), TypeScript sẽ cảnh báo lỗi vì biến check không thể có 
            giá trị nào hợp lệ.




    * Kết luận:
            Kiểu never trong TypeScript rất hữu ích để chỉ các trường hợp không thể xảy ra và giúp đảm bảo 
            tính đầy đủ của kiểm tra kiểu tại compile-time. Sử dụng never có thể làm cho mã của bạn trở nên 
            an toàn hơn và giúp phát hiện lỗi sớm hơn trong quá trình phát triển.
*/