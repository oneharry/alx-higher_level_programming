#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  let i = 0;
  for (i = 0; i < x; i++) {
    func();
  }
};
