// Q3. Sort a list of elements using Quick Sort.

let arr = [5, 3, 2, 6, 7, 1, 4, 8, 9, 0];

function quickSort(arr, startIdx, endIdx) {
  if (startIdx < 0) return;
  if (startIdx >= endIdx) return;

  let pivot = Math.floor((startIdx + endIdx) / 2);
  let pivotElement = arr[pivot];
  let count = 0;

  for (let i = startIdx; i <= endIdx; i++) {
    if (arr[i] <= pivotElement) count++;
  }

  [arr[pivot], arr[startIdx + count - 1]] = [
    arr[startIdx + count - 1],
    arr[pivot],
  ];

  pivot = startIdx + count - 1;

  let i = 0;
  let j = endIdx;

  while (i < pivot && j > pivot) {
    if (arr[i] > pivotElement && arr[j] <= pivotElement) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++;
      j--;
    } else if (arr[i] > pivotElement) j--;
    else if (arr[j] <= pivotElement) i++;
    else {
      i++;
      j--;
    }
  }

  quickSort(arr, startIdx, pivot - 1);
  quickSort(arr, pivot + 1, endIdx);
}

console.log("Before:", arr);
quickSort(arr, 0, arr.length - 1);
console.log("After (Quick Sort):", arr);
