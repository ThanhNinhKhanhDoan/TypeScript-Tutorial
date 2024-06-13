function getTotal(...number: number[]): number {
    let total = 0;
    number.forEach((num) => total += num);


    return total;
}
console.log(getTotal());
console.log(getTotal(10, 20));
console.log(getTotal(10, 20, 30));
console.log("-----------------------");


function multiply(n: number, ...m: number[]) {
    let x = m.map((x) => {
        console.log("Check x =", x)
        return n * x;
    });

    return m.map((x) => n * x);
}
const ket_qua = multiply(10, 1, 2, 3, 4);

console.log("Check ket_qua: ", ket_qua);




console.log("-----------------------");
function Greet(greeting: string, ...names: string[]) {
    return greeting + " " + names.join(",") + "!"
}

console.log("Check Greet: ", Greet("Xin Chao", "TNKD", " Zìa Zia"));
console.log("Hello");



console.log("-----------------------");
console.log("-----------------------");
// Kết Hợp Tham Số Cố Định và Rest Parameters
console.log("-----------Kết Hợp Tham Số Cố Định và Rest Parameters------------");
function greet(greeting: string, ...names: string[]): void {
    names.forEach(name => {
        console.log(`${greeting}, ${name}!`);
    });
}

greet("Hello", "Alice", "Bob", "Charlie");
// In ra:
// Hello, Alice!
// Hello, Bob!
// Hello, Charlie!

greet("Hi");
// Không in gì cả vì mảng `names` rỗng