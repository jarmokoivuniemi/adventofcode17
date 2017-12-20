
function captcha1(input) {
  const arr = intArray(input);
  const isNextDigitMatch = (x, i) => x === arr[(i+1) % arr.length];
  const digitsMatchingNextDigit = (sum, x, i) => sum + (isNextDigitMatch(x, i) ? x : 0)

  return  arr.reduce(digitsMatchingNextDigit, 0);
};

function captcha2(input) {
  const arr = intArray(input);
  const half = arr.length/2;
  const matchesHalfwayAround = (x, i) => x === arr[(i+half) % arr.length];
  const digitsMatchingHalfwayAround = (sum, x, i) => sum + (matchesHalfwayAround(x, i) ? x : 0)

  return  arr.reduce(digitsMatchingHalfwayAround, 0);
};

function intArray(input) {
  return input.split('').map(x => parseInt(x));
};


module.exports.captcha1 = captcha1
module.exports.captcha2 = captcha2
