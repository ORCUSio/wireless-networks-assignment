// Q12. Validate whether a given value is a RegExp or not.

function checkRegEx(s) {
  return Object.prototype.toString.call(s) === "[object RegExp]";
}

let s = /aba/;
let t = "hello";

console.log(`/aba/ is RegExp:`, checkRegEx(s));
console.log(`"hello" is RegExp:`, checkRegEx(t));
