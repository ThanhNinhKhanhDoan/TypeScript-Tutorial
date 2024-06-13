function tinh_tich(a: number, b: number, z = false) {
    if (z === false) {
        return a + b;
    }
    if (z) {
        return a - b
    }
}

console.log(">>> check tinh_tich: ", tinh_tich(1, 2));
console.log(">>> check tinhtich2: ", tinh_tich(1, 2, true));



// Hàm Với Tham Số Mặc Định
console.log("--------- Hàm Với Tham Số Mặc Định ----------")

function greet(name: string, greeting: string = "Hello"): void {
    console.log(`${greeting}, ${name}!`)
}
greet("NTN", "KD");
greet("NTN");



// Hàm Với Nhiều Tham Số Mặc Định
console.log("********* Hàm Với Nhiều Tham Số Mặc Định *********")
function createUser(name: string, age: number = 18, address: string = "Not provided"): void {
    console.log(`Name: ${name}`);
    console.log(`Age: ${age}`);
    console.log(`Address: ${address}`);
}
createUser("NTN", 23, "DN");
console.log("--------------")
createUser("NTN", 23);
console.log("--------------")
createUser("NTN");


// Kết Hợp Tham Số Mặc Định và Tùy Chọn
console.log("^^^^^^^^^ Kết Hợp Tham Số Mặc Định và Tùy Chọn ^^^^^^^^^")
function displayInfo(name: string, age?: number, coutry: string = "Unknown"): void {
    console.log(`Name: ${name}`);

    if (age !== undefined) {
        console.log(`Age: ${age}`);
    }

    console.log(`Coutry: ${coutry}`);
}
displayInfo("PKD", 23, "DN");
console.log("===============")
displayInfo("PKD", 23);
console.log("===============")
displayInfo("PKD");
