<template>
  <div id="home-sidebar-content">
    <router-view></router-view>
    <navbar id="navbar"></navbar>
    <div id="dashboard-content">
      <ul class="nav">
      <li class="nav-item">
        <h1 id="dashboard-label">DASHBOARD</h1>
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

#home-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
}

#dashboard-content {
  margin-left: 50px;
  margin-right: 20px;
  margin-top: 60px;
}

.nav {
  margin-top: 20px;
}

#dashboard-label {
  font-size: 16px;
  margin-top: 14px;
}

#navbar{
  margin-top: 40px;
}
</style>