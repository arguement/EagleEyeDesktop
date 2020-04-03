<template>
  <div id="home-sidebar-content">
    <router-view></router-view>
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

#dashboard-content {
  margin: 20px;
}

.nav {
  margin-top: 20px;
}

#input-search {
  border: none;
  border-radius: 4px;
  background: #E5E7E9;
  height: 40px;
  font-size: 10px;
  letter-spacing: 0.5px;
  font-weight: 400;
  width: 300px;
  color: #ABB2B9;
}

#dashboard-label {
  font-size: 16px;
}
</style>