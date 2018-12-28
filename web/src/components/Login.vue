<template>
    <div>
      <el-card>
        <div class="margin-std" style="font-weight: bold">Welcome To YLOG</div>
        <el-input class="margin-std" v-model="input1" placeholder="account" clearable></el-input>
        <el-input type="password" class="margin-std" v-model="input2" placeholder="password"></el-input>
        <div  style="margin: auto; width: 100%;height: 16px;">
          <el-button style="float: right; " type="text">Forgot password?</el-button>
        </div>
        <el-row class="margin-std" style="padding:10px;">
          <el-col :span="12">
            <el-button type="primary">Login</el-button>
          </el-col>
          <el-col :span="12">
            <el-button  type="primary">Register</el-button>
          </el-col>
        </el-row>
      </el-card>
    </div>
</template>

<script>
export default {
  name: 'Login'
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
