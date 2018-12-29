<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>
        <el-button type="text" v-on:click="jump">{{title}}</el-button>
      </span>
      <div v-show="iss" style="float: right; padding: 3px 0">{{"作者: "+username}}</div>
      <el-button v-show="!iss" style="float: right; padding: 3px 0" type="text" v-on:click="dele">删除</el-button>
      <el-button v-show="!iss" style="float: right; padding: 3px 0" type="text" v-on:click="edit">编辑</el-button>
    </div>
    <div>{{summary}}</div>
  </el-card>
</template>

<script>
export default {
  name: 'Card',
  props: {
    username: String,
    bid: Number,
    title: String,
    summary: String
  },
  data () {
    return {
      // title: '',
      // summary: '',
      // link: ''
    }
  },
  computed: {
    iss: function () {
      return this.username !== false
    },
    bids: function () {
      return this.bid
    }
  },
  methods: {
    jump: function () {
      console.log('jump')
      let bid = this.bids
      this.$router.push({name: 'article', params: {bid}})
    },
    dele: function () {
      let bid = this.bids
      this.$del_api(bid)
      this.title = ''
      this.summary = ''
    },
    edit: function () {
      this.$store.commit({
        type: 'create_cache',
        title: this.title,
        value: this.summary,
        bid: this.bid
      })
      this.$router.push({name: 'create'})
    }
  }
}
</script>

<style scoped>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 1px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    /*width: 100%;*/
    margin-left: 5px;
    margin-right: 5px;
    margin-top: 10px;
    margin-bottom: 10px;
  }
</style>
