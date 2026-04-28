// Q17. Split a string and convert it into an array of words.

function getWordArray(s) {
  let arr = s.split(" ");
  return arr;
}

let s = "Today is sunday";

console.log("Original string:", s);
console.log("Word array:", getWordArray(s));
