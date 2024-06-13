const tinhhieu = (x: number, y: number, z?: number) => {
    if (z) {
        return x - y - z;
    }
    return x - y;
}

console.log("--- Hiệu: ", tinhhieu(4, 2, 1));
console.log("--- Hiệu2: ", tinhhieu(4, 2));



console.log("++++++++Hàm Với Nhiều Tham Số Tùy Chọn++++++++")
function greet(name: string, greeting?: string): void {
    if (greeting) {
        console.log(`${greeting} I love You ${name}!`);
    } else {
        console.log(`Hello ${name}`);
    }
}
greet("KD", "NTN")
greet("KD")



//Hàm Với Nhiều Tham Số Tùy Chọn
console.log("-----------Hàm Với Nhiều Tham Số Tùy Chọn------------")
function createUsser(name: string, age?: number, address?: string): void {
    console.log(`Name: ${name}`);
    if (age !== undefined) {
        console.log(`Age: ${age}`);
    }
    if (address !== undefined) {
        console.log(`Adress: ${address}`);
    }
}
createUsser("NTN", 25, "01 Da Man 6");
console.log("-----------------------")
createUsser("NTN", 25);
console.log("-----------------------")
createUsser("NTN");




// Tham Số Mặc Định và Tham Số Tùy Chọn
console.log("-----------Tham Số Mặc Định và Tham Số Tùy Chọn------------")
function multiply(a: number, b: number = 1): number {
    return a * b;
}
console.log("--- Kết Quả: ", multiply(5, 2));
console.log("--- Kết Quả2: ", multiply(5));
/*  `Tham số mặc định là một tham số có một giá trị mặc định nếu không được cung cấp trong khi gọi 
    hàm. Tham số mặc định có thể được kết hợp với tham số tùy chọn.`
*/