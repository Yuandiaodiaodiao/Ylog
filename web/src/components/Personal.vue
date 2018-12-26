<template>
  <el-container>
    <el-header>
      <el-row>
        <el-col class="col1" :span="6">
          YLOG
        </el-col>
        <el-col  :span="18">
          <el-menu :default-active="activeIndex"  mode="horizontal" @select="handleSelect">
            <el-menu-item index="1">博客</el-menu-item>
            <el-menu-item index="2" >吃瓜</el-menu-item>
            <el-menu-item index="3" >消息</el-menu-item>
            <el-menu-item index="5">
              <img class="img1" src="https://s1.ax1x.com/2018/12/26/FgDePg.jpg" alt="FgDePg.jpg" border="0" />
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
    </el-header>
    <el-container>
      <el-aside width="200px">Aside</el-aside>
      <el-main>
        <Card></Card>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Card from '@/components/Card'
export default {
  name: 'Personal',
  components: {
    Card
  },
  data () {
    return {
      userNickName: '233'
    }
  }
}
</script>

<style scoped>
  .col1{
    text-align: left;
    border-radius: 4px;
  }
  .el-menu{
    float: right;
  }
  .el-row {
    height: 60px;
    margin-bottom: 20px;
    width: 100%;
  }
  .el-row:last-child{
    margin-bottom: 0;
  }
  .el-col {
    border-radius: 4px;
  }
  .img1 {
    width: 40px;
    margin: auto;
  }
  .el-header, .el-footer {
    background-color: #ffffff;
    color: #333;
    text-align: center;
    line-height: 60px;
    /*box-shadow: 10px 10px 5px #880001;*/
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    /*line-height: 160px;*/
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
