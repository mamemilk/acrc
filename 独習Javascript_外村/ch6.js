console.log("#### 6章")

function append_a (a, res = []){
    res.push(a)
    return res;
}

let a = append_a(1);
let b = append_a(2);
let c = append_a(3);

console.log(a,b,c, "pythonのようなresの評価は最初の一回だけ，ということはおきない")

const ans1 = '1:仮引数，2:実引数, 3:undefined, 4:こんにには，undefined'
console.log('[1] ', ans1)

const ans2 = '1:undefined 2:20, 3:undefined'
console.log('[2] ', ans2)

const ans3 = '1: undefined 2:undefined, 3:10, 4:"100"'
console.log('[3] ', ans3)

setTimeout(function(n){console.log(`こんにちは，${n}`)}, 2000, "おれ")
setTimeout(n => {console.log(`こんにちは，${n}`)}, 2000, "おれ")

function add(val1, val2){return val1+val2;}
function minus(val1, val2){return val1-val2;}

function calcAndDisp(op, disp, val1, val2){
    disp(op(val1,val2))
}

calcAndDisp(minus, console.log, 3,2);


let f1 = (num1, num2) => {return num1+num2};
console.log(f1(1,2))

let f2 = num => {return num*2}
console.log(f2(1));

let f3 = () => {console.log('Hello World')}
f3()

let f4 = name => {console.log("Hello World");console.log(`Hello ${name}!`)}
f4('おれ')

let f5 = () => {return {name:"独習太郎"}}
console.log(f5())