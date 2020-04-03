<template>
  <div id="logoContent">
    <router-view></router-view>
    <h1>I'm a login side thingy</h1>
  </div>
</template>

<script>
export default {
  data () {
    return {
      electron: process.versions.electron,
      name: this.$route.name,
      node: process.versions.node,
      path: this.$route.path,
      platform: require('os').platform(),
      vue: require('vue/package.json').version
    }
  }
}
</script>

<style>
#logoContent {
    margin-left: 200px;
    margin-right: 0px;
    display: flex;
    justify-content: center;
}
</style>