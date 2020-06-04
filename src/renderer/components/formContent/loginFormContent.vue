<template>
  <div id="logoContent">
    <router-view></router-view>
    <h1></h1>
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
    background-color: #E8EAF6;
    height: 100vh;
    width: 50%;
}
</style>