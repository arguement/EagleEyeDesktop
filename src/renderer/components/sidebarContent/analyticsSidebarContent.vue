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


    <MglMap :accessToken="accessToken" :mapStyle="mapStyle" id="map"/>



  </div>
</template>

<script>
import Mapbox from "mapbox-gl";
import { MglMap } from "vue-mapbox";

import navbar from '../navbar/navbar'
export default {
  components: { navbar, MglMap },
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
      vue: require('vue/package.json').version,
       accessToken: 'pk.eyJ1IjoiZWFnbGVleWVjYXBzdG9uZSIsImEiOiJjazhwM3l4engxYnNjM2VuMjU5aml1ZDNmIn0.GYqnPa1M3_CzYD1G3kQy3w', // your access token. Needed if you using Mapbox maps
      mapStyle: 'mapbox://styles/eagleeyecapstone/ck8p5xjd4022u1imspdl62b83' // your map style
    }
  },

  created() {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox;
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