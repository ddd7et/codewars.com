/*
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

function positiveSum(arr) {
  
}

Test.assertEquals(positiveSum([1,2,3,4,5]),15);
Test.assertEquals(positiveSum([1,-2,3,4,5]),13);
Test.assertEquals(positiveSum([]),0);
Test.assertEquals(positiveSum([-1,-2,-3,-4,-5]),0);
Test.assertEquals(positiveSum([-1,2,3,4,-5]),9);
*/

function positiveSum(arr) {
    return arr.reduce((a,x) => {if (x>0) a+=x; return a;}, 0 );
}

const arr = [5,3,1,-5];
//const arr = [1,2,3,4,5];
//const arr = [];
//const arr = [-1,-2,-3,-4,-5];
//const arr = [-1,2,3,4,-5]

console.log(  positiveSum(arr)     );