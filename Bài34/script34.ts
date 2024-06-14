// Public

console.log("--------Bộ điều chỉnh `Public`--------")
class toc_do {
    public name: string;

    constructor(name: string) {
        this.name = name;
    }

    public di_chuyen(khoang_cach: number): void {
        console.log(`${this.name} di chuyển được ${khoang_cach}km !`);
    }
}

let doi_tuong = new toc_do("Thanh Ninh");
// doi_tuong.name = "Hé Lo"; // Thay đổi tên name
doi_tuong.di_chuyen(20);

console.log(doi_tuong.name);


// Private


console.log("--------Bộ điều chỉnh `Private`--------")

class toc_do2 {
    private name2: string;
    constructor(name2: string) {
        this.name2 = name2;
    }

    public di_chuyen2(khoang_cach2: number): void {
        console.log(`${this.name2} di chuyển được ${khoang_cach2}m !`);
    }
}
const doi_tuong2 = new toc_do2("Khánh Đoan");
doi_tuong2.di_chuyen2(20);
// console.log(doi_tuong2.name2); // Lỗi: Thuộc tính 'name2' là private và chỉ có thể truy cập trong lớp 'toc_do2'.



// Protected


console.log("--------Bộ điều chỉnh `Private`--------")

class toc_do3 {
    protected name3: string;

    constructor(name3: string) {
        this.name3 = name3;
    }

    protected di_chuyen3(khoang_cach3: number): void {
        console.log(`${this.name3} di chuyển được ${khoang_cach3} cm !`);
    }
}

class Dog extends toc_do3 {
    constructor(name3: string) {
        super(name3)
    }

    public sua(): void {
        console.log(" Gâu Gâu");
    }

    public di_chuyen_va_sua(khoang_cach3: number): void {
        this.di_chuyen3(khoang_cach3);
        this.sua();
    }
}

let doi_tuong3 = new Dog("A Tú");
doi_tuong3.di_chuyen_va_sua(5);
// console.log(doi_tuong3.name3); //// Lỗi: Thuộc tính 'name3' là protected và chỉ có thể truy cập trong lớp 'toc_do3' và các lớp con của nó.