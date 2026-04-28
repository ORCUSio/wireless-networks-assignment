// Q23. Slideshow logic — next/prev navigation through an image list.
// (In a browser context this would update an <img> element's src attribute.)

let images = [
  "./img1.jfif",
  "./img2.jfif",
  "./img3.jfif",
  "./img4.jfif",
  "./img5.jfif",
];

let index = 0;

function showImage() {
  // In browser: document.getElementById("slide").src = images[index];
  console.log("Current image:", images[index]);
}

function next() {
  index = (index + 1) % images.length;
  showImage();
}

function prev() {
  index = (index - 1 + images.length) % images.length;
  showImage();
}

// Demo: simulate slideshow navigation
showImage();
next();
next();
prev();
