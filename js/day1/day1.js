
function captcha1(input) {
  const arr = intArray(input);
  return  arr.reduce((res, x, i) => res + (x === arr[(i+1) % arr.length] ? x : 0), 0);
};

function intArray(input) {
  return input.split('').map(x => parseInt(x));
};

function captcha2(input) {
  const arr = intArray(input);
  const half = arr.length/2
  return  arr.reduce((res, x, i) => res + (x === arr[(i+half) % arr.length] ? x : 0), 0);
};

module.exports.captcha1 = captcha1
module.exports.captcha2 = captcha2
