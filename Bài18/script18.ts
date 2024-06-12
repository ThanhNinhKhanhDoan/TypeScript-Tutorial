function addNumberString(a: any, b: any) {
    if (typeof a === 'number' && typeof b === 'number') {
        return a + b;
    }
    if (typeof a === 'string' && typeof b === 'string') {
        return a.concat(b); // hàm concat là để gộp phần tử lại với nhau
    }

    throw new Error("Tham số phải là số hoặc chuỗi");

}
// console.log("==> check addNumberString: ", addNumberString(2001, 24));



function printId(id: number | string): void {
    if (typeof id === "string") {
        console.log(`ID is a string: ${id.toUpperCase()}`);
    } else {
        console.log(`ID is a number: ${id}`);
    }
}

// Gọi hàm với giá trị kiểu string
printId("abc123"); // Kết quả sẽ là "ID is a string: ABC123"

// Gọi hàm với giá trị kiểu number
printId(123);      // Kết quả sẽ là "ID is a number: 123"






// let data: (number | string)[] | null;

// data = [1, "two", 3, "four"];  // Hợp lệ
// data = null;                   // Hợp lệ
// data = [1, 2, 3];              // Hợp lệ
// data = "not an array";         // Không hợp lệ