
var app = new Vue({
    el:'#app',
    data:{
        username:'',
        password:'',
        STUinfo:{
            grade:11,
            id:1111,
            major:'',
            pinyin:'',
            student_id:'',
            student_name:''
        },
        THinfo:{
            email:'',
            id:1,
            teacher:''
        }
    },
    methods:{
        First:function(){
            //判断学生、老师、管理员
            if(this.username.indexOf('@') != -1){
                //老师
                this.loginTH();
            }else{
                this.loginSTU();
            }
        },
        loginSTU:function(){
            axios.get('http://127.0.0.1:5000/main/tb_student',
            {
                params:{
                    student_id:this.username
                }
            }).then((response)=>{
                var data = response.data[0];
                console.log(data)
                this.STUinfo.grade = data.grade;
                this.STUinfo.id = data.id;
                this.STUinfo.major = data.major;
                this.STUinfo.pinyin = data.pinyin;
                this.STUinfo.student_id = data.student_id;
                this.STUinfo.student_name = data.student_name;
                if(this.STUinfo.pinyin == this.password){
                    alert('登陆成功');
                    //TODO,修改页面
                    window.location.href="ADindex.html?id="+this.STUinfo.id;
                }else{
                    alert('登陆失败');
                }
            }).catch((response)=>{
                console.log(response);
            })
        },
        loginTH:function(){
            //需要加字段
            axios.get('http://127.0.0.1:5000/main/tb_teacher',
            {
                params:{
                    email:this.username
                }
            }).then((response)=>{
                var data = response.data[0];
                console.log(data)
                this.THinfo.email = data.email;
                this.THinfo.id = data.id;
                this.THinfo.teacher = data.teacher;
                // if(this.info.pinyin == this.password){
                //     alert('登陆成功');
                //     window.location.href="index.html" 
                // }else{
                //     alert('登陆失败');
                // }
                alert('缺少字段');
            }).catch((response)=>{
                console.log(response);
            })
        }
    }
})