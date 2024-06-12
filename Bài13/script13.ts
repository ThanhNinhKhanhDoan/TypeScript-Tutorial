let skills: (string | number)[] = ["KD", 23];
skills.push("DT");
skills.push(24);

console.log(">>>check skills: ", skills)

// Kiểu tuple: dataType/size/order

let kieu_tuple: [string, number] = ["TN", 23];

let kieu_tuple2: [boolean, string, number?]; // dấu hỏi đó là để khi ta tạo kiểu nhưng không bắt buộ khai báo giá trị
kieu_tuple2 = [true, "KDTN", 23]

console.log(">>>check kieu_tuple: ", kieu_tuple);
console.log(">>>check kieu_tuple2: ", kieu_tuple2);