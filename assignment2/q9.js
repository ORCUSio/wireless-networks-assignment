// Q9. Check if a numeric array is sorted or not.

let arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

let flag = true;

for (let i = 0; i < arr.length - 1; i++) {
  if (arr[i] > arr[i + 1]) {
    flag = false;
    break;
  }
}

console.log("Array:", arr);
console.log("Is sorted:", flag);
