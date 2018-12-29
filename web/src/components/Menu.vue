<template>
  <div>
    <el-row>
      <el-col class="col1" :span="2">
        <img class="img-logo" src="../assets/logo1.png" alt="logo1">
      </el-col>
      <el-col class="col1" :span="2">
        <div class="item1" style="font-weight: bold ">YLOG</div>
      </el-col>
      <el-col :span="20">
        <el-menu :router=true :default-active="activate_page"  class="right-side" mode="horizontal" >
          <el-menu-item  v-show="$route.name=='article'" index="-1" >
              <el-button  round icon="el-icon-arrow-left" style="font-size: 14px;" v-on:click="on_back">Back</el-button>
          </el-menu-item>
          <el-menu-item  v-show="!this.$store.state.is_login" index="/login" :route="{path: '/login'}">Login</el-menu-item>
          <el-menu-item v-show="this.$store.state.is_login" index="/space">Space</el-menu-item>
          <el-menu-item index="/" :route="{path: '/'}">New</el-menu-item>
          <el-menu-item  v-show="this.$store.state.is_login"  index="/create" :route="{path: '/create'}">Create</el-menu-item>
          <el-menu-item  v-show="this.$store.state.is_login"  index="4">Message</el-menu-item>
          <el-submenu :show-timeout=50 :hide-timeout=50 index="4">
            <template slot="title" class="col1">
              <div style="display: inline;margin-right: 5px">{{this.$store.state.username}}</div>
              <img style="height: 50%;display: inline" class="img-logo" src="https://s1.ax1x.com/2018/12/26/FgDePg.jpg" alt="FgDePg.jpg" border="0"/>
            </template>
            <el-menu-item index="2-1">Profile</el-menu-item>
            <el-menu-item index="2-2">Setting</el-menu-item>
            <el-menu-item index="2-3">About</el-menu-item>
            <el-menu-item index="2-4" v-on:click="logout" style="color: #F56C6C">Logout</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Menu',
  props: {
    userNickName: String
  },
  methods: {
    logout: function () {
      this.$store.commit('login', false)
      this.$router.push('/login')
      this.$cookies.set('password', '')
    },
    on_back: function () {
      this.$router.go('-1')
    }
  },
  computed: {
    activate_page: function () {
      return this.$route.path
    }
  }
}
</script>

<style scoped>
  .right-side{
    float: right;
  }
  .img-logo{
    vertical-align: middle;
  }
  .col1 {
    line-height: 60px;
    border-radius: 4px;
  }
</style>
