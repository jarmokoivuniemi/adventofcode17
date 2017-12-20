var captcha1 = require('./day1.js').captcha1;
var captcha2 = require('./day1.js').captcha2;
var fs = require('fs');
var path = require('path');
var filePath = path.join(__dirname, 'puzzle.txt');

describe('Day 1, part 1', function() {
  it('returns zero when given zero', function() {
    expect(captcha1('0')).toBe(0);
  });

  it('returns sum of two numbers when given two same numbers', function() {
    expect(captcha1('11')).toBe(2);
  });

  it('returns sum of three numbers when given three same numbers', function() {
    expect(captcha1('111')).toBe(3);
  });

  it('returns sum two numbers when each number has matching number next to it', function() {
    expect(captcha1('1122')).toBe(3);
  });

  it('wraps around and checks if last and first numbers match', function() {
    expect(captcha1('12211')).toBe(4);
  });

  it('works', function() {
    var input = fs.readFileSync(filePath).toString().trim();
    expect(captcha1(input)).toBe(1228);
  });

});

describe('Day 1, part 2', function() {
  it('returns sum of all numbers when all numbers are the same', function() {
    expect(captcha2('1111')).toBe(4);
  });

  it('returns sum of all numbers when each number has a match halfway across', function() {
    expect(captcha2('1212')).toBe(6);
  });

  it('returns zero when none of the numbers has a match halfway across', function() {
    expect(captcha2('1221')).toBe(0);
  });
  
  it('works', function() {
    var input = fs.readFileSync(filePath).toString().trim();
    expect(captcha2(input)).toBe(1238);
  });
});
