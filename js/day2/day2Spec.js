var difference = require('./day2.js').difference;
var differenceChecksum = require('./day2.js').differenceChecksum;

var divideEvenlyDivisible = require('./day2.js').divideEvenlyDivisible;
var divisionChecksum = require('./day2.js').divisionChecksum;

var fs = require('fs');
var path = require('path');
var filePath = path.join(__dirname, 'puzzle.txt');


describe('Day 2, part 1', function() {
  it('calculates difference between largest and smallest value', function() {
    expect(difference('5\t1\t9\t5')).toBe(8);
  });

  it('calculates checksum for three rows', function() {
    let input = fs.readFileSync(filePath).toString().trim();
    expect(differenceChecksum(input)).toBe(53460);
  });

});

describe('Day 2, part 2', function() {
  it('divides numbers that are evenly divisible', function() {
    expect(divideEvenlyDivisible('5\t9\t2\t8')).toBe(4);
  });

  it('works', function() {
    let input = fs.readFileSync(filePath).toString().trim();
    expect(divisionChecksum(input)).toBe(282);
  });
});
