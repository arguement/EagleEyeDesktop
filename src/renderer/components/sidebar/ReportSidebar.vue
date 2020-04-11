<template>
  <div class="sticky-top" id="sidebar-wrapper">
    <router-view></router-view>
    <nav id="sidebar-nav" class="nav flex-column">
      <svg id="eye" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="18px" height="18px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 4C7 4 2.73 7.11 1 11.5 2.73 15.89 7 19 12 19s9.27-3.11 11-7.5C21.27 7.11 17 4 12 4zm0 12.5c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
      <li class="nav-item">
        <router-link to="/home" class="nav-link">DASHBOARD</router-link>
      </li>
      <li id="tasks-link" class="nav-item">
        <router-link id="dashboard-link-reports" to="/reports" class="nav-link">REPORTS</router-link>
      </li>
      
      <li id="tasks-link" class="nav-item">
        <router-link  to="/analytics" class="nav-link" >CRIME MAP</router-link>
      </li>
      
      <li id="log-out" class="nav-item">
        <router-link  to="/" class="nav-link">LOG OUT</router-link>
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
#sidebar-wrapper {
  height: 100%; /* Full-height: remove this if you want "auto" height */
  width: 230px; /* Set the width of the sidebar */
  position: fixed; /* Fixed Sidebar (stay in place on scroll) */
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  background-color: white; /* Black */
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 20px;
}

nav .nav-link {
  font-size: 12px;
  letter-spacing: 1px;
  color: #ABB2B9;
  font-weight: 600;
}

#sidebar-nav {
  margin-left: 50px;
  margin-right: 50px;
  
}

#dashboard-link-reports{
  color: #5C6BC0;
  letter-spacing: 1px;
  font-weight: 600;
}

.nav-link:hover {
  color: #5C6BC0;
}
</style>