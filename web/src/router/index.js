import Vue from 'vue'
import Router from 'vue-router'
import MainList from '@/components/MainList'
import SideMain from '@/components/SideMain'
Vue.use(Router) // 开插件
const route = [
  {
    path: '/',
    name: 'Main',
    components: {
      main: MainList,
      side: SideMain
    }
  }
]
export default new Router({
  routes: route
})
