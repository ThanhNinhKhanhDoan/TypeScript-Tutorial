// class Person {
//     ssn: string;
//     firstName: string;
//     lastName: string;

//     constructor(ssn: string, firstName: string, lastName: string) {
//         this.ssn = ssn;
//         this.firstName = firstName;
//         this.lastName = lastName;
//     }

//     getFullName(): string {
//         return `Xin Chào: ${this.firstName} ${this.lastName}`
//     }
// }

// const person1 = new Person("Nguyễn", "Thanh", "Ninh");
// console.log("--> check class: ", person1.getFullName());











class Person {
    // Thuộc tính
    name: string;

    // Hàm khởi tạo
    constructor(name: string) {
        this.name = name;
    }

    // Phương thức
    greet(): void {
        console.log(`Hello, my name is ${this.name}`);
    }
}

// Tạo đối tượng từ class Person
const person1 = new Person("KD");

// Gọi phương thức greet
person1.greet(); // Output: Hello, my name is John





/* Tính kế thừa: 
Classes trong TypeScript cũng hỗ trợ tính kế thừa, cho phép một class 
con kế thừa thuộc tính và phương thức từ class cha:
*/

class Employee extends Person {
    // Thuộc tính mới
    employeeId: number;


    // Hàm khởi tạo
    constructor(name: string, employeeId: number) {
        super(name); // Gọi hàm khởi tạo của class cha
        this.employeeId = employeeId;
    }

    // Phương thức mới
    work(): void {
        console.log(`${this.name} is working with ID ${this.employeeId}`)
    }
}

// Tạo đối tượng từ class Employee
const employee1 = new Employee("NTN", 2409);


// Gọi phương thức kế thừa và phương thức mới
employee1.greet();
employee1.work();


/*
    Giải thích về kế thừa
        1. Định nghĩa class con:
            - `class Employee extends Person {...}`: Định nghĩa class `Employee` kế thừa
                từ class `Person.
        
        2. Thuốc tính mới:
            - `employeeId: number;`: Định nghĩa thuộc tính mới `employeeId` có kiểu `number`.

        3. Hàm khởi tạo: 
            -   constructor(name: string, employeeId: number) {
                    super(name); // Gọi hàm khởi tạo của class cha
                    this.employeeId = employeeId;
                } Hàm khởi tạo của class `Employee` nhận thêm tham số `employeeId`. Gọi
                 `super(name)` để gọi hàm khởi tạo của class cha `Person`.
                 
        4. Phương thức mới:
            - work(): void { console.log(${this.name} is working with ID ${this.employeeId}); }: 
            Phương thức work in ra một chuỗi chứa tên và ID của nhân viên.
*/