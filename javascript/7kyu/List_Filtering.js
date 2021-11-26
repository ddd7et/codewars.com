let l = [1,2,'aasf','1','123',123]
let names = ["marge", "homer", "bart", "lisa", "maggie"]

//console.log(l)

let newNames = [];

for (let i=0; i<names.length; i++) {
    let name = names[i];
    let firstLetter = name.charAt(0).toUpperCase();
    newNames.push(firstLetter + name.slice(1)); 
}

console.log(newNames);

