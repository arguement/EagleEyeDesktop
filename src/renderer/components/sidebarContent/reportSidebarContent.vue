<template>
  <div id="reports-sidebar-content">
    <router-view></router-view>
    
<!-- NAVBAR -->    
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
          <span class="dot"><div id="user-initials">{{ storeState.user["first-name"].charAt(0) }}{{ storeState.user["surname"].charAt(0) }}</div></span>
          </li>   
        </ul>
      </div>
    </nav>

    <div id="reports-content">
      <div id="report-section">
        <div id="report-list">

<!-- REPORT LIST NAV SECTION -->
          <transition name="slide-fade">
            <ul v-if="!show" id="report-data" class="nav">
              <ul class="nav navbar-nav mr-auto">
                <form id="search-form" class="form-inline my-2 my-lg-0">
                  <input class="form-control" id="input-search" type="search" placeholder="Find reports" aria-label="Search">
                </form>
              </ul>
              <p id="current-page">Page {{ pageNumber }} / {{ pagecount }}</p>
              <p id="of">of</p>
              <p id="report-quatitiy">{{ reports.length }} Reports</p>
          
              <div id="report-navigations">
                <svg v-on:click="prevPage" :disabled="pageNumber <= 0" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                <svg v-on:click="nextPage" :disabled="pageNumber > pagecount" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
              </div>
            </ul>
          </transition>

          
<!-- REPORT DETAILS NAV SECTION --> 
<transition name="slide-fade">
  <div id="report-arrow" v-if="show">
          <ul id="report-data" class="nav">
            <li v-on:click="show=!show" class="nav-item">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                    back              
            </li>
            <li v-on:click="dispatch()" id="add-officer" class="nav-item">
              <div id="add-user" class="btn btn-outline-primary">
                <svg id="user-add-button"xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 0 24 24" width="20"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                Officer
              </div>
            </li>
          </ul>
          </div>
          </transition>

