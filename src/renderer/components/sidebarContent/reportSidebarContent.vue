<template>
  <div id="home-sidebar-content">
    <router-view></router-view>
    <h1>report</h1>
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

#home-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
}
</style>