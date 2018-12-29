<template>
  <div>
    <mavon-editor v-model="valux" :subfield="false" :defaultOpen="defaultData" :toolbarsFlag="false" :boxShadow="false"></mavon-editor>
  </div>
</template>

<script>
export default {
  name: 'Article',
  data () {
    return {
      valux: '',
      js: {title: '', value: ''},
      defaultData: 'preview'
    }
  },
  watch: {
    js: function (val, old) {
      this.valux = '# ' + val.title + '  \n' + val.value
    }
  },

  created: async function () {
    let bid = this.$route.params.bid
    let js = await this.$get_article_api(bid)
    if (js.code === true) {
      this.js = js.js
    }
  }
}
</script>

<style scoped>

</style>
