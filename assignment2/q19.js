// Q19. Return the number of minutes expressed in hours and minutes.

function timeConvert(minutes) {
  let hrs = Math.floor(minutes / 60);
  let mins = minutes % 60;

  let hr = `${hrs} hour${hrs > 1 ? "s" : ""}`;
  let min = `${mins} minute${mins > 1 ? "s" : ""}`;

  if (hrs === 0) return min;
  else if (mins === 0) return hr;
  else return hr + " " + min;
}

console.log("60 minutes  =>", timeConvert(60));
console.log("90 minutes  =>", timeConvert(90));
console.log("135 minutes =>", timeConvert(135));
console.log("45 minutes  =>", timeConvert(45));
