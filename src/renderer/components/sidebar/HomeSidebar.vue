<template>
  <div>
    <router-view></router-view>
    <nav id="sidebar-nav" class="nav flex-column">
      <li class="nav-item">
        <router-link to="/home" class="nav-link" id="dashboard-link-home">DASHBOARD</router-link>
      </li>
      <li id="tasks-link" class="nav-item">
        <router-link to="/reports" class="nav-link">REPORTS</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/" class="nav-link">LOGIN</router-link>
      </li>
    </nav>
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

nav .nav-link .nav-item{
  font-size: 12px;
  letter-spacing: 1px;
  font-weight: 600;
  color: #ABB2B9;
}

#sidebar-nav {
  margin-top: 100px;
  margin-left: 50px;
  margin-right: 50px;
}

#dashboard-link-home{
  color: #3F51B5;
}
</style>