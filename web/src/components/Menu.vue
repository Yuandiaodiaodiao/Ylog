<template>
  <div>
    <el-row>
      <el-col class="col1" :span="2">
        <img class="img-logo" src="../assets/logo1.png" alt="logo1">
      </el-col>
      <el-col class="col1" :span="2">
        <div class="item1">YLOG</div>
      </el-col>
      <el-col :span="20">
        <el-menu mode="horizontal" >
          <el-menu-item index="1">博客</el-menu-item>
          <el-menu-item index="2">吃瓜</el-menu-item>
          <el-menu-item index="3">消息</el-menu-item>
          <el-menu-item index="5">
            <img class="img1" src="https://s1.ax1x.com/2018/12/26/FgDePg.jpg" alt="FgDePg.jpg" border="0"/>
          </el-menu-item>
          <el-submenu :show-timeout=50 :hide-timeout=50 index="4">
            <template slot="title">{{userNickName}}</template>
            <el-menu-item index="2-1">个人资料</el-menu-item>
            <el-menu-item index="2-2">设置</el-menu-item>
            <el-menu-item index="2-3">注销</el-menu-item>
          </el-submenu>
          <el-menu-item index="6">关于</el-menu-item>
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
  .img-logo{
    vertical-align: middle;
  }
  .el-col {
    line-height: 60px;
    border-radius: 4px;
  }
</style>
