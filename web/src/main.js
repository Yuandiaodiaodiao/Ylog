// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
// element
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(Element, { size: 'small', zIndex: 3000 })
Vue.use(mavonEditor)
Vue.config.productionTip = false
console.log('pre start1')
/* eslint-disable no-new */
new Vue({
  el: '#app', // 233
  router,
  render: h => h(App)
})
