<template>
  <div id="reports-sidebar-content">
    <router-view></router-view>
    <navbar></navbar>
    <div id="reports-content">

<div id="report-section">
    <div id="report-list">
    <ul id="report-shit" class="nav">
      <li class="nav-item">
        <h1 id="reports-label">REPORTS</h1>
      </li>
      <form id="search-form" class="form-inline my-2 my-lg-0">
      <input class="form-control" id="input-search" type="search" placeholder="Search reports" aria-label="Search">
    </form>
    <p id="report-quatitiy">{{ reports.length }}</p>
    </ul>

<table class="table table-borderless">
  <thead>
    <tr>
      <th scope="col"></th>
      <th scope="col">Offence</th>
      <th scope="col">Name</th>
      <th scope="col">Date</th>
      <th scope="col">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr v-on:click="show = !show; getIndex(index)" id="table-data" v-for="(report, index) in reports" :key="report.id">
      <th scope="row"></th>
      <td>{{ report["Offence"] }}</td>
      <td>{{ report["Victims-Firstname"] }} {{ report["Victims-Surname"] }}</td>
      <td>{{ report["Date-Time"].toDate() }}</td>
      <td></td>
    </tr>
  </tbody>
</table>
    </div>

<div id="user-selected">
    <transition name="fade" :index="index">
  <div v-if="show">
    <p>{{ reports[i] }}</p>
  </div>
  </transition>
</div>
</div>

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
    },
    getIndex: function (index) {
        this.i.pop()
        this.i.push(index)
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
      reports: [],
      show: false,
      i: []
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
tbody {
    background-color: white;
}

#info-shit {
    font-size: 12px;
    letter-spacing: 1px;
    display: flex;
    flex-direction: row;
}

#report-shit {
margin-bottom: 50px;
}

th {
    font-size: 12px;
    color: #5C6BC0;
}

td {
    font-size: 12px;
}

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

#report-quatitiy {
    font-size: 12px;
    margin-top: 14px;
    margin-right: 40px;
}

input:focus, input.form-control:focus {

    outline:none !important;
    outline-width: 0 !important;
    box-shadow: none;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
}

#report-info {
    margin-top: 5px;
    border: none;
    border-radius: 4px;
    height: 50px;
}

#table-data:hover, #table-data:target {
    background-color: #E8EAF6;
}
</style>