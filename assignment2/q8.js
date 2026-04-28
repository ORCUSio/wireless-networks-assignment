// Q8. Sort the characters in a string alphabetically.

function sortStr(s) {
  let arr = s.split("");
  arr = arr.sort();
  let ans = arr.join("");
  return ans;
}

let s = "fjsalkdfja";

console.log("Original string:", s);
s = sortStr(s);
console.log("Sorted string:", s);
