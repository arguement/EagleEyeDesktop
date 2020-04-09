<template>
  <div id="reports-sidebar-content">
    <router-view></router-view>
    
    <nav id="page-nav" class="navbar navbar-expand-lg navbar-light bg-light">
        <li class="navbar-brand">
        <h1 id="report-label">REPORTS</h1>
      </li>
    <div id="navbar-icons">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
          <svg id="notif" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg>
        </li>
      <li class="nav-item">
        <span class="dot"><div id="user-initials">JD</div></span>  
      </li>   
    </ul>
    </div>
</nav>

    <div id="reports-content">

<div id="report-section">
    <div id="report-list">

    <transition name="slide-fade">
    <ul v-if="!show" sid="report-data" class="nav">
      <form id="search-form" class="form-inline my-2 my-lg-0">
      <input class="form-control" id="input-search" type="search" placeholder="Search reports" aria-label="Search">
    </form>
    <p id="current-page">Page {{ pageNumber }} / {{ pagecount }}</p>
    <p id="of">of</p>
    <p id="report-quatitiy">{{ reports.length }} Reports</p>
    
    <div id="report-navigations">
    <svg v-on:click="prevPage" :disabled="pageNumber <= 0" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
    <svg v-on:click="nextPage" :disabled="pageNumber > pagecount" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
    </div>
    </ul>
    </transition>
    
<ul id="report-data" class="nav">
      <li class="nav-item">
<div id="report-arrow" v-if="show">
<transition name="slide-fade">
<div v-on:click="show=!show">
    <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
    back</div>
</transition>
</div>
</li>
</ul>

<transition name="slide-fade">
<table v-if="!show" class="table table-borderless">
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
    <tr v-on:click="show = !show; getIndex(index);" id="table-data" v-for="(report, index) in paginatedData" :key="report.id">
      <th scope="row"></th>
      <td id="offence-cell">{{ report["Offence"] }}</td>
      <td>{{ report["Victims-Firstname"] }} {{ report["Victims-Surname"] }}</td>
      <td>{{ report["Date-Time"].toDate() }}</td>
      <td></td>
    </tr>
  </tbody>
</table>
</transition>


</div>
<div id="user-selected">
    <transition name="slide-fade">
  <div id="view-report" v-if="show">
    <p id="offence">{{ reports[i]["Offence"] }}</p>
    <div id="offence-info">
    <p><span id="info-label">Reported by: </span>{{ reports[i]["Victims-Firstname"] }} {{ reports[i]["Victims-Middlename"]}} {{ reports[i]["Victims-Surname"]}}</p>
    <p><span id="info-label">Alias: </span>{{ reports[i]["Victims-Alias"] }}</p>
    <p><span id="info-label">Home Address: </span>{{ reports[i]["Victims-Home-Address"] }}</p>
    <p><span id="info-label">Occupation: </span>{{ reports[i]["Victims-Occupation"] }}</p>
    <p><span id="info-label">TRN: </span>{{ reports[i]["Victims-TRN"] }}</p>
    <p><span id="info-label">DOB: </span>{{ reports[i]["Victims-Date-of-Birth"] }}</p>
    <p><span id="info-label">Resident Status: </span>{{ reports[i]["Resident-Status"] }}</p>
    <p><span id="info-label">Email: </span>{{ reports[i]["Victims-Email"] }}</p>
    </div>
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
  props: {
    reportList: {
      type: Array,
      required: true
    },
    size: {
      type: Number,
      required: false,
      default: 1
    },
    pagecount: {
      type: Number,
      required: true
    },
    paginatedData: {
      type: Array,
      required: true
    }
  },
  components: { navbar },
  methods: {
    open (link) {
      this.$electron.shell.openExternal(link)
    },
    getIndex: function (index) {
        this.i.pop()
        this.i.push(index)
    },
    nextPage: function (){
         this.pageNumber++;
         this.count++
         let start = this.count * this.size
          let end = start + this.size;
          this.paginatedData = this.reportList.slice(start, end)
      },
    prevPage: function (){
        this.pageNumber--;
        this.count--
        let start = this.count * this.size
        let end = start + this.size;
        this.paginatedData = this.reportList.slice(start, end)
      },
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
      i: [],
      pageNumber: 1,
      count: 0
    }
  },
    created (){
      let report = db.collection("Crime Report").get()
        .then(snapshot => {
          snapshot.forEach(doc => {
            this.reports.push(doc.data());
            console.log(doc.data());
          });
          this.reportList = this.reports

          this.pagecount = Math.ceil(this.reports.length/this.size)

          let start = this.count * this.size
          let end = start + this.size;
          this.paginatedData = this.reportList.slice(start, end)
        })
        .catch(err => {
          console.log('Error getting documents', err);
        });
    },
}

</script>

<style>
.slide-fade-enter-active {
  transition: all 1s ease;
}
.slide-fade-leave-active {
  transition: all .000001s ease;
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}

#report-arrow {
    font-size: 12px;
}

#user-selected {
    margin-left: 50px;
}

tbody {
    background-color: white;
}

#report-data {
margin-bottom: 40px;
}

#offence-cell {
    font-weight: 600;
}

#info-label {
    font-weight: 600;
}

#offence-info {
    font-size: 12px;
    color: #566573;
    letter-spacing: 0.5px;
    font-weight: 400;
}

th {
    font-size: 12px;
    color: #5C6BC0;
}

td {
    font-size: 12px;
    color: #566573;
    letter-spacing: 0.5px;
    font-weight: 400;
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
}

#report-quatitiy {
    font-size: 12px;
    color: #566573;
    letter-spacing: 0.5px;
    font-weight: 400;
    margin-top: 14px;
    margin-right: 40px;
}

#current-page {
    font-size: 12px;
    color: #566573;
    letter-spacing: 0.5px;
    font-weight: 400;
    margin-top: 14px;
    margin-right: 10px;
}


#of {
  font-size: 12px;
    color: #566573;
    letter-spacing: 0.5px;
    font-weight: 400;
    margin-top: 14px;
    margin-right: 10px;
}

#report-navigations {
    margin-top: 8px;
}

#offence {
    font-size: 20px;
    letter-spacing: 0.5px;
    font-weight: 400;
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

#table-data:hover {
    background-color: #E8EAF6;
}

.dot {
  height: 40px;
  width: 40px;
  background-color: #9FA8DA;
  border-radius: 50%;
  display: inline-block;
  margin-top: 5px;
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

#notif, #account, .dot {
    margin-left: 20px;
    fill: #9FA8DA;
}

#notif {
  margin-top: 13px;
}

#page-nav {
    height: 50px;
    margin: 20px;
}

#report-label {
    font-size: 16px;
    margin-top: 30px;
    margin-left: 17px;
}
</style>