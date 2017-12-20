
function captcha1(input) {
  const numbers = intArray(input);
  const isNextDigitMatch = (x, i) => x === numbers[(i+1) % numbers.length];
  const digitsMatchingNextDigit = (sum, x, i) => sum + (isNextDigitMatch(x, i) ? x : 0)

  return  numbers.reduce(digitsMatchingNextDigit, 0);
};

function captcha2(input) {
  const numbers = intArray(input);
  const half = numbers.length/2;
  const matchesHalfwayAround = (x, i) => x === numbers[(i+half) % numbers.length];
  const digitsMatchingHalfwayAround = (sum, x, i) => sum + (matchesHalfwayAround(x, i) ? x : 0)

  return  numbers.reduce(digitsMatchingHalfwayAround, 0);
};

function intArray(input) {
  return input.split('').map(x => parseInt(x));
};


module.exports.captcha1 = captcha1
module.exports.captcha2 = captcha2
