// Q21. Check whether a singly linked list is empty or not.

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  isEmpty() {
    return this.head === null;
  }

  add(data) {
    const node = new Node(data);
    if (!this.head) {
      this.head = node;
    } else {
      let current = this.head;
      while (current.next) current = current.next;
      current.next = node;
    }
  }
}

let emptyList = new LinkedList();
console.log("Empty list - isEmpty:", emptyList.isEmpty()); // true

let populatedList = new LinkedList();
populatedList.add(1);
populatedList.add(2);
console.log("Populated list - isEmpty:", populatedList.isEmpty()); // false
