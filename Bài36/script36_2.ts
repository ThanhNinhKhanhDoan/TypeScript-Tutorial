class Person1 {
    private _age: number;
    private _lastName: string;
    private _firstName: string;

    constructor(age: number, lastName: string, firstName: string) {
        this._age = age;
        this._lastName = lastName;
        this._firstName = firstName;
    }

    public get age(): number {
        return this._age;
    }

    public set age(newAge: number) {
        if (newAge > 0 && newAge < 150) {
            this._age = newAge;
        } else {
            console.error("Tuổi không hợp lệ")
        }
    }

    public get lastName(): string {
        return this._lastName;
    }

    public set lastName(newlastName: string) {
        if (newlastName && newlastName.length > 0) {
            this._lastName = newlastName;
        } else {
            console.error("Họ không hợp lệ")
        }
    }


    public get firstName(): string {
        return this._firstName;
    }

    public set firstName(newfirstName: string) {
        if (newfirstName && newfirstName.length > 0) {
            this._firstName = newfirstName;
        } else {
            console.error("Tên không hợp lệ")
        }
    }

}

let person1 = new Person1(23, "Nguyễn", "Thanh Ninh");

// Get giá trị ra
console.log(`${person1.lastName} ${person1.firstName}`);
console.log(`${person1.age} Tuổi`);



// Set giá trị vào

person1.age = 23.5;
person1.firstName = "Khánh Đoan";
person1.lastName = "Phạm";
console.log(`${person1.lastName} ${person1.firstName}`);
console.log(`${person1.age} Tuổi`);
