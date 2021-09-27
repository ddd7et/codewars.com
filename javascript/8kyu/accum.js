//https://www.codewars.com/kata/5667e8f4e3f572a8f2000039 
//This time no story, no theory. The examples below show you how to write function accum:

//Examples:

//accum("abcd") -> "A-Bb-Ccc-Dddd"
//accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
//accum("cwAt") -> "C-Ww-Aaa-Tttt"

//The parameter of accum is a string which includes only letters from a..z and A..Z.


function accum(str) {

    new_str = "";

    for (i=0;i<str.length;i++){
        new_str += str[i].toUpperCase() + str[i].repeat(i).toLowerCase() +"-";
    }
    return new_str.slice(0, new_str.length-1);

}

var str = "RqaEzty";
//var new_string = accum(str);

//console.log(new_string);


console.log(str);
str = str.split("")
console.log(str);

new_str = str.map((x,i) => x[0].toUpperCase()+x.repeat(i).toLowerCase()+"-");

console.log("new_string=", new_str);

new_str2 = str.reduce((a,x) => {

    //a+=x[0]+x.repeat(1)+"-";
    a.push(x)+"-";
    return a;
    }, {} );
    //return а ; } , { } ) ;

console.log(new_str2);