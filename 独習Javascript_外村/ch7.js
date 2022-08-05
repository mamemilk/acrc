const HERE = `
         | トップレベル | 関数内 | ブロック内     | モジュール内のトップレベル
let      | スクリプト   | 関数   | ブロック      | モジュール
const    | ↑           | ↑     |  ↑            | ↑
var      | グローバル   | ↑     | ブロックの外側 | ↑
関数宣言  | ↑           | ↑     | ↑             |

`;

console.log(HERE)

ans2 = `
1: 関数内
2: 関数内
3: 関数内
4: 関数内
5: グローバル
6: グローバル
7: 関数内
`

{
    let val = "グローバル"
    function fn1(){
        let val = "関数内"
        if(Math.random() < .5){
            console.log(val)
            fn1();
        }

        function fn2(){
            console.log('3', val)
        }
        console.log('4', val)

        fn2();
        return val;
    }

    function fn3(){
        console.log('5', val);
    }
    console.log('6',val)

    const result = fn1();
    console.log('7', result);
    fn3();
}

function delayMessageFactory(disp_f, msec){
    function innerFn(message){
        setTimeout(disp_f, msec, message)
    }
    return innerFn
}

const log = delayMessageFactory(console.log, 1000);
log('konbanwa')


function delayMessageFactoryClosure(disp_f, msec){

    return message => {
        setTimeout(disp_f, msec, message)
    }
}
const log_c = delayMessageFactoryClosure(console.log, 1000);
log_c('closure')
