<template>
  <div id="analytics-sidebar-content">
    <router-view></router-view>
    <navbar></navbar>
    <div id="analytics-content">
      <ul class="nav">
      <li class="nav-item">
        <h1 id="analytics-label">ANALYTICS</h1>
      </li>
    </ul>
    </div>
  </div>
</template>

<script>
import navbar from '../navbar/navbar'
export default {
  components: { navbar },
  methods: {
    open (link) {
      this.$electron.shell.openExternal(link)
    }
  },
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

#analytics-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
}

#analytics-content {
  margin-left: 50px;
  margin-right: 20px;
  margin-top: 60px;
}

.nav {
  margin-top: 20px;
}

#analytics-label {
  font-size: 16px;
  margin-top: 14px;
}
</style>