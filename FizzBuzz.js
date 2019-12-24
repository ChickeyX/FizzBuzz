for (i = 1; i <= 100; i++) {              // Increment 'x' by 1 in each repeat (up to 100)
  string = "";                            // Reset 'string'
  if (i % 3 == 0) {string += "Fizz"}      // If 'i' is divisible by 3 then add "Fizz" to 'string'
  if (i % 5 == 0) {string += "Buzz"}      // If 'i' is divisible by 5 then add "Buzz" to 'string'
  console.log(string || i)                // If 'string' is empty, print 'i'. Otherwise, print 'string'
}
