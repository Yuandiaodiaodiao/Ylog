<template>
    <div>
      <el-card>
        <div class="margin-std" style="font-weight: bold">Welcome To YLOG</div>
        <el-input onkeyup="value=value.replace(/[^\w\u4E00-\u9FA5]/g, '')" class="margin-std" maxlength="16"  v-model="input1" placeholder="account" clearable ></el-input>
        <el-input onkeyup="value=value.replace(/[^\w\u4E00-\u9FA5]/g, '')" type="password" maxlength="32" class="margin-std" :clearable="true" v-model="input2" placeholder="password"></el-input>
        <div  style="margin: auto; width: 100%;height: 16px;">
          <div v-if="if_error" style="color: red;float: left;font-size: 12px; padding: 9px 15px; border-radius: 3px;">{{error_str}}</div>
          <el-button style="float: right; " type="text">Forgot password?</el-button>
        </div>
        <el-row class="margin-std" style="padding:10px;">
          <el-col :span="12">
            <el-button v-on:click="login" type="primary" :disabled="username_len">Login</el-button>
          </el-col>
          <el-col :span="12">
            <el-button  v-on:click="register" type="primary" :disabled="username_len">Register</el-button>
          </el-col>
        </el-row>
      </el-card>
    </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      if_error: false,
      input1: this.$store.state.username,
      input2: '',
      error_str: ''
    }
  },
  computed: {
    username_len: function () {
      return this.input1.length < 6 || this.input2.length < 6
    }
  },
  methods: {
    login: async function () {
      let res = await this.$login_api(this.input1, this.$md5(this.input2))
      this.error_str = res.strs
      this.if_error = !res.code
      this.$store.commit('login', res.code)
      if (res.code === true) {
        this.$router.push({path: '/space'})
      }
    },
    register: async function () {
      if (this.input1.length < 6) {
        this.error_str = 'username is too short'
      }
      let res = await this.$register_api(this.input1, this.$md5(this.input2))
      this.error_str = res.strs
      this.if_error = !res.code
      this.$store.commit('login', res.code)
      console.log(res.code)
      if (res.code === true) {
        this.login()
        console.log('route')
      }
    }
  }
}
</script>

<style scoped>
  .right-side{
    float: right;
  }
.el-card{
  margin: auto;
  width: 360px;
}

.el-input{
  width: 90%;
}
  .margin-std{
    margin: 10px;
  }
</style>
