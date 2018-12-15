var info_choose = new Vue({
	el:"#course_info_choose",
	data:{
		input:null,
		num:30,
		courses: [],
		state:'',
		value: '',
	},
	methods:{
		querySearch(queryString, cb) {
        var courses = this.courses;
        var results = queryString ? courses.filter(this.createFilter(queryString)) : courses;
        // 调用 callback 返回建议列表的数据
        cb(results);
      },
      createFilter(queryString) {
        return (course) => {
          return (course.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      loadAll() {
        return [
			{"value":"操作系统"},
			{"value":"编译原理"},
			{"value":"数据挖掘"},
			{"value":"计算方法"},
			{"value":"应用密码学"},
			{"value":"智能系统"},
			{"value":"软件工程"},
        ];
      },
      handleSelect(item) {
        console.log(item);
      },
    },
    mounted() {
      this.courses = this.loadAll();
    },
});

var result=new Vue({
	el:"#result",
	data:{
		result:null,
	},
	methods:{
		submit:function(){
		this.result = [{
			classroomId:4201,
			name:'D201',
			Peo:60
		},{
			classroomId:4202,
			name:'D202',
			Peo:70
		},{
			classroomId:7301,
			name:'G301',
			Peo:60
		}];
		}
	}
})