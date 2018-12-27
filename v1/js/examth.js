
var countTime = new Vue({
    el:'#timePicker',
    data:{
      result:null,
      examTime:null,
      num:30,
      priority:1,
      chooseClassID:null,
      options:[
        {value:1,label:'高'},
        {value:2,label:'较高'},
        {value:3,label:'中'},
        {value:4,label:'较低'},
        {value:5,label:'低'}
      ],
      classData:[
        {classID:1,name:'计算方法'},
        {classID:2,name:'数据挖掘'}
      ],
      sec:[],
      secList:[1,2,3,4,5,6,7,8,0,'A','B','C'],
    },
    methods:{
      summit:function(){
        if(new Date(this.examTime)<new Date()){
          //拒绝申请
          alert("请重新选择时间")
          return;
        }
       
        var arr2 = this.sec.sort(function(a,b){
         if (a>b) {
                       return 1;
                  }else if(a<b){
                      return -1
                  }else{
                      return 0;
                 }    
              });

        var day = new Date(this.examTime).getDay();
        var a = new Array("sub", "mon", "tues", "wed", "thur", "fri", "sat");  
        console.log(day)
        axios.get('http://127.0.0.1:5000/main/tb_classroom_table',{
              params:{
                  mode:'1',
                  day:a[day],
                  time:arr2.join(""),
                  number:this.num
              }
        })
        .then((response)=>{
            var data = response.data;
            console.log(data)
            this.result = data;
         }).catch((response)=>{
            console.log(response);
          })
        
      },
      apply:function(classroomId){
        var day = new Date(this.examTime);
            day = day.getFullYear()+'-'+(day.getMonth()+1)+'-'+(day.getDate())
            day1 = new Date();
            day1 = day1.getFullYear()+'-'+(day1.getMonth()+1)+'-'+(day1.getDate())
            console.log(day)
        

        var arr2 = this.sec.sort(function(a,b){
          if (a>b) {
                        return 1;
                   }else if(a<b){
                       return -1
                   }else{
                       return 0;
                  }    
               });
        //找教室ID
        axios.get('http://127.0.0.1:5000/main/tb_class',{
              params:{
                  class_room:classroomId
              }
        })
        .then((response)=>{
            var data = response.data[0];
            console.log(data)
            var classroomID = data.id;
            
            axios.put('http://127.0.0.1:5000/main/tb_reservation',{
                class_id:classroomID,
                user_id:5912,
                submit_date:day1,
                jieshu:day+' '+arr2.join(""),
                reason:'考试课室申请',
                status:0
            }).then((res)=>{
              console.log(res)
            }).catch((res)=>{
              console.log(res)
            })
         }).catch((response)=>{
            console.log(response);
          })
      }
    }
  })

 