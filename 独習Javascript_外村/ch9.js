class User{
    constructor(arg){
        this.username = arg
        this.deleted = 0
    }

    login(){
        if(this.deleted == 0){
            console.log(`${this.username}はログインに成功しました．`)
        }else{
            console.log(`${this.username}はログインに失敗しました．`)
        }
    }
}

class AdminUser extends User{
    constructor(arg){
        super(arg)
    }
    deleteUser(obj){
        
        if(obj instanceof User){
            
        }else{
            console.log('Userオブジェクトを引数にする必要があります．')
            throw TypeError;        
        }
        
        obj.deleted = 1
        console.log(`${obj.username}を削除しました．`)
    }
}

a = new User('a')
b = new User('b')
c = new User('c')
X = new AdminUser('X')

X.deleteUser(b)
a.login()
b.login()
c.login()

X.deleteUser(1)