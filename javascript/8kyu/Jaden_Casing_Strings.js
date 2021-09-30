String.prototype.toJadenCase = function () {
  
    console.log(this);
    let str = this;
    let new_string = "";
  
    new_string += str[0].toLocaleUpperCase();
  
    for (let i=1; i<str.length; i++) {
      if (str[i-1] == " "){
          new_string += str[i].toLocaleUpperCase()
      }
      else {
          new_string += str[i]
      }
    }
  
    return new_string;
    
};

