// Q20. Implement a Stack that checks if a given element is present or not.

class Stack {
  constructor() {
    this.items = [];
  }

  push(element) {
    this.items.push(element);
  }

  pop() {
    if (this.isEmpty()) {
      return "Stack is empty";
    }
    return this.items.pop();
  }

  peek() {
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  contains(x) {
    return this.items.includes(x);
  }
}

const st = new Stack();
st.push(10);
st.push(20);
st.push(30);

console.log("Stack items:", st.items);
console.log("Contains 20:", st.contains(20));
console.log("Contains 50:", st.contains(50));
