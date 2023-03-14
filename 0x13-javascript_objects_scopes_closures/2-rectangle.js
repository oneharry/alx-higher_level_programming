#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.height = h;
      this.width = w;
    }
    return this;
  }
}
module.exports = Rectangle;
