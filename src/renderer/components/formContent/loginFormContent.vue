<template>
  <div id="logoContent">
    <router-view></router-view>
    <h1 id="eagle-eye">eagle eye</h1>
    <svg id="login-eye" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="50px" height="50px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 4C7 4 2.73 7.11 1 11.5 2.73 15.89 7 19 12 19s9.27-3.11 11-7.5C21.27 7.11 17 4 12 4zm0 12.5c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
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
#logoContent {
    background-color: #E8EAF6;
    height: 100vh;
    width: 50%;
    display: flex;
  flex-direction: column;
  align-items: center;
}

#eagle-eye {
  font-size: 20px;
  letter-spacing: 3px;
  font-weight: 700;
  margin-top: 200px;
}

#login-eye {
}
</style>