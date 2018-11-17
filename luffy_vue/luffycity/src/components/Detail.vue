<template>
    <div class="detail">
      <h3>课程详细页</h3>
      <p>课程名:{{detail.title}}</p>
      <p>等级:{{detail.level}}</p>
      <p>图片:{{detail.img}}</p>
      <p>课程:{{detail.course}}</p>
      <p>口号{{detail.slogon}}</p>
      <p>为什么学习:{{detail.why_learn}}</p>
      <h2>课程章节</h2>
      <ul v-for="item in detail.chapter">
        <li>{{item.title}}</li>
      </ul>
      <h2>推荐课程</h2>
      <ul v-for="item in detail.recommends_2">
        <!--这样写了之后，路由URL变了，但是网页没有加载，因为mounted方法只有在文档加载的时候才会执行，但是现在网页不会重新加载-->
        <!--<li>-->
          <!--<router-link :to="{name:'detail',params:{id:item.id}}">-->
            <!--{{item.title}}-->
          <!--</router-link>-->
        <!--</li>-->
        <!--要换一种写法 绑定点击事件-->
        <li @click="changeDetail(item.id)">
            {{item.title}}
        </li>
      </ul>
    </div>
</template>

<script>
    export default {
        name: "detail",
        data(){
            return{
                detail:{
                    course:null,
                    img:null,
                    level:null,
                    slogon:null,
                    title:null,
                    why_learn:null,
                    chapter:[],
                    recommends_2:[]
                }

            }
        },
        mounted(){
          var nid =this.$route.params.id;
          this.initCourseDetail(nid)
        },
        methods:{
            initCourseDetail(nid){
                var _this = this;
                this.$axios.request({
                    url:`http://127.0.0.1:8000/api/v1/course/${nid}`,
                    method:'GET'
                }).then(function(ret){
                    console.log(ret.data);
                    _this.detail = ret.data.data
                }).catch(function(){

                })
            },
            changeDetail(nid){
              this.initCourseDetail(nid);
              //和router-link的功能是一样的,改变URL
              this.$router.push({name:'detail',params:{id:nid}})
            }

        }
    }
</script>

<style scoped>

</style>
