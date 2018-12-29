<template>
  <div>
    <!--<el-button type="primary" v-on:click="add">刷新</el-button>-->
    <!--<el-button type="danger" v-on:click="del">删除</el-button>-->
    <ul style="margin-right: 40px">
      <li
        is="Card"
        v-for="item in blogs"
        v-bind:key="item.bid"
        v-bind:title="item.title"
        v-bind:bid="item.bid"
        v-bind:username='false'
        v-bind:summary="item.value.substr(0, 400)"
      ></li>
    </ul>
    <el-button-group style="margin: auto">
      <el-button type="primary" icon="el-icon-arrow-left" v-on:click="prevpage">上一页</el-button>
      <el-button type="primary" v-on:click="nextpage">下一页<i class="el-icon-arrow-right el-icon--right"></i></el-button>
    </el-button-group>
  </div>
</template>

<script>
import Card from '@/components/Card'
export default {
  name: 'MainList',
  components: {
    Card
  },
  data () {
    return {
      blogs: [
      ]
    }
  },
  methods: {
    add: function () {
      this.blogs.push({
        title: 'd',
        summary: 'e'
      })
    },
    del: function () {
      this.blogs.pop()
    },
    nextpage: async function () {
      if (this.blogs.length !== 0) {
        let unixtime = this.blogs[this.blogs.length - 1]['编辑时间']
        for (let i of this.blogs) {
          unixtime = Math.min(i['编辑时间'], unixtime)
        }
        console.log('unixtime=' + unixtime)
        let js = await this.$get_ten_api(unixtime, '<')
        if (js.code === true) {
          this.blogs = js.js
        }
      }
    },
    prevpage: async function () {
      if (this.blogs.length !== 0) {
        let unixtime = this.blogs[0]['编辑时间']
        for (let i of this.blogs) {
          unixtime = Math.max(i['编辑时间'], unixtime)
        }
        console.log('unixtime=' + unixtime)
        let js = await this.$get_ten_api(unixtime, '>')
        if (js.code === true) {
          this.blogs = js.js
        }
      }
    }
  },
  created: async function () {
    let unixtime = this.$unixtime()
    let js = await this.$get_my_api(unixtime, '<', this.$store.state.uid)
    if (js.code === true) {
      this.blogs = js.js
    }
  }
}
</script>

<style scoped>

</style>
