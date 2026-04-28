// Q4. Sort a list of elements using Merge Sort.

function merge(arr1, arr2) {
  let i = 0;
  let j = 0;
  let ans = [];

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] <= arr2[j]) ans.push(arr1[i++]);
    else ans.push(arr2[j++]);
  }

  while (i < arr1.length) ans.push(arr1[i++]);
  while (j < arr2.length) ans.push(arr2[j++]);

  return ans;
}

function mergeSort(arr) {
  if (arr.length <= 1) return arr;

  let mid = Math.floor(arr.length / 2) - 1;
  let left = [],
    right = [];

  for (let i = 0; i <= mid; i++) left.push(arr[i]);
  for (let i = mid + 1; i < arr.length; i++) right.push(arr[i]);

  left = mergeSort(left);
  right = mergeSort(right);

  return merge(left, right);
}

let arr = [45, 3, 2, 6, 4, 21, 6, 8, 4, 2, 0];

console.log("Before:", arr);
arr = mergeSort(arr);
console.log("After (Merge Sort):", arr);
