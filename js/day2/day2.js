const sum = (acc, x) => acc + x 
const min = (x, y) => (x < y) ? x : y;
const max = (x, y) => (x > y) ? x : y;


function differenceChecksum(input) {
  return input
    .split("\n")
    .map(x => difference(x))
    .reduce(sum)
};

function difference(input) {
  let numbers = input.split('\t').map(x => parseInt(x));
  return numbers.reduce(max) - numbers.reduce(min)
};

function divisionChecksum(input) {
  return input
    .split("\n")
    .map(x => divideEvenlyDivisible(x))
    .reduce(sum)
};

function divideEvenlyDivisible(input) {
  return input
    .split('\t')
    .map(x => parseInt(x))
    .filter((x, _, numbers) => hasDivisible(x, numbers))
    .reduce((x, y) => max(x, y) / min(x, y))
};

function hasDivisible(x, numbers) {
  return numbers
    .filter(n => x !== n)
    .filter(n => max(x, n) % min(x, n) == 0)
    .length != 0;
};

module.exports.difference = difference
module.exports.differenceChecksum = differenceChecksum
module.exports.divideEvenlyDivisible = divideEvenlyDivisible
module.exports.divisionChecksum = divisionChecksum
