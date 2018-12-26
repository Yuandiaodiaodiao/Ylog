<template>
  <div id="app">
    <img src="./assets/logo.png">
    <p>233</p>
    <router-link to="/login">Login</router-link>
    <router-link to="/person">个人主页</router-link>
    <router-view name="default"></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
