const sum = (acc, x) => acc + x 

function captcha1(input) {
  const numbers = intArray(input);
  const isNextDigitMatch = (x, i) => x === numbers[(i+1) % numbers.length];
  const digitsMatchingNextDigit = (x, i) => isNextDigitMatch(x, i) ? x: 0

  return numbers
    .map(digitsMatchingNextDigit)
    .reduce(sum);
};

function captcha2(input) {
  const numbers = intArray(input);
  const half = numbers.length/2;
  const matchesHalfwayAround = (x, i) => x === numbers[(i+half) % numbers.length];
  const digitsMatchingHalfwayAround = (x, i) => matchesHalfwayAround(x, i) ? x : 0;

  return numbers
    .map(digitsMatchingHalfwayAround)
    .reduce(sum);
};

function intArray(input) {
  return input.split('').map(x => parseInt(x));
};


module.exports.captcha1 = captcha1
module.exports.captcha2 = captcha2
