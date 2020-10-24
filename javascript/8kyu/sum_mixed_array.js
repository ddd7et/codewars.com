//https://www.codewars.com/kata/sum-mixed-array/train/javascript
// Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
//Return your answer as a number.

function sumMix(x){
  var i, sum=0;
  for (i=0; i < x.length; i++){
    sum += Number(x[i]);
  }
  return sum
}

/*
function sumMix(x){
  return x.map(a => +a).reduce((a, b) => a + b);
}
*/