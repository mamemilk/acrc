// 5章目からnode.jsで練習問題をやる．

console.log('#### 練習問題5.5')

let greeting = "greetingの値"

//if(greeting instanceof String){
if(typeof greeting == 'string'){
        console.log(`{greeting}, いい天気ですね．`)
}

greeting = 1

if(typeof greeting == 'string'){
    console.log(`{greeting}, いい天気ですね．これは表示されない`)
}

try{
    if(typeof greeting != 'string'){
        throw TypeError
    }
}catch{
    console.log('不正なデータです')
}finally{
    console.log('finally called')
}

greeting = '1'

try{
    if(typeof greeting != 'string'){
        throw TypeError
    }
}catch{
    console.log('不正なデータです')
}finally{
    console.log('finally called')
}


console.log('#### 練習問題5.10')
let a = [1,2,3]//{a:1, b:2}
const PropDesc = Reflect.getOwnPropertyDescriptor(a, "length");
console.log('enumerable ? : ', PropDesc)


console.log('#### 練習問題5.11')
const arry = [10, "文字", 20, true, 23, 47]

let sum = 0;
for(const ele of arry){
    if(typeof ele == 'number'){
        sum += ele
    }
}
console.log(sum)


console.log('#### 練習問題5.12')
const obj512 = {
    prop1 : 10,
    prop2 : "moji",
    prop3 : 20,
    skip : 20,
    prop4 : true,
    prop5 : 23, 
    prop6 : 47
}
let sum0 = 0;
for(const ele in obj512){
    if(ele != 'skip' && typeof obj512[ele] == 'number'){
        sum0 += obj512[ele]
    }
}
console.log(sum0)


console.log('#### 理解度チェック')

for(let i=5; i<10; i++){
    console.log(i);
}

for(let i=1; i<=100; i++){
    if(i%3==0 && i%5==0){
        console.log('Fizz Buss')
    }else if(i%3==0){
        console.log('Fizz')
    }else if(i%5==0){
        console.log('Buzz')
    }else{
        console.log(i)
    }

}

const ans53 = '1:列挙可能, 2:プロパティ記述子, 3:enumerable'
console.log(ans53)

const capitals = {
    日本: "東京", 
    アメリカ: "ワシントン", 
    イギリス: "ロンドン"
}

for(const ele of Object.keys(capitals)){
    console.log(`${ele}の首都は${capitals[ele]}です`)
}
for(const [key, value] of Object.entries(capitals)){
    console.log(`${key}の首都は${value}です`)
}

console.log('5は，throwの直後の出力だけされず，あとはすべて出力される．')

