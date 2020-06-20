<template>
  <div class="sticky-top" id="sidebar-wrapper">
    <router-view></router-view>
    <nav id="sidebar-nav" class="nav flex-column">

      <div id="logo-dash">
      <svg id="eye" v-on:click="show = !show" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="18px" height="18px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 4C7 4 2.73 7.11 1 11.5 2.73 15.89 7 19 12 19s9.27-3.11 11-7.5C21.27 7.11 17 4 12 4zm0 12.5c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/>
      </svg>
      </div>

      <li class="nav-item">
        <router-link to="/home" class="nav-link">DASHBOARD</router-link>
      </li>
      
      <li id="tasks-link" class="nav-item">
        <router-link to="/reports" class="nav-link">REPORTS</router-link>
      </li>
      
      <li id="tasks-link" class="nav-item">
        <router-link to="/map" class="nav-link" >CRIME MAP</router-link>
      </li>

      <li id="tasks-link" class="nav-item">
        <router-link to="/analytics" class="nav-link" >ANALYTICS</router-link>
      </li>
     
      <li id="tasks-link" class="nav-item">
        <router-link to="/allusers" class="nav-link" id="dashboard-link-user">USERS</router-link>
      </li>
      
      <li id="task-link" class="nav-item">
        <router-link to="/modifypriority" class="nav-link">PRIORITY</router-link>
      </li>

      
      
      <li id="log-out" class="nav-item">
        <router-link to="/" class="nav-link">LOG OUT</router-link>
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
      vue: require('vue/package.json').version,
      show: true
    }
  }
}
</script>

<style>
#dashboard-link-user{
  color: #5C6BC0;
  letter-spacing: 1px;
  font-weight: 600;
}

#logo-eye-dash {
  font-size: 10px;
  letter-spacing: 1px;
  font-weight: 300;
  margin-top: 1.5px;
}

#logo-dash {
  display: flex;
  flex-direction: row;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
nav .nav-link .nav-item{
  font-size: 12px;
  color: #ABB2B9;
  letter-spacing: 1px;
  font-weight: 600;
}

#sidebar-nav {
  margin-top: 20px;
  margin-left: 50px;
  margin-right: 50px;
}

#dashboard-link-{
  color: #7986CB;
  letter-spacing: 1px;
  font-weight: 600;
}

#eye {
  margin-bottom: 50px;
  margin-top: 20px;
  margin-left: 50px;
  margin-right: 50px;
}

#log-out {
  position: absolute;
  bottom: 0;
  margin-bottom: 20px;
}

#dash {
  fill: #7986CB;
}

#file {
  fill: #ABB2B9
} 
</style>