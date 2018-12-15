var info_choose = new Vue({
	el:"#course_info_choose",
	data:{
		input:null,
		num:30,
		courses: [],
		state:'',
		input_start_w:'',
		input_end_w:'',
		value: '',
		selectedOptions:[],
		options:[
			{
				value: '选项1',
				label: '否'
			},
			{
				value: '选项2',
				label: '单周'
			},
			{
				value: '选项3',
				label: '双周'
			},
		],
		time:[
			{
				value: 'Monday',
				label: '周一',
				children:[
					{
						value:'12',
						label:'12'
					},
					{
						value:'34',
						label:'34'
					},
					{
						value:'345',
						label:'345'
					},
					{
						value:'67',
						label:'67'
					},
					{
						value:'89',
						label:'89'
					},
					{
						value:'890',
						label:'890'
					},
					{
						value:'AB',
						label:'AB'
					},
					{
						value:'ABC',
						label:'ABC'
					}
				]
			},
			{
				value: 'Tuesday',
				label: '周二',
				children:[
					{
						value:'12',
						label:'12'
					},
					{
						value:'34',
						label:'34'
					},
					{
						value:'345',
						label:'345'
					},
					{
						value:'67',
						label:'67'
					},
					{
						value:'89',
						label:'89'
					},
					{
						value:'890',
						label:'890'
					},
					{
						value:'AB',
						label:'AB'
					},
					{
						value:'ABC',
						label:'ABC'
					}
				]
			},
			{
				value: 'Wednesday',
				label: '周三',
				children:[
					{
						value:'12',
						label:'12'
					},
					{
						value:'34',
						label:'34'
					},
					{
						value:'345',
						label:'345'
					},
					{
						value:'67',
						label:'67'
					},
					{
						value:'89',
						label:'89'
					},
					{
						value:'890',
						label:'890'
					},
					{
						value:'AB',
						label:'AB'
					},
					{
						value:'ABC',
						label:'ABC'
					}
				]
			},
			{
				value: 'Thursday',
				label: '周四',
				children:[
					{
						value:'12',
						label:'12'
					},
					{
						value:'34',
						label:'34'
					},
					{
						value:'345',
						label:'345'
					},
					{
						value:'67',
						label:'67'
					},
					{
						value:'89',
						label:'89'
					},
					{
						value:'890',
						label:'890'
					},
					{
						value:'AB',
						label:'AB'
					},
					{
						value:'ABC',
						label:'ABC'
					}
				]
			},
			{
				value: 'Friday',
				label: '周五',
				children:[
					{
						value:'12',
						label:'12'
					},
					{
						value:'34',
						label:'34'
					},
					{
						value:'345',
						label:'345'
					},
					{
						value:'67',
						label:'67'
					},
					{
						value:'89',
						label:'89'
					},
					{
						value:'890',
						label:'890'
					},
					{
						value:'AB',
						label:'AB'
					},
					{
						value:'ABC',
						label:'ABC'
					}
				]
			},
			{
				value: 'Saturday',
				label: '周六',
				children:[
					{
						value:'12',
						label:'12'
					},
					{
						value:'34',
						label:'34'
					},
					{
						value:'345',
						label:'345'
					},
					{
						value:'67',
						label:'67'
					},
					{
						value:'89',
						label:'89'
					},
					{
						value:'890',
						label:'890'
					},
					{
						value:'AB',
						label:'AB'
					},
					{
						value:'ABC',
						label:'ABC'
					}
				]
			},
			{
				value: 'Sunday',
				label: '周日',
				children:[
					{
						value:'12',
						label:'12'
					},
					{
						value:'34',
						label:'34'
					},
					{
						value:'345',
						label:'345'
					},
					{
						value:'67',
						label:'67'
					},
					{
						value:'89',
						label:'89'
					},
					{
						value:'890',
						label:'890'
					},
					{
						value:'AB',
						label:'AB'
					},
					{
						value:'ABC',
						label:'ABC'
					}
				]
			}
		]
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