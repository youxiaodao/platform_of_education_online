<template>
    <div class="course">
      <h1>课程列表</h1>
      <!-- <ul v-for="item in courseList">
        <li>
          <router-link :to="{name:'detail',params:{id:item.id}}">
            {{item.title}}
          </router-link>
        </li>
      </ul> -->
      <div v-for="row in courseList">
        <div style="width:350px;float:left;">
          <img src="" alt="">
          <h3>
            <router-link :to="{name:'detail',params:{id:row.id}}">
              {{row.title}}
            </router-link>
          </h3>
          <p>{{row.level}}</p>

        </div>

      </div>
    </div>
</template>

<script>
    export default {
        name: "Course",
        data(){
          return{
            courseList:[
            ]
          }
        },
        mounted(){
          this.initCourse()
        },
        methods:{
          initCourse(){
            var _this  =this
            this.$axios.request({
              url:'http://127.0.0.1:8000/api/v1/course/',
              method:'GET',
            }).then(function(ret){
              if(ret.data.code===1000){
                _this.courseList = ret.data.data
              }
            }).catch(function(){
            })
          }
        }
    }
</script>

<style scoped>

</style>