<!-- REPORT LIST -->
          <transition name="slide-fade">
            <table v-if="!show" class="table table-borderless" style="border-collapse:separate; border-spacing:0 3px; margin-top:-3px;">
              <thead>
                <tr>
                  <th scope="col"></th>
                  <th scope="col">Crime</th>
                  <th scope="col">Priority</th>
                  <th scope="col">Name</th>
                  <th scope="col">Date</th>
                  <th scope="col">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr id="table-data" v-for="(report, index) in paginatedData" :key="report.id">
                  <th v-on:click="show = !show;" scope="row">
                    <div  class="form-group form-check">
                      <input v-on:click="showNav = false" type="checkbox" class="form-check-input" id="exampleCheck1">
                    </div>
                  </th>
                  <td v-on:click="show = !show; getIndex(index); getReport(report)" id="offence-cell">{{ report[1]["offence"] }}</td>
                  <td v-on:click="show = !show; getIndex(index); getReport(report)" >{{ report[1]["priority"] }}</td>
                  <td v-on:click="show = !show; getIndex(index); getReport(report)">{{ report[1]["first-name"] }} {{ report[1]["surname"] }}</td>
                  <td v-on:click="show = !show; getIndex(index); getReport(report)">{{ report[1]["date-time-reported"].toDate() }}</td>
                  <td v-on:click="show = !show; getIndex(index); getReport(report)">{{ report[1]["status"] }}</td>
                  
                </tr>
              </tbody>
            </table>
          </transition>
        </div>

        <div id="user-selected">
            <transition name="slide-fade">
              <div id="view-report" v-if="show">
                <div id="report-title">
                  <div>
                    <p id="offence" class="report-title1">{{ paginatedData[1][i]["offence"] }}</p>
                    <p id="offence-info">Status: {{ paginatedData[1][i]["status"] }}</p>
                  </div>
                  <p id="offence-info" class="report-title2">{{ paginatedData[1][i]["date-time-reported"].toDate() }}</p> 
                </div>


      <!-- PERSONAL INFORMAION -->
                <p id="offence1">Victim's Personal Information</p>
                <p id="offence-info">Name: {{ paginatedData[1][i]["first-name"] }} {{ paginatedData[1][i]["middle-name"] }} {{ paginatedData[1][i]["surname"] }}</p>
                <p id="offence-info">Alias: {{ paginatedData[1][i]["alias"] }}</p>
                <p id="offence-info">Maiden Name: {{ paginatedData[1][i]["maiden-name"] }}</p>
                <p id="offence-info">Occupation: {{ paginatedData[1][i]["occupation"] }}</p>
                <p id="offence-info">TRN: {{ paginatedData[1][i]["trn"] }}</p>
                <p id="offence-info">Home Address: {{ paginatedData[1][i]["home-address"] }}</p>
                <p id="offence-info">Place of Work: {{ paginatedData[1][i]["job-name"] }}</p>
                <p id="offence-info">Work Address: {{ paginatedData[1][i]["job-address"] }}</p>
                <p id="offence-info">Email: {{ paginatedData[1][i]["email"] }}</p>
                <p id="offence-info">Home: {{ paginatedData[1][i]["home-number"] }}</p>
                <p id="offence-info">Cell: {{ paginatedData[1][i]["cell-number"] }}</p>
                <p id="offence-info">Gender: {{ paginatedData[1][i]["gender"] }}</p>
                <p id="offence-info">DOB: {{ paginatedData[1][i]["birth-date"].toDate() }}</p>
                <p id="offence-info">Nationality: {{ paginatedData[1][i]["nationality"] }}</p>
                <p id="offence-info">Reapeat Victim: {{ paginatedData[1][i]["repeat-victim"] }}</p>
                <p id="offence-info">Resident Status: {{ paginatedData[1][i]["resident-status"] }}</p>
      
      <!-- OFFENCE INFORMATION -->
                <p id="offence1">Offence Information</p>
                <p id="offence-info">Location of Offence: {{ paginatedData[1][i]["offence-location"] }}</p>
                <p id="offence-info">Time/Date Commited: {{ paginatedData[1][i]["date-time-commited"].toDate() }}</p>
                <p id="offence-info">Description of Offence Location: {{ paginatedData[1][i]["offence-location-description"] }}</p>
                <p id="offence-info">Lighting/weather conditions: {{ paginatedData[1][i]["lighting-weather-conditions"] }}</p>
                <p id="offence-info">Offence Description: {{ paginatedData[1][i]["offence-description"] }}</p>
                <p id="offence-info">Property Stolen: {{ paginatedData[1][i]["property-stolen"] }}</p>
                <p id="offence-info">Description of Offenders: {{ paginatedData[1][i]["offender-description"] }}</p>
                <p id="offence-info">Firearms seized: {{ paginatedData[1][i]["firearms"] }}</p>
                <p id="offence-info">Ammunition seized: {{ paginatedData[1][i]["ammunition"] }}</p>
                <p id="offence-info">Drugs seized: {{ paginatedData[1][i]["drugs"] }}</p>
                <p id="offence-info">Weapons: {{ paginatedData[1][i]["weapon"] }}</p>
              </div>
            </transition>
          </div>
        </div>

    </div>
  </div>
</template>

