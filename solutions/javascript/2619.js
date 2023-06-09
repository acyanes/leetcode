Array.prototype.last = function () {
  let s = this.length;
  if (s == 0) {
    return -1;
  }
  return this[s - 1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
