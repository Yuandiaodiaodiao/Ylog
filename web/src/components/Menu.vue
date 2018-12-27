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
        <el-menu  class="right-side" mode="horizontal" >
          <el-menu-item v-show="true" index="0">Login</el-menu-item>
          <el-menu-item index="1">Space</el-menu-item>
          <el-menu-item index="2">New</el-menu-item>
          <el-menu-item index="3">Create</el-menu-item>
          <el-menu-item index="4">Message</el-menu-item>
          <el-menu-item index="5">
            <img class="img1" src="https://s1.ax1x.com/2018/12/26/FgDePg.jpg" alt="FgDePg.jpg" border="0"/>
          </el-menu-item>
          <el-submenu :show-timeout=50 :hide-timeout=50 index="4">
            <template slot="title">{{userNickName}}</template>
            <el-menu-item index="2-1">Profile</el-menu-item>
            <el-menu-item index="2-2">Setting</el-menu-item>
            <el-menu-item index="2-3">About</el-menu-item>
            <el-menu-item index="2-4">Logout</el-menu-item>
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
  }
}
</script>

<style scoped>
  .right-side{
    float: right;
  }
  .img1{
    height: 100%;
    margin-bottom: 10px;
  }

  .img-logo{
    vertical-align: middle;
  }
  .el-col {
    line-height: 60px;
    border-radius: 4px;
  }
</style>