<script>
import {store} from "../../store/store"
import navbar from '../navbar/navbar'
import {db} from '../../../../static/js/fire_config' 
import {realref} from '../../../../static/js/fire_config' 


      
export default {
  props: {
    /* reportList: {
      type: Array,
      required: true
    }, */
    /* size: {
      type: Number,
      required: false,
      default: 10
    }, */
    /* pagecount: {
      type: Number,
      required: true
    } *//* ,
    paginatedData: {
      type: Array,
      required: true
    } */
  },
  components: { navbar },
  methods: {
    open (link) {
      this.$electron.shell.openExternal(link)
    },
    getReport: function (report) {
     // this.reportClicked = report
    },

    dispatch: function () {
      let report = this.reportClicked
      this.$router.push({ name: "dispatch", query: {reportClicked: report} })
    },


    // GETS INDEX OF REPORT
    getIndex: function (index) {
        this.i.pop()
        this.i.push(index)
    },
    
    // FORWARD ARROW NAV
    nextPage: function (){
      if (this.pageNumber < this.pagecount) {
         this.pageNumber++;
         this.count++
         let start = this.count * this.size
          let end = start + this.size;
          this.paginatedData = this.reportList.slice(start, end)
      } else {
        this.pageNumber = this.pageNumber
      }
      },

     // BACK ARROW NAV 
    prevPage: function (){
      if (this.pageNumber > 1) {
        this.pageNumber--;
        this.count--
        let start = this.count * this.size
        let end = start + this.size;
        this.paginatedData = this.reportList.slice(start, end)
      } else {
        this.pageNumber = this.pageNumber
      }
    } ,
    /*dispatchofficer(){
      //console.log(this.selectofficer)
      let reportref=db.collection('Crime Report').doc(this.fullinfo[i].id) 
      //console.log(this.fullinfo[i].id) 
      let setwithmerge = reportref.set({
        status: "Officer Dispatched"
      },{merge:true})
      this.$router.push({ path:"/dispatch"})
    },*/
    //STORE USER IN STATE
    

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
      pageNumber: 1,
      count: 0,
      i: [],
      storeState: store.state,
      reportList: [],
      paginatedData:[],
      size: 10,
      pagecount: 0,
      officers:[],
      
      fullinfo:[],
      priorities:[],
      specificprioritiea:[],
      reportClicked: []

    }
  },
    created (){  


      db.collection('Crime Priorities').get().then(
          querysnapshot => {
          querysnapshot.forEach (doc => {
          this.priorities.push(doc.data())
          }); 
          //console.log(this.priorities) 
          })
      
      db.collection("Crime Report").get()
        .then(snapshot => {
          snapshot.forEach(doc => {
            this.reports.push([doc.id, doc.data()]);
            //console.log(doc.data());
            this.fullinfo.push(doc)
          }); 
          
        
          
          for (let index = 0; index < this.reports.length; index++) {
            let reportArray = this.reports[index][1];
            if (!("weapons" in reportArray)) {
              reportArray["weapons"] = "N/A"
            }
            if (!("drugs" in reportArray)) {
              reportArray["drugs"] = "N/A"
            }
            if (!("ammunition" in reportArray)) {
              reportArray["ammunition"] = "N/A"
            }
            if (!("firearms" in reportArray)) {
              reportArray["firearms"] = "N/A"
            }
            if (!("offender-description" in reportArray)) {
              reportArray["offender-description"] = "N/A"
            }
            if (!("property-stolen" in reportArray)){
              reportArray["property-stolen"] = "N/A"
            }
            if (!("offence-description" in reportArray)) {
              reportArray["offence-description"] = "N/A"
            }
            if (!("lighting-weather-conditions" in reportArray)) {
              reportArray["lighting-weather-conditions"] = "N/A"
            }
            if (!("offence-location-description" in reportArray)) {
              reportArray["offence-location-description"] = "N/A"
            }
            if (!("date-time-commited" in reportArray)) {
              reportArray["date-time-commited"] = "N/A"
            }
            if (!("offence-location" in reportArray)) {
              reportArray["offence-location"] = "N/A"
            }
            if (!("resident-status" in reportArray)) {
              reportArray["resident-status"] = "N/A"
            }
            if (!("repeat-victim" in reportArray)) {
              reportArray["repeat-victim"] = "N/A"
            }
            if (!("nationality" in reportArray)) {
              reportArray["nationality"] = "N/A"
            }
            if (!("birth-date" in reportArray)) {
              reportArray["birth-date"] = "N/A"
            }
            if (!("gender" in reportArray)) {
              reportArray["gender"] = "N/A"
            }
            if (!("cell-number" in reportArray)) {
              reportArray["cell-number"] = "N/A"
            }
            if (!("home-number" in reportArray)) {
              reportArray["home-number"] = "N/A"
            }
            if (!("email" in reportArray)) {
              reportArray["email"] = "N/A"
            }
            if (!("job-address" in reportArray)) {
              reportArray["job-address"] = "N/A"
            }
            if (!("job-name" in reportArray)) {
              reportArray["job-name"] = "N/A"
            }
            if (!("home-address" in reportArray)) {
              reportArray["home-address"] = "N/A"
            }
            if (!("trn" in reportArray)) {
              reportArray["trn"] = "N/A"
            }
            if (!("occupation" in reportArray)) {
              reportArray["occupation"] = "N/A"
            }
            if (!("maiden-name" in reportArray)) {
              reportArray["maiden-name"] = "N/A"
            }
            if (!("alias" in reportArray)) {
              reportArray["alias"] = "N/A"
            }
            if (!("first-name" in reportArray)) {
              reportArray["first-name"] = "N/A"
            }
            if (!("middle-name" in reportArray)) {
              reportArray["middle-name"] = "N/A"
            }
            if (!("surname" in reportArray)) {
              reportArray["surname"] = "N/A"
            }
          }
           for (let i=0;i < this.reports.length;i++){ 
            //console.log(Object.keys(this.priorities[0]))
            let prioritiesobjects=Object.keys(this.priorities[0])
            let offence=(this.reports[i][1].offence).toLowerCase()
            let tester=prioritiesobjects.includes(offence)
            //console.log(offence)
            //console.log(tester)
            if ( tester = true){
              let priorities=this.priorities[0][offence]
              console.log(priorities) 
              this.reports[i][1].priority=priorities
            }
           } 
           
          this.reports.sort(function(a,b){return b.priority-a.priority})
          this.reportList = this.reports
          this.pagecount = Math.ceil(this.reports.length/this.size)

          let start = this.count * this.size
          let end = start + this.size;
          this.paginatedData = this.reportList.slice(start, end)

        })
        .catch(err => {
          console.log('Error getting documents', err);
        });   
         
     
       setInterval(() => {
         console.log("test")
       },6100);
       
    },
  }


 

