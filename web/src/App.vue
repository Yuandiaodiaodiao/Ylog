<template>
  <div id="app">
      <el-container>
        <el-header>
          <Menu></Menu>
        </el-header>
        <el-container>
          <el-aside width=auto>
            <router-view name="side"></router-view>
          </el-aside>
          <el-main>
            <router-view name="main"></router-view>
          </el-main>
        </el-container>
      </el-container>
  </div>
</template>

<script>
import Menu from '@/components/Menu'
export default {
  name: 'App',
  components: {
    Menu
  },
  method: {
  },
  created: async function () {
    this.$store.state.api_url = 'http://' + window.location.hostname + ':80' + '/api'
    console.log('login_cookie')
    if (this.$cookies.isKey('username') && this.$cookies.isKey('password')) {
      this.$store.state.username = this.$cookies.get('username')
      let res = await this.$login_api(this.$cookies.get('username'), this.$cookies.get('password'))
      this.$store.commit('login', res.code)
      if (res.code === true) {
        this.$router.push({path: '/'})
      }
    }
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: absolute;
  width: 100%;
  height: 100%;
  margin-top: 0px;
}
.el-aside,.el-main,#app{
  background-color: #f6f6f6;
}
.el-header{
  margin-top: 0px;
  background-color: #ffffff;
  box-shadow: 1px 1px 5px #cacaca ;
  margin-bottom: 5px;
}
</style>
