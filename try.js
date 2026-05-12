let globalVar="I am global";

function test(){
    let localVar="I am local";
    console.log(globalVar);
    console.log(localVar);
}
test();

console.log(globalVar);
//console.log(localVar);

let name="Global";

function showName(){
    console.log(name);
}
function test(){
    let name="Local";
    showName();
}

test();

//this will print gloabal as this is in global scope 
// not local
function outer() {
    let count = 0;

    function inner() {
        count++;
        console.log(count);
    }

    return inner;
}

const fn = outer();

fn(); // 1
fn(); // 2
fn(); // 3