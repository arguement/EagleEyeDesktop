<template>
  <div id="analytics-sidebar-content">
    <router-view></router-view>
    <nav id="analytics-nav" class="navbar navbar-expand-lg navbar-light bg-light">
        <li class="navbar-brand">
        <h1 id="analytics-label">ANALYTICS</h1>
      </li>
    <div id="navbar-icons">
    <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <span class="ana-dot"><div id="user-initials">JD</div></span>          
        <li class="nav-item">
        </li>
    </ul>
    </div>
</nav>
    

    <MglMap :accessToken="accessToken" :mapStyle="mapStyle" :center="coordinates" :zoom="zoom" id="map"/>


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
      mapStyle: 'mapbox://styles/eagleeyecapstone/ck8pjo9j80fes1ims3wsv29t1', // your map style
      coordinates: [-76.836, 17.977],
      zoom: 11.60
    }
  },

  created() {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox;
  }
}
</script>

<style>
.ana-dot {
    display: block;
    margin-top: 30px;
    margin-right: 20px;
    height: 40px;
    width: 40px;
    background-color: #9FA8DA;
    border-radius: 50%;
    display: inline-block;
}

#analytics-nav {
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    top: 0;
    right: 0;
    background-color: transparent!important;
    overflow-x: hidden; /* Disable horizontal scroll */
    transition: 0.5s;
    width: 100%;
    height: 70px;
    padding-left: 270px;
    }

#map{
    box-shadow: 21px 27px 54px -30px rgba(0,0,0,0.75);
    border-radius: 4px;
}

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
  margin-top: 30px;
}
</style>