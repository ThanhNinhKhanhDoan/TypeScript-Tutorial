let count: number = 0;
while (count < 5) {
    console.log("--> ouput count: ", count);
    if (count % 2 === 1) break;
    count++;
}




function printNumbersUntilLimit(limit: number): void {
    let i = 1;
    while (i <= limit) {
        console.log("==> ouput printNumbersUntilLimit = ", i)
        i++;
    }
}
printNumbersUntilLimit(5);







//Vòng lặp while với mảng
function printArrNumbersUntilLimit(arr: number[]): void {
    let i = 0;
    while (i < arr.length) {
        console.log("==> ouput printArrNumbersUntilLimit = ", arr[i]);
        i++
    }
}

const numbers1: number[] = [10, 20, 30, 40, 50];
printArrNumbersUntilLimit(numbers1)

/*
    Giải thích ví dụ:
        - Hàm printArrayElementsUsingWhile:
            + Đầu vào: Nhận vào một mảng arr kiểu number[].
            + Khởi tạo biến: let i = 0 - biến i được khởi tạo với giá trị 0.

        - Vòng lặp while:
            + Điều kiện: i < arr.length - vòng lặp tiếp tục khi i nhỏ hơn độ dài của mảng arr.
            + Thân vòng lặp:
                ` console.log(arr[i]); - in ra phần tử thứ i của mảng arr.
                ` i++; - tăng giá trị của i lên 1 sau mỗi lần lặp.

        - Gọi hàm printArrayElementsUsingWhile:
            + Hàm sẽ in ra các phần tử của mảng numbers, cụ thể là 10, 20, 30, 40, 50.
*/