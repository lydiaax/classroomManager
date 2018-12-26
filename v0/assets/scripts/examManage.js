
var countTime = new Vue({
    el:'#setPro',
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
      UnitData:[
        {ID:1,name:'工学院'},
        {ID:2,name:'社科部'}
      ],
    },
    methods:{
      summit:function(){
        this.result = [{
          classroomId:4201,
          name:'D201',
          allowExamPeo:30,
          Peo:60
        },{
          classroomId:4202,
          name:'D202',
          allowExamPeo:35,
          Peo:70
        },{
          classroomId:7301,
          name:'G301',
          allowExamPeo:30,
          Peo:60
        }];
      },
      apply:function(classroomId){
        console.log(typeof(classroomId))
        str = String(classroomId);
        str += ' ';
        str += this.examTime;
        alert(str)
      }
    }
  })
  