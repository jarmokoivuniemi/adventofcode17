var captcha1 = require('./day1.js');

describe('Day 1', function() {
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
    
  });

});
