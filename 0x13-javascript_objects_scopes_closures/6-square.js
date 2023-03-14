#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let cha = 'X';
    let i, j;
    const size = this.height;
    if (c) {
      cha = c;
    }
    for (i = 0; i < size; i++) {
      let space = '';
      for (j = 0; j < size; j++) {
        space += cha;
      }
      console.log(space);
    }
  }
}
module.exports = Square;
