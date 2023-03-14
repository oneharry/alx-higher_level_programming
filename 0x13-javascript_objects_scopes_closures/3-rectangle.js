#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const h = this.height;
    const w = this.width;
    let i;
    for (i = 0; i < h; i++) {
      console.log('X'.repeat(w));
    }
  }
}
module.exports = Rectangle;
