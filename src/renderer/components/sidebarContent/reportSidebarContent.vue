<template>
  <div id="reports-sidebar-content">
    <router-view></router-view>
    <navbar></navbar>
    <div id="reports-content">
    <ul class="nav">
      <li class="nav-item">
        <h1 id="reports-label">REPORTS</h1>
      </li>
      <form id="search-form" class="form-inline my-2 my-lg-0">
      <input class="form-control" id="input-search" type="search" placeholder="Find something" aria-label="Search">
    </form>
    
    </ul>
    <h1>{{ reports[0]["Victims-Firstname"] }}</h1>
    </div>
  </div>
</template>

<script>
import navbar from '../navbar/navbar'
import {db} from '../../../../static/js/fire_config'
export default {
  components: { navbar },
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
      reports: []
    }
  },
    created(){

      let report = db.collection("Crime Report").get()
        .then(snapshot => {
          snapshot.forEach(doc => {
            this.reports.push(doc.data());
            console.log(doc.data());
          });
        })
        .catch(err => {
          console.log('Error getting documents', err);
        });

      
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
    margin-left: 50px;
    margin-right: 20px;
    margin-top: 60px;
}

#input-search {
  border: none;
  border-radius: 4px;
  background: #E5E7E9;
  height: 40px;
  font-size: 13px;
  letter-spacing: 0.5px;
  font-weight: 400;
  width: 300px;
  color: #85929E;
}


#reports-label {
    font-size: 16px;
    margin-top: 14px;
}

input:focus, input.form-control:focus {

    outline:none !important;
    outline-width: 0 !important;
    box-shadow: none;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
}

</style>