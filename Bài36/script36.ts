class Person {
    private _name: string;
    private _age: number;

    constructor(name: string, age: number) {
        this._name = name;
        this._age = age;
    }

    // Getter cho thuộc tính name
    public get name(): string {
        return this._name
    }

    // Setter cho thuộc tính name
    public set name(newName: string) {
        if (newName && newName.length > 0) {
            this._name = newName;
        } else {
            console.error("name không hợp lệ!");
        }
    }




    // Getter cho thuộc tính age
    public get age(): number {
        return this._age;
    }

    // Setter cho thuộc tính age

    public set age(newAge: number) {
        if (newAge > 0 && newAge < 150) {
            this._age = newAge;
        } else {
            console.error("age không hợp lệ!");
        }
    }

}

const person = new Person("Thanh Ninh", 23);

// Sử dụng getter để lấy giá trị
console.log(person.name);
console.log(person.age);



// Sử dụng setter để gán giá trị mới
person.name = "Khánh Đoan";
person.age = 24;

console.log(person.name);
console.log(person.age);


// Gán giá trị không hợp lệ sẽ bị từ chối
person.name = "";
person.age = -5;




console.log("---------------");
console.log("---------------");
console.log("-----Phân biệt dùng Public-----");

class PersonPublic {
    public name: string;
    public age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

let personPublic = new PersonPublic('Alice', 30);

// Truy cập trực tiếp
personPublic.name = '';
personPublic.age = -5;

console.log(personPublic.name); // Output: (empty string, không hợp lệ)
console.log(personPublic.age);  // Output: -5 (không hợp lệ)


// Như vậy, bằng cách sử dụng thuộc tính private và kết hợp với getters và setters, bạn có thể bảo vệ và kiểm soát dữ liệu của mình một cách tốt hơn.