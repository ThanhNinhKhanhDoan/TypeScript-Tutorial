//Enum cơ bản
enum Direction {
    Up,
    Down,
    Left,
    Right
}

let move: Direction = Direction.Left;
console.log(">>>check ", move);



// Enum với giá trị khởi tạo tùy chỉnh
enum StatusCode {
    Success = 202,
    NotFound = 404,
    SeverError = 500
}

let status1: StatusCode = StatusCode.NotFound;
console.log(">>>check ", status1);




// Enum với giá trị chuỗi
enum Colors {
    red = "Red",
    yellow = "Yellow",
    blue = "Blue"
}

let color: Colors = Colors.yellow;
console.log(">>>check ", color);




// ----------------------------//

// Truy cập vào tên từ giá trị
enum Directions {
    Up,
    Down,
    Left,
    Right
}

let direction: string = Directions[3]
console.log(">>>check ", direction);




// Kiểm tra giá trị của Enum
enum Responses {
    No = 0,
    Yes = 1
}

function respond(recipient: string, message: Responses): void {
    console.log(`${recipient}: ${message === Responses.Yes ? "Yes" : "No"}`);
}

respond("NTN", Responses.No)