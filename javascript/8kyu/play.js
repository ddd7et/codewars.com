str = "hEllo Bay sort uLiana Here";

console.log(str);


//new_str = str.split(" ").map(w => w[0].toLocaleUpperCase()+w.slice(1)   ).join(' ')  

new_str = str.split(" ").map(f).join(" ")

function f(currentValue, index, arr){

    if (index % 2 == 0){
        console.log(arr)
        return currentValue.toLocaleUpperCase()
    }
    
    else{
        return currentValue.toLocaleLowerCase() 
    }
}


console.log(new_str)

let i = 11;

console.log(i % 2);