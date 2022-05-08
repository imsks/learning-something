// function foo(a: number, b: number) {
//     return a + b
// }
// const result = foo(2, 5)
// console.log(result)
var User = /** @class */ (function () {
    function User(name) {
        this.name = name;
    }
    return User;
}());
var user = new User("Sachin");
var user2 = new User("Sachin 2");
console.log(user);
console.log(user2);
