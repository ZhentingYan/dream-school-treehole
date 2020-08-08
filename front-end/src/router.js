import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Auth from '@/views/Auth.vue'
import Post from '@/views/Post.vue'
import PersonInfo from '@/views/PersonInfo.vue'
import PostDetail from '@/views/PostDetail.vue'

Vue.use(VueRouter)

export default new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth,
    },
    {
      path: '/post',
      name: 'Post',
      component: Post,
    },
    {
      path: '/info',
      name: 'PersonInfo',
      component: PersonInfo,
    },
    {
      path: '/post-detail/:id',
      name: 'PostDetail',
      component: PostDetail,
    },
  ],
})
