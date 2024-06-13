for (let index = 0; index < 9; index++) {
    if (index % 2 === 1) {
        continue;
    }
    console.log("--> check index = ", index);
    // Vòng lặp sẽ in ra giá trị của index từ 0 đến 8 (do index < 9).
    // Các giá trị của index mà là số lẻ (1, 3, 5, 7) sẽ bị bỏ qua do lệnh continue.
}






// Sử dụng continue trong vòng lặp for
function printEventNumbers(limit: number): void {
    for (let i = 0; i <= limit; i++) {
        if (i % 2 !== 0) {
            continue; // Bỏ qua các số lẻ và chuyển sang lần lặp tiếp theo
        }
        console.log("+++ Check i = ", i)
    }
}
printEventNumbers(10)

/*
    Giải thích code:
        - Hàm printEvenNumbers:
            + Nhận vào một số limit để xác định phạm vi in ra các số chẵn.

        - Vòng lặp for:
            + Vòng lặp chạy từ 0 đến limit.
            + Kiểm tra nếu i là số lẻ bằng cách sử dụng điều kiện if (i % 2 !== 0).
            + Nếu i là số lẻ, lệnh continue sẽ được thực thi, bỏ qua việc in ra số lẻ và chuyển sang lần lặp tiếp theo.
            + Nếu i là số chẵn, số đó sẽ được in ra.
*/





//  Sử dụng continue trong vòng lặp while
function printNonNegativeNumber(arr: number[]): void {
    let index: number = 0;
    while (index < arr.length) {
        if (arr[index] < 0) {
            index++;
            continue; // Bỏ qua các số âm và chuyển sang lần lặp tiếp theo
        }

        console.log("/// Check arr[index] = ", arr[index]); // Chỉ in ra các số không âm
        index++;
    }
}

const numbers: number[] = [-1, 2, -3, 4, -5, 6];
printNonNegativeNumber(numbers);
/*
    Giải thích code:
        - Hàm printNonNegativeNumbers:
            + Nhận vào một mảng arr chứa các số.

        - Vòng lặp while:
            + Vòng lặp chạy từ 0 đến độ dài của mảng.
            + Kiểm tra nếu phần tử tại index là số âm bằng cách sử dụng điều kiện if (arr[index] < 0).
            + Nếu phần tử là số âm, lệnh continue sẽ được thực thi, bỏ qua việc in ra số âm và chuyển sang lần lặp tiếp theo.
            + Nếu phần tử là số không âm, số đó sẽ được in ra.
            + Sau mỗi lần lặp, giá trị của index sẽ được tăng lên 1.
*/