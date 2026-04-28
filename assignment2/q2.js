// Q2. Find the first index of a given element using linear search.

let arr = [3, 2, 2, 12, 4, 5, 2, 65, 7, 5, 3];
let target = 2;

console.log("Array:", arr);
console.log("Searching for:", target);

for (let i = 0; i < arr.length; i++) {
  if (arr[i] == target) {
    console.log("First index of", target, ":", i);
    break;
  }
}
