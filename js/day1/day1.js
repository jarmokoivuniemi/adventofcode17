
function captcha1(input) {
  const arr = intArray(input);
  return  arr.reduce((res, x, i) => res + (x === arr[(i+1) % arr.length] ? x : 0), 0);
};

function intArray(input) {
  return input.split('').map(x => parseInt(x));
};

module.exports = captcha1
