import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

import Course from '@/components/Course'
import Detail from '@/components/Detail'
import Index from '@/components/Index'
import Micro from '@/components/Micro'
import News from '@/components/News'
import Login from '@/components/Login'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/course',
      name: 'course',
      component: Course,
      meta:{
        requireAuth: true
      }
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: Detail
    },
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/micro',
      name: 'micro',
      component: Micro,
      meta:{
        requireAuth: true
      }
    },
    {
      path: '/news',
      name: 'news',
      component: News
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
  ],
  mode:'history'
})
