import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Personal from '@/components/Personal'
Vue.use(Router) // 开插件
const route = [
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/login',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/person',
    name: 'Personal',
    component: Personal
  }
]
export default new Router({
  routes: route
})
