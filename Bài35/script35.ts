/*  `readonly` trong Interface
        - Khi sử dụng readonly trong một interface, tất cả các thuộc tính được khai báo với readonly sẽ 
            không thể bị thay đổi sau khi đối tượng được khởi tạo.
*/
console.log("-------Interface-------");

interface Person {
    readonly name: string;
    age: number;
}

const person: Person = {
    name: "NTN",
    age: 23
};

person.age = 24;
// person.name = "aaa" // Lỗi: Cannot assign to 'name' because it is a read-only property.
console.log("person: ", person);


// Trong ví dụ trên, thuộc tính name của đối tượng person là readonly, vì vậy sau khi khởi tạo giá trị "John", không thể thay đổi giá trị của nó.



/*  `readonly` trong Class
        - Trong các class, readonly có thể được sử dụng cho các thuộc tính của class. Thuộc tính này có thể được khởi tạo trong constructor và không thể thay đổi sau đó.
*/

console.log("-------Class-------");

class Car {
    readonly make: string;
    model: string;

    constructor(make: string, model: string) {
        this.make = make;
        this.model = model;
    }
}

const myCar = new Car("Mercedes", "Audi");
myCar.model = "NTN";
// myCar.make = "No" //Lỗi: Không thể gán cho 'make' vì đây là thuộc tính chỉ đọc.
console.log("myCar: ", myCar);