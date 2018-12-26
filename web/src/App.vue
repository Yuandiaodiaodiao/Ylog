<template>
  <div id="app">
      <el-container>
        <el-header>
          <Menu></Menu>
        </el-header>
        <el-container>
          <el-aside width="200px">
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
  background-color: #ffffff;

}
</style>
