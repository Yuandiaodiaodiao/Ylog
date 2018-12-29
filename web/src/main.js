// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import md5 from 'js-md5'
import axios from 'axios'
import App from './App'
import router from './router'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import Vuex from 'vuex'
import vuecookie from 'vue-cookies'
import api from '@/api/api'
import qs from 'qs'

// element
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.prototype.strify = qs.stringify
Vue.use(api)
Vue.use(Vuex)
Vue.use(Element, { size: 'small', zIndex: 3000 })
Vue.use(mavonEditor)
Vue.config.productionTip = false
Vue.use(vuecookie)
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.crossDomain = true
axios.defaults.withCredentials = true
Vue.prototype.axios = axios
Vue.prototype.$md5 = md5
const store = new Vuex.Store({
  state: {
    is_login: false,
    api_url: '',
    username: '',
    passwordmd5: '',
    uid: -1,
    cache1: {
      bid: 0,
      title: '',
      value: ''
    }
  },
  mutations: {
    login (state, bol) {
      state.is_login = bol
    },
    create_cache (state, paylod) {
      state.cache1.title = paylod.title
      state.cache1.value = paylod.value
      state.cache1.bid = paylod.bid
    }
  }
})
console.log('pre start1')
/* eslint-disable no-new */

new Vue({
  el: '#app', // 233
  router,
  store,
  render: h => h(App)
})
