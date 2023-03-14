#!/usr/bin/node
class Square extends require('./5-square.js') {
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
