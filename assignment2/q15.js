// Q15. Create a clock that prints the current time every second.

function startClock() {
  function updateTime() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, "0");
    const minutes = String(now.getMinutes()).padStart(2, "0");
    const seconds = String(now.getSeconds()).padStart(2, "0");
    console.log(`${hours}:${minutes}:${seconds}`);
  }

  updateTime();
  setInterval(updateTime, 1000);
}

startClock();
