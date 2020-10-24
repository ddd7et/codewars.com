//https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/javascript

//Write a function called repeat_str which repeats the given string src exactly count times.

//repeatStr(6, "I") // "IIIIII"
//repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

//describe("Tests", function() {
//    it ("Basic tests", function() {
//      Test.assertSimilar(repeatStr(3, "*"), "***");
//      Test.assertSimilar(repeatStr(5, "#"), "#####");
//      Test.assertSimilar(repeatStr(2, "ha "), "ha ha ");
//    });
//  });


function repeatStr (n, s) {
    new_string = ""
    for (i=0;i<n;i++){
        new_string += s;
    };
    return new_string;
    
}

console.log(repeatStr(1, '*'));

/*
function repeatStr (n, s) {
    return s.repeat(n);
  }
*/

