var countTime = new Vue({
  el:'#localTime',

  methods:{
    time:function(){
      let date = new Date(+new Date() + 8 * 3600 * 1000)
                .toISOString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '');
      return date;
    }
  }
})
