// Q25. Redirect to a specified URL.
// (In a browser context this uses window.location.href.)

function redirect(url) {
  // In browser: window.location.href = url;
  console.log("Redirecting to:", url);
}

redirect("https://www.google.com");
