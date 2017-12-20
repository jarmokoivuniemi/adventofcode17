function difference(input) {
  const numbers = input.split(' ').map(x => parseInt(x));
  const min = numbers.reduce((a, b) => a < b ? a:b)
  const max = numbers.reduce((a, b) => a > b ? a: b)
  return max - min
};

describe('Day 2, part 1', function() {
  it('finds difference between largest and smallest value', function() {
    expect(difference('5 1 9 5')).toBe(8);
  });
});
