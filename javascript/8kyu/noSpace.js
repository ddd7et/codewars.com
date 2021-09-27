//https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/javascript

//Simple, remove the spaces from the string, then return the resultant string.

//Test.describe("Example tests",_=>{
//Test.assertEquals(noSpace('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB');
//Test.assertEquals(noSpace('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd'); 
//Test.assertEquals(noSpace('8aaaaa dddd r     '), '8aaaaaddddr'); 
//});

function noSpace(x){
    new_string = "";
    for (i=0;i<x.length;i++){
        if (x[i] !== " ")
            new_string += x[i];
    };

    return new_string;
}

x = '8aaaaa dddd r     ';

console.log(noSpace(x));

/*
function noSpace(x){
  return x.replace(/\s/g, '');
}
*/