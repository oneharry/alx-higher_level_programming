#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((x, y) => {
    if (y === searchElement) {
      return x + 1;
    } else {
      return x;
    }
  }, 0);
};