</script>

<style>
#add-officer {
  margin-left: 50px;
}

#flag, #close, #dispatch, #ongoing {
    font-size: 12px;
    fill: #566573;
    color: #566573;
    letter-spacing: 1px;
    margin-top: 2px;
}


input[type="checkbox"] {
  outline:1px solid #D5D8DC  ;
    outline-offset: -1px;
}
#user-selected {
  position: relative;
}
.report-title2 {
  position: absolute;
  right: 0;
}
#report-title {
  position: relative;
  display: flex;
  flex-direction: row;
}

#view-report {
  margin-bottom: 100px;
}
#refresh {
  margin-top: 11px;
  margin-left: 20px;
  fill: #566573;
}
.slide-fade-enter-active {
  transition: all 1s ease;
}
.slide-fade-leave-active {
  transition: all .000001s ease;
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave- active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
#report-arrow {
    font-size: 12px;
    fill: #566573;
    color: #566573;
    letter-spacing: 1px;
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
    letter-spacing: 1px;
    font-weight: 400;
}
th {
    font-size: 12px;
    color: #5C6BC0;
    letter-spacing: 1px;
}
td {
    font-size: 12px;
    color: #566573;
    letter-spacing: 1px;
    font-weight: 400;
}
#reports-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
  margin-left: 230px
}
#reports-content {
    margin-left: 50px;
    margin-right: 50px;
    margin-top: 60px;
}
#input-search {
  border: none;
  border-radius: 4px;
  background: #E5E7E9;
  height: 40px;
  font-size: 12px;
  letter-spacing: 1px;
  font-weight: 400;
  width: 100%;
  color: #85929E;
}
#reports-label {
    font-size: 16px;
}
#report-quatitiy {
    font-size: 12px;
    color: #566573;
    letter-spacing: 1px;
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
    letter-spacing: 1px;
    font-weight: 400;
    margin-top: 14px;
    margin-right: 10px;
}
#report-navigations {
    margin-top: 8px;
    fill: #566573;
}
#offence {
    font-size: 20px;
    letter-spacing: 0.5px;
    font-weight: 400;
}
#offence1 {
    font-size: 15px;
    letter-spacing: 0.5px;
    font-weight: 400;
    margin-top: 50px;
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
  font-weight: 400;
  letter-spacing: 1px;
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
    margin-right: 50px;
    margin-left: 50px;
    letter-spacing: 1px;
}
#report-label {
    font-size: 16px;
    margin-top: 30px;
    letter-spacing: 2px;
    font-weight: 300px;
  }
</style>