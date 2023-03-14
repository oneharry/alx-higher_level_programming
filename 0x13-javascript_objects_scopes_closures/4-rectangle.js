#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    const h = this.height;
    const w = this.width;
    let i, j;
    for (i = 0; i < h; i++) {
      let space = '';
      for (j = 0; j < w; j++) {
        space += 'X';
      }
      console.log(space);
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
}
module.exports = Rectangle;
