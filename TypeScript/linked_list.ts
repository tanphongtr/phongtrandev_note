// linked list in TypeScript
class _Node {
  data: any;
  next: Node | null;

  constructor(data: any) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  head: _Node | null;
  constructor() {
    this.head = null;
  }

  insertFirst(item: number) {
    this.head = new _Node(item);
  }
}

const SLL = new LinkedList();
SLL.insertFirst(1);
SLL.insertFirst(2);
SLL.insertFirst(3);
console.log(SLL);