<template>
  <div>
    <router-view></router-view>
    <nav id="page-nav" class="navbar navbar-expand-lg navbar-light bg-light">
    
    <div id="navbar-icons">
    <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <span class="dot"><div id="user-initials">JD</div></span>          
        <li class="nav-item">
        </li>
    </ul>
    </div>
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
.dot {
  height: 40px;
  width: 40px;
  background-color: #9FA8DA;
  border-radius: 50%;
  display: inline-block;
}

#user-initials {
  margin-left: 9px;
  margin-top: 8px;
  font-weight: 500;
}

#navbar-icons {
    position: absolute;
    right: 0;
}

#notif, #account {
    margin-left: 10px;
    fill: #5C6BC0;
}

#page-nav {
    margin: 20px;
}
</style>