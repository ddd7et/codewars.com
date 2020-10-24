//https://www.codewars.com/kata/57e3f79c9cb119374600046b/train/javascript

//Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

//Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

//Examples:

//hello "john"   => "Hello, John!"
//hello "aliCE"  => "Hello, Alice!"
//hello          => "Hello, World!" # name not given
//hello ''       => "Hello, World!" # name is an empty String



function hello(name) {
    
  if (typeof name === 'undefined'){
      return "Hello, World!";
  }

    if (name.length<1){
      return "Hello, World!";
    }

    return "Hello, "+ name[0].toUpperCase() + name.substr(1,name.length).toLowerCase()+"!";
  }

//hello("hello");

//hello "john"   => "Hello, John!"
//hello "aliCE"  => "Hello, Alice!"
//hello          => "Hello, World!" # name not given
//hello ''       => "Hello, World!"

var name = "john";


console.log(
  hello(name)
);

/*
function hello(name){
  if (name){
    return "Hello, " + name.substring(0,1).toUpperCase() + name.substring(1).toLowerCase() + '!';
  } else {
    return "Hello, World!";
  }
}
*/