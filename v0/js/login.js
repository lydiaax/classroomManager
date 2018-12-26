var app = new Vue({
    el:'#app',
    data:{
        username:'',
        password:'',
        info:{
            grade:11,
            id:1111,
            major:'',
            pinyin:'',
            student_id:'',
            student_name:''
        }
    },
    methods:{
        login:function(){
            console.log('login'+this.username+this.password)
            
            axios.get('http://127.0.0.1:5000/main/tb_student',
            {
                params:{
                    student_id:this.username
                }
            }).then((response)=>{
                var data = response.data[0];
                console.log(data)
                this.info.grade = data.grade;
                this.info.id = data.id;
                this.info.major = data.major;
                this.info.pinyin = data.pinyin;
                this.info.student_id = data.student_id;
                this.info.student_name = data.student_name;
                console.log(this.info)
                if(this.info.pinyin == this.password){
                    alert('登陆成功');
                    window.location.href="index.html" 
                }else{
                    alert('登陆失败');
                }
            }).catch((response)=>{
                console.log(response);
            })
        }
    }
})