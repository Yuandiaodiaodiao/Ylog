const api = {
  install: function (Vue) {
    Vue.prototype.$login_api = async function (username, passwdmd5) {
      try {
        this.$cookies.set('username', username)
        this.$cookies.set('password', passwdmd5)
        let res = await this.axios.get(this.$store.state.api_url + '/login')
        let js = res.data
        if (js.code === 'success') {
          this.$store.state.username = username
          this.$store.state.passwordmd5 = passwdmd5
          this.$store.state.uid = js.uid
          console.log('login true')
          return {code: true, strs: 'login success'}
        } else {
          console.log('login failed')
          return {code: false, strs: 'login failed'}
        }
      } catch (e) {
        console.log(e)
        return {code: false, strs: 'server error'}
      }
    }
    Vue.prototype.$register_api = async function (username, passwdmd5) {
      try {
        this.$cookies.set('username', username)
        this.$cookies.set('password', passwdmd5)
        let res = await this.axios.get(this.$store.state.api_url + '/register')
        let js = res.data
        if (js.code === 'success') {
          this.$store.state.username = username
          this.$store.state.passwordmd5 = passwdmd5
          console.log('reg true')
          return {code: true, strs: 'register success'}
        } else {
          console.log('user exists')
          return {code: false, strs: 'user exists'}
        }
      } catch (e) {
        console.log(e)
        return {code: false, strs: 'server error'}
      }
    }
    Vue.prototype.$get_article_api = async function (bid) {
      try {
        let res = await this.axios.post(
          this.$store.state.api_url + '/article',
          JSON.stringify({
            bid: bid
          })
        )
        let js = res.data
        if (js.code === 'success') {
          return {code: true, strs: 'register success', js: js}
        } else {
          console.log('no exists')
          return {code: false, strs: 'not find'}
        }
      } catch (e) {
        console.log(e)
        return {code: false, strs: 'server error'}
      }
    }
    Vue.prototype.$unixtime = function () {
      var tmp = Date.parse(new Date()).toString()
      tmp = tmp.substr(0, 10)
      return tmp
    }
    Vue.prototype.$get_ten_api = async function (unixtime, bigger) {
      try {
        let res = await this.axios.post(
          this.$store.state.api_url + '/getten',
          JSON.stringify({
            time: unixtime,
            cmp: bigger
          })
        )
        let js = res.data
        if (js.code === 'success') {
          return {code: true, strs: 'register success', js: js.js}
        } else {
          console.log('no exists')
          return {code: false, strs: 'not find'}
        }
      } catch (e) {
        console.log(e)
        return {code: false, strs: 'server error'}
      }
    }

    Vue.prototype.$get_my_api = async function (unixtime, bigger, uid) {
      try {
        let res = await this.axios.post(
          this.$store.state.api_url + '/getmy',
          JSON.stringify({
            time: unixtime,
            cmp: bigger,
            uid: uid
          })
        )
        let js = res.data
        if (js.code === 'success') {
          return {code: true, strs: 'register success', js: js.js}
        } else {
          console.log('no exists')
          return {code: false, strs: 'not find'}
        }
      } catch (e) {
        console.log(e)
        return {code: false, strs: 'server error'}
      }
    }

    Vue.prototype.$del_api = async function (bid) {
      try {
        let res = await this.axios.post(
          this.$store.state.api_url + '/del',
          JSON.stringify({
            bid: bid
          })
        )
        console.log(res)
      } catch (e) {
        console.log(e)
        return {code: false, strs: 'server error'}
      }
    }
  }

}

export default api
