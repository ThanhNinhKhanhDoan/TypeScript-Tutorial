function tinhtong(a: number, b: number) {
    return a + b;
}

console.log("Tổng: ", tinhtong(24, 24));


const tinhhieu = (a: number, b: number) => {
    return a - b;
}
console.log("Hiệu: ", tinhhieu(24, 9));







// Callback
function callbackExample(message: string): void {
    console.log("Callback executed: " + message);
}

function processData(data: string, callback: (message: string) => void): void {
    // Giả sử chúng ta xử lý dữ liệu ở đây
    let processedData = data.toUpperCase();

    // Gọi hàm callback với kết quả xử lý
    callback(processedData);
}

processData("hello, world", callbackExample);