var app = new Vue({
    el:'#app',
    data:{
        result:[],
        waitinfo:[],
        passinfo:[]
    },
    created:function(){
        axios.get('http://127.0.0.1:5000/main/tb_reservation',{
            params:{
                status:0
            }
        })
        .then((response)=>{
            var data = response.data;
            if(data != null && data.length != 0) {
                this.result = data;
                for(var i=0;i<this.result.length;i++){
                    this.result[i].submit_date = this.result[i].submit_date.split(" ")[0];
                    console.log("外部:"+i)
                    //查找教室
                    axios.get('http://127.0.0.1:5000/main/tb_class',{
                        params:{
                            id: this.result[i].class_id
                        }
                    })
                    .then((response)=>{
                        console.log("res:"+i)
                        var data = response.data[0];
                        console.log(data)
                        if(data != null) {
                            this.$set(this.result[i],"className",data.class_room);
                            console.log(this.result[i].className)
                            
                        }
                    }).catch((response)=>{
                        console.log(response);
                    })
                }
                for(var i=0;i<this.result.length;i++){
                    //查找学生
                    axios.get('http://127.0.0.1:5000/main/tb_student',{
                        params:{
                            id: this.result[i].user_id
                        }
                    })
                    .then((response)=>{
                        
                        var data = response.data[0];
                        console.log(data)
                        if(data != null) {
                            this.$set(this.result[i],"stuName",data.student_name);
                            console.log(this.result[i].stuName)
                        }
                    }).catch((response)=>{
                        console.log(response);
                    })
                }
            }
            
        }).catch((response)=>{
            console.log(response);
        })
        
        
    },
    // updated:function() {
    //     console.log("beforeUpdate")
    //     while(1){
    //         if(this.result.length!=0){
    //             for(var i=0;i<this.result.length;i++){
    //                 if(this.result[i].status==0){
    //                     this.waitinfo.push(result[i]);
    //                 }else{
    //                     this.passinfo.push(result[i]);
    //                 }
    //             }
    //             this.result = this.waitinfo;
    //             break;
    //         }      
    //     }
    // },
    methods:{
        pass:function(id){
            let obj = {'id':id}
            axios.post('http://127.0.0.1:5000/main/tb_reservation',{
                    filter: JSON.stringify(obj),
                    update: JSON.stringify({'status':'1'}),
                })
                .then((response)=>{
                    alert('已通过');
                    console.log(response);
                    for(var i=0;i<this.result.length;i++){
                        if(this.result[i].id==id){
                            console.log("delete")
                            this.result.splice(i,1);
                            break;
                            
                        }
                            
                        
                    }
                }).catch((response)=>{
                    console.log(response);
                })
        },
        reject:function(id){
            let obj = {'id':id}
            axios.post('http://127.0.0.1:5000/main/tb_reservation',{
                    filter: JSON.stringify(obj),
                    update: JSON.stringify({'status':'2'}),
                })
                .then((response)=>{
                    alert('已拒绝');
                    console.log(response);
                }).catch((response)=>{
                    console.log(response);
                })
        }
    }
})

$(document).ready(function(){
    $(".label label-success").click(function(event){
      event.stopPropagation();
      alert("提交.");
    });
  });