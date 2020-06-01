<template>
  <div id="map-sidebar-content">
    <router-view></router-view>

<!-- NAVBAR -->    
    <nav id="map-nav" class="navbar navbar-expand-lg navbar-light bg-light">
        <li class="navbar-brand">
          <h1 id="map-label">CRIME MAP</h1>
        </li> 
        <div id="navbar-icons">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <svg v-on:click="show=!show" id="map-chart" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M11 2v20c-5.07-.5-9-4.79-9-10s3.93-9.5 9-10zm2.03 0v8.99H22c-.47-4.74-4.24-8.52-8.97-8.99zm0 11.01V22c4.74-.47 8.5-4.25 8.97-8.99h-8.97z"/></svg>      </li>
          <li class="nav-item">
            <svg id="map-notif" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg>
          </li>
          <li class="nav-item">
            <span class="map-dot"><div id="user-initials">{{ storeState.user["first-name"].charAt(0) }}{{ storeState.user["surname"].charAt(0) }}</div></span> 
          </li>
        </ul>
        </div>
      </nav>

<!-- MAP SECTION -->
      <div id="map">
        <MglMap :accessToken="accessToken" 
                :mapStyle="mapStyle" 
                :center="coordinates" 
                :zoom="zoom" 
                :container="container" >  
              
              <MglGeocoderControl
      
      :accessToken="accessToken"
      :input.sync="defaultInput"
      @results="handleSearch"
    />  
     <MglMarker :coordinates="crime_coordinates" color="blue" />
        </MglMap>
      </div>

<!-- MAP KEY -->
      <transition name="slide-fade">
        <div v-if="show" class="card">
          <p id="cm-text"></p>
          <div class="card-body">
          </div>
        </div>
      </transition>

  </div>
</template>

<script>
import {store} from "../../store/store"
import Mapbox from "mapbox-gl";
//import geocoder from "vue-mapbox"
import { MglMap, MglNavigationControl, MglGeolocateControl,MglMarker} from 'vue-mapbox' 
import MglGeocoderControl from 'vue-mapbox-geocoder' 
import MapboxGeocoder from 'vue-mapbox-geocoder'
import {db} from '../../../../static/js/fire_config'

export default {
  components: { MglMap,MglGeocoderControl,MapboxGeocoder,MglMarker},
  methods: {
    open (link) {
      this.$electron.shell.openExternal(link)
    },
    handleSearch(event) {
      console.log(event)
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
      accessToken: 'pk.eyJ1IjoiZWFnbGVleWVjYXBzdG9uZSIsImEiOiJjazhwM3l4engxYnNjM2VuMjU5aml1ZDNmIn0.GYqnPa1M3_CzYD1G3kQy3w',
      mapStyle: 'mapbox://styles/eagleeyecapstone/ck8qt1dzu0jdu1jov54rjauq8', // your map style
      coordinates: [-76.836, 17.977],
      zoom: 11.60,
      container: 'map',
      show: false,
      storeState: store.state,
      defaultInput: 'Paris',
      origin: 'https://api.mapbox.com',
      reports:[],
      crime_coordinates:[-78.1035,18.3975],
    }
  },

  created() {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox; 
   
   //gets the report data 
   db.collection("Crime Report").get().then(
     snapshot =>{snapshot.forEach(
       doc=>{
         this.reports.push(doc.data())
         
       });
        //console.log( geocoder.query(this.reports[19]['Offence-location']+ ",Jamaica"))
     })
     console.log(MapboxGeocoder)
  },
  methods:{
    handleSearch(event) {
      console.log(event)
    }
  }
}
</script>

<style>
#cm-text {
  margin-top: 20px;
  font-size: 12px;
  letter-spacing: 0.5px;
  font-weight: 500;
}

.card {
    position: fixed;
    top: 25%;
    left: 5%;
    margin-right: 40px;
    width: 300px;
    height: 500px;
    text-align: center;
    position: absolute;
    border: none!important;
    border-radius: 4px;
    opacity: .5;
}

.map-dot {
  height: 40px;
  width: 40px;
  background-color: #9FA8DA;
  display: inline-block;
  margin-top: 30px;
  border-radius: 100%;
  
}

#map-notif {
    display: block;
    margin-top: 40px;
    margin-right: 20px;
    fill: #9FA8DA;
}

#map-notif:hover{
  fill: #7986CB;
}

#map-chart:hover{
  fill: #7986CB;
}

.map-dot:hover {
  background-color: #7986CB;
}

#map-chart {
    display: block;
    margin-top: 40px;
    margin-right: 20px;
    fill: #9FA8DA;
}

#activity {
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    bottom: 0;
    right: 0;
    overflow-x: hidden; /* Disable horizontal scroll */
    transition: 0.5s; 
}

#map-nav {
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
    margin-right: 50px;
    }

#map-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
  margin-left: 230px
}


#map-label {
  font-size: 16px;
  margin-top: 50px;
  margin-left: 60px;
  letter-spacing: 2px;
}

#map { position: absolute; top: 0; bottom: 0; width: 100%; }

body { margin: 0; padding: 0; }

#fit {
display: block;
position: relative;
margin: 0px auto;
width: 50%;
height: 40px;
padding: 10px;
border: none;
border-radius: 3px;
font-size: 12px;
text-align: center;
color: #fff;
background: #ee8a65;
}

</style>