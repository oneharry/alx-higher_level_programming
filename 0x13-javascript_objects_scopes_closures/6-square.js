#!/usr/bin/node
const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i;
    const size = this.height;
    if (c === 'undefined') {
      this.print();
    }
    for (i = 0; i < size; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
