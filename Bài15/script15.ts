// # Gán kiểu `any` cho một biến
let randomValue: any = 24;
console.log("---check randomValue: ", randomValue);

randomValue = "KĐ";
console.log("---check randomValue: ", randomValue);

randomValue = true;
console.log("---check randomValue: ", randomValue);
/* 
Trong ví dụ `này`:
    - Biến randomValue được khai báo với kiểu `any`.
    - Chúng ta có thể gán bất kỳ giá trị nào cho randomValue mà không gặp lỗi kiểu.
*/




// # Sử dụng `any` trong hàm
function logValue(value: any): void {
    console.log(">>>check logValue", value);
}

logValue(true)
logValue("TNKD")
logValue({ key: "ĐoanTrang" })
/*
Trong ví dụ `này`:
    - Hàm logValue nhận một tham số có kiểu `any`.
    - Hàm có thể được gọi với bất kỳ giá trị nào và giá trị đó sẽ được in ra mà không gặp lỗi.
*/





// # Sử dụng `any` với các đối tượng phức tạp
let complexObject: any = { name: "TNKD", age: 23 }; // Biến complexObject có kiểu `any` chứa các đối tượng
console.log("---> check complexObject: ", complexObject);
// console.log("---> check complexObject: ", complexObject["age"]);


complexObject = ["Đoan Trang", "Thanh Hà"]; // Biến complexObject có kiểu `any` chứa các mảng
console.log("---> check complexObject: ", complexObject);
// console.log("---> check complexObject: ", complexObject[0]);


complexObject = () => "TNKĐ"; // Biến complexObject có kiểu `any` chứa các hàm
console.log("---> check complexObject: ", complexObject());
