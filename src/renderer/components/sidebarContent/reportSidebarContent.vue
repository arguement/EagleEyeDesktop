<template>
  <div id="reports-sidebar-content">
    <router-view></router-view>
    <div id="reports-content">
    <ul class="nav">
      <li class="nav-item">
        <h1 id="reports-label">REPORTS</h1>
      </li>
      <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" id="input-search" type="search" placeholder="Search" aria-label="Search">
    </form>
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

#reports-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
}

#reports-content {
    margin: 20px;
}

#reports-label {
    font-size: 16px;
}
</style>