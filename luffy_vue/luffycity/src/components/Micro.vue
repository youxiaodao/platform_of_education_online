<template>
    <h3>微职位:{{this.title}}</h3>
</template>

<script>
    export default {
        name: "Micro",
        data(){
            return{
              title:''
            }

        },
        mounted(){
          // 这样写，那么需要登录权限才能访问的页面都需要协商这一句
          //vue自带拦截器可以帮我们做,并且，需要在路由中加上标识
          if(!this.$store.state.token){
            this.$router.push({name:'login'})
          }
          this.initMicro()
        },
        methods:{
          initMicro(){
            var _this = this;
            this.$axios.request({
              url:'http://127.0.0.1:8000/api/v1/micro',
              method:'GET',
              params:{token:this.$store.state.token}
            }).then(function (arg) {
              console.log(arg);
              if(arg.data.code ===1000){
                _this.title = arg.data.title
              }
            })
          }
      }
    }
</script>

<style scoped>

</style>
