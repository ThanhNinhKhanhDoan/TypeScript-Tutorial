// Định nghĩa các chữ ký
function add(a: string, b: string): string;
function add(a: number, b: number): number;

// Định nghĩa thực thi duy nhất
function add(a: any, b: any): any {
    return a + b;
}

// Sử dụng hàm với chuỗi
const result1 = add("Hello, ", "world");
console.log("Check result1: ", result1);

// Sử dụng hàm với số
const result2 = add(10, 20);
console.log("Check result2: ", result2);
/*
    Giải thích:
        - Overload Signatures: Hai chữ ký được định nghĩa:
            + function add(a: string, b: string): string;
            + function add(a: number, b: number): number;

        - Implementation Signature: Chữ ký thực thi duy nhất:
            + function add(a: any, b: any): any { return a + b; }
            ` Hàm thực thi này chứa logic để thực hiện phép cộng. Nó sử dụng kiểu any để chấp nhận bất 
            kỳ loại đầu vào nào. Logic này sẽ hoạt động dựa trên kiểu dữ liệu thực tế được truyền vào.`

        - Sử dụng hàm:
            + Khi gọi add("Hello, ", "world!"), TypeScript sử dụng chữ ký đầu tiên và trả về một chuỗi.
            + Khi gọi add(10, 20), TypeScript sử dụng chữ ký thứ hai và trả về một số.
*/
