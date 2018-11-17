<template>
   <div class="login">
     <h2>登陆页面</h2>
     <input type="text" v-model="username" placeholder="请输入用户名">
     <input type="password" v-model="password" placeholder="请输入密码">
     <input type="button" value="登陆" @click="login">
   </div>
</template>

<script>
    export default {
        name: "Login",
      data(){
          return {
            username: '',
            password: ''
          }
      },
      methods:{
          login(){
            var _this = this;
            this.$axios.request({
              url:this.$store.state.apiList.login,
              method:'POST',
              data:{
                user:this.username,
                pwd:this.password
              },
              headers:{
                'Content-type':'application/json',
                // 'k1':1
              }
            }).then(function (arg) {
              if(arg.data.code === 1000){
                // _this.$store.state.token = arg.data.token;
                // 没必要在返回一次username，直接用前端输入的，但是如果有昵称，就需要返回昵称了
                // _this.$store.state.username = _this.username
                _this.$store.commit('saveToken',{token:arg.data.token,username:_this.username});
                var url =_this.$route.query.back_url;
                //因为用了this.￥router.query导致登陆后不能跳转到back_url
                if(url){
                  _this.$router.push({path:url})
                }else {
                  _this.$router.push({path:'/index'})
                }
              }else {
                alert(arg.data.error)
              }
            }).catch(function (arg) {
              console.log('发生错误',arg)
            })
          }
      }


    }
</script>

<style scoped>

</style>
