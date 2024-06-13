function forLoopprintNumbers(): void {
    for (let i = 0; i < 10; i++) {
        console.log("--> ouput i: ", i);
    }
}
forLoopprintNumbers()


// Vòng lặp for với Mảng
function printArrayElements(arr: number[]): void {
    for (let i = 0; i < arr.length; i++) {
        console.log("*** Check printArrayElements: ", arr[i])
    }
}

const numbers: number[] = [10, 20, 30, 40, 50];
printArrayElements(numbers);