import Vue from 'vue'
import Router from 'vue-router'
import MainList from '@/components/MainList'
import SideMain from '@/components/SideMain'
import Login from '@/components/Login'
import Create from '@/components/Create'
import Article from '@/components/Article'
import SpaceList from '@/components/SpaceList'
Vue.use(Router) // 开插件
const route = [
  {
    path: '/',
    name: 'Main',
    components: {
      main: MainList,
      side: SideMain
    }
  },
  {
    path: '/login',
    name: 'login',
    components: {
      main: Login
    }
  },
  {
    path: '/create',
    name: 'create',
    components: {
      main: Create
    },
    meta: { keepAlive: true }
  },
  {
    path: '/article/:bid',
    name: 'article',
    components: {
      main: Article
    }
  },
  {
    path: '/space',
    name: 'space',
    components: {
      main: SpaceList,
      side: SideMain
    }
  }

]
export default new Router({
  routes: route
})
