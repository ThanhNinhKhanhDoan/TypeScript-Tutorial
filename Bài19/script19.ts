
type NTN = string | number | object | boolean
function addNumberString(a: NTN, b: string | number | object | boolean) {
    if (typeof a === 'number' && typeof b === 'number') {
        return a + b;
    }
    if (typeof a === 'string' && typeof b === 'string') {
        return a.concat(b); // hàm concat là để gộp phần tử lại với nhau
    }

    throw new Error("Tham số phải là số hoặc chuỗi");

}
console.log("==> check addNumberString: ", addNumberString("TN ", "KD"));