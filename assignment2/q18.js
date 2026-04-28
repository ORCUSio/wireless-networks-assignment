// Q18. Convert uppercase letters to lowercase and lowercase to uppercase.

function switchCases(str) {
  let n = str.length;
  let ans = "";

  for (let i = 0; i < n; i++) {
    if (str[i].toLowerCase() === str[i]) {
      ans += str[i].toUpperCase();
    } else {
      ans += str[i].toLowerCase();
    }
  }

  return ans;
}

let s = "Server Side Programming Lab";

console.log("Original:", s);
console.log("Switched:", switchCases(s));
