<template>
  <div>
    <el-button type="primary" v-on:click="add">刷新</el-button>
    <el-button type="danger" v-on:click="del">删除</el-button>
    <ul>
      <li
        is="Card"
        v-for="item in blogs"
        v-bind:key="item.title"
        v-bind:title="item.title"
        v-bind:summary="item.summary"
      ></li>
    </ul>
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
        {
          title: 'a',
          summary: 'b'
        },
        {
          title: 'c',
          summary: 'd'
        }
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
    }
  }
}
</script>

<style scoped>

</style>
