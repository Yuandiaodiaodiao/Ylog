<template>
  <keep-alive>
    <div>
      <el-row>
        <el-col :span="12">
          <el-card style="margin-left: 20px;margin-right: 20px;margin-bottom:10px ">
            <el-input v-model="title" placeholder="title"></el-input>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card style="margin-left: 20px;margin-right: 20px;margin-bottom:10px">
            <el-button v-on:click="push" type="primary">发表</el-button>
            <el-button v-on:click="clr" type="primary">编辑修改</el-button>
          </el-card>
        </el-col>
      </el-row>
      <mavon-editor v-model="value"/>
    </div>
    </keep-alive>
</template>

<script>
export default {
  name: 'Create',
  data () {
    return {
      title: this.$store.state.cache1.title,
      value: this.$store.state.cache1.value
    }
  },
  beforeDestroy: function () {
    console.log('val=' + this.value)
    this.$store.commit({
      type: 'create_cache',
      title: this.title,
      value: this.value
    })
  },
  methods: {
    clr: async function () {
      console.log('create go!')
      let res = await this.axios.post(
        this.$store.state.api_url + '/create',
        JSON.stringify({
          title: this.title,
          value: this.value,
          uid: this.$store.state.uid,
          bid: this.$store.state.cache1.bid

        })
      )
      let js = res.data
      if (js.code === 'success') {
        this.$message({
          message: '博客发表成功',
          type: 'success',
          duration: 2
        })
        let bid = js.bid
        console.log('bid' + bid)
        this.$router.push({name: 'article', params: {bid}})
      }
    },
    push: async function () {
      this.$store.state.cache1.bid = -1
      this.clr()
    }
  }
}
</script>

<style scoped>
  .inline{
    display: inline;
  }
</style>
