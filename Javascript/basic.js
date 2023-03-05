// khai báo biến

// var khai báo có phạm vi toàn cầu hoặc chức năng có phạm vi trong khi let và const có phạm vi khối.
// var các biến có thể được cập nhật và khai báo lại trong phạm vi của nó;
// let các biến có thể được cập nhật nhưng không được khai báo lại;
// const các biến không thể được cập nhật hoặc khai báo lại.
// Tất cả chúng đều được nâng lên đầu phạm vi của chúng.
// Nhưng trong khi var các biến được khởi tạo bằng undefined và các biến let không const được khởi tạo.
// Khi var và let có thể được khai báo mà không được khởi tạo, nhưng const phải được khởi tạo trong quá trình khai báo.

function myFunction() {
  var x = 1;
  if (true) {
    var x = 2;  // x được ghi đè
    console.log(x);  // 2
  }

  let y = 1;
  if (true) {
    let y = 2;  // y được ghi đè
    console.log(y);  // 2
  }

  const const1 = 1;
  // const1 = 2; // lỗi
  // const const2; // lỗi
}