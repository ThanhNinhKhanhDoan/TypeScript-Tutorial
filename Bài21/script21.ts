function getDayName(day: number): string {
    let dayName: string;
    switch (day) {
        case 0:
            dayName = "Sunday";
            break;
        case 1:
            dayName = "Monday";
            break;

        case 2:
            dayName = "Tuesday";
            break;

        case 3:
            dayName = "Wednesday";
            break;

        case 4:
            dayName = "Thursday";
            break;

        default:
            dayName = "Invalid day";
            break;
    }

    return dayName;
}

console.log(getDayName(0))
console.log(getDayName(5))


/* ---------------------------------------- */

let age: number = 25;
switch (age) {
    case 18:
        console.log("Năm 1 ĐH");
        break;

    case 19:
        console.log("Năm 2 ĐH");
        break;


    case 24:
    case 25:
        console.log("Đã đi làm");
        break;
    default:
        console.log("Cà rởn");
        break;
}