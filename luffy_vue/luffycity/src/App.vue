<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <!--<router-link to="/">vue主页</router-link>-->
    <router-link to="/index">路飞主页</router-link>
    <router-link to="/course">课程</router-link>
    <router-link to="/micro">微职位</router-link>
    <router-link to="/news">深科技</router-link>
    <div v-if="this.$store.state.token">
      <a href="">{{this.$store.state.username}}</a>
      <a href="" @click="logout">注销</a>
    </div>
    <div v-else>
      <router-link to="/login">登陆</router-link>
    </div>

    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return{

    }
  },
  methods:{
    logout(){
      this.$store.commit('clearToken')
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
