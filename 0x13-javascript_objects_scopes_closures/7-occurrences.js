#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce(
    (NumORepeat, curVal) =>
      curVal === searchElement ? NumORepeat + 1 : NumORepeat,
    0
  );
};
