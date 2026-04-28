// Q22. Rectangle class with area and perimeter methods.

class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  area() {
    return this.width * this.height;
  }

  perimeter() {
    return 2 * (this.width + this.height);
  }
}

let rect = new Rectangle(10, 5);

console.log("Width:", rect.width, "| Height:", rect.height);
console.log("Area:", rect.area());
console.log("Perimeter:", rect.perimeter());
