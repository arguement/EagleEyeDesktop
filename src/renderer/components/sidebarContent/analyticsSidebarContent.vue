<template>
  <div id="analytics-sidebar-content">
    <router-view></router-view>
    
    <nav id="page-nav" class="navbar navbar-expand-lg navbar-light bg-light">
        <li class="navbar-brand">
        <h1 id="dashboard-label">ANALYTICS</h1>
      </li>
   
</nav>



  </div>
</template>

<script>
import {store} from "../../store/store"
import {db} from '../../../../static/js/fire_config'
export default {
  data () {
    return {
      electron: process.versions.electron,
      name: this.$route.name,
      node: process.versions.node,
      path: this.$route.path,
      platform: require('os').platform(),
      vue: require('vue/package.json').version,
      storeState: store.state
    }
  },
}
</script>

<style>
#analytics-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
  margin-left: 230px
}
</style>