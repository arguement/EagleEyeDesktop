<template>
  <div id="home-sidebar-content" v-if="!loading">
    <router-view></router-view>

    <div id="loader" v-if="spinner.loading">
      <scale-loader  :loading="spinner.loading" :color="spinner.color" :size="spinner.size" ></scale-loader>
    </div>
    
<!-- NAVBAR -->
    <div id="conditional-render" v-else>
      <nav id="page-nav" class="navbar navbar-expand-lg navbar-light bg-light">
          <li class="navbar-brand">
            <h1 id="dashboard-label">DASHBOARD</h1>
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
  
  <!-- DASHBOARD CONTENT -->    
  <h1 id="welcome-name">Hello {{ storeState.user["first-name"] }}</h1>
  
  
  
  <div class="grid-container" >
  
      <!-- <div>
  
        <div class="card">
          <div class="card-body">
            {{allData.card_data.pending_count}}
          </div>
        </div>
  
        <div class="card">
          <div class="card-body">
            {{allData.card_data.dispatch_count}}
          </div>
        </div>
  
        <div class="card">
          <div class="card-body">
            {{allData.card_data.total_count}}
          </div>
        </div>
        
      </div> -->
  
  
      <!-- <div id="bar">
        <bar-chart :chart-data="chartdata" :options="options"></bar-chart>
      </div>
      <div id="pie">
        <pie-chart :chart-data="chartdata" :options="options"></pie-chart>
      </div> -->
  
      <div class="item-a">
        <h4> Overall </h4>
        <div class="flex-center-align" >
    
          <div class="card " style="width: 8rem;height: 6rem;">
            <div class="card-body flex-center">
             <p class="card-text">
                {{allData.card_data.pending_count}}
              </p>
              <p class="card-foot">Pending Crimes</p>
            </div>
          </div>
    
          <div class="card" style="width: 8rem;height: 6rem;">
            <div class="card-body flex-center">
              <p class="card-text">
                {{allData.card_data.dispatch_count}}
              </p>
              <p class="card-foot">Dispatches Crimes</p>
            </div>
          </div>
    
          <!-- <div class="card" style="width: 8rem;height: 6rem;">
            <div class="card-body flex-center">
              <p class="card-text">
                {{allData.card_data.total_count}}
              </p>
              <p class="card-foot">Total Crimes</p>
            </div>
          </div> -->
    
          <div class="card" style="width: 8rem;height: 6rem;">
            <div class="card-body flex-center">
              <p class="card-text">
                {{allData.card_data.closed_count}}
              </p>
              <p class="card-foot">Closed</p>
            </div>
          </div>
          
        </div>
      </div>

      <div class="item-e">
        <h4> Within 30 days</h4>
        <div class="flex-center-align " >
  
          <!-- <h1>Within 30 days</h1> -->
    
          <div class="card " style="width: 8rem;height: 6rem;">
            <div class="card-body flex-center">
             <p class="card-text">
                {{allData.card_data_30.pending_count}}
              </p>
              <p class="card-foot">Pending Crimes</p>
            </div>
          </div>
    
          <div class="card" style="width: 8rem;height: 6rem;">
            <div class="card-body flex-center">
              <p class="card-text">
                {{allData.card_data_30.dispatch_count}}
              </p>
              <p class="card-foot">Dispatches Crimes</p>
            </div>
          </div>
    
          <!-- <div class="card" style="width: 8rem;height: 6rem;">
            <div class="card-body flex-center">
              <p class="card-text">
                {{allData.card_data.total_count}}
              </p>
              <p class="card-foot">Total Crimes</p>
            </div>
          </div> -->
    
          <div class="card" style="width: 8rem;height: 6rem;">
            <div class="card-body flex-center">
              <p class="card-text">
                {{allData.card_data_30.closed_count}}
              </p>
              <p class="card-foot">Closed</p>
            </div>
          </div>
          
        </div>
      </div>
  
      <div style="max-width: 600px;height: auto;" class="item-b">
        <!-- <pie-chart :data="mostReportedCrimesData" :options="mostReportedCrimesOptions" ></pie-chart> -->
        <bar-chart :chart-data="mostReportedCrimesData" :options="mostReportedCrimesOptions"></bar-chart>
      </div>
  
      <div class="item-c">
  
        <h2>Parishes with The Most Crimes</h2>
        <div>
          <ul class="columns">
            <li v-for="item in allData.locations_with_most_crime" :key="item['offence-location']">
             {{item['offence-location']}} <span>{{item['offence count']}} </span>
            </li>
            
           
          </ul>
        </div>
        
      </div> 
  
      <div class="item-d">
        <line-chart :chart-data="reportsIn30DaysData" :options="reportsIn30DaysOptions"></line-chart>
      </div>
  
      
  
  </div>
    </div>

</div>
</template>

<script>
import {store} from "../../store/store"
import {db} from '../../../../static/js/fire_config'
import PieChart from "../charts/PieChart.js";
import BarChart from "../charts/BarChart.js";
import LineChart from "../charts/LineChart.js";
import ScaleLoader from 'vue-spinner/src/ScaleLoader'

export default {
  components: {
      BarChart,
      PieChart,
      LineChart,
      ScaleLoader
    },
  data () {
    return {
      electron: process.versions.electron,
      name: this.$route.name,
      node: process.versions.node,
      path: this.$route.path,
      platform: require('os').platform(),
      vue: require('vue/package.json').version,
      user: [],
      storeState: store.state,
      loading: false,
      allData: {},
      mostReportedCrimesData: {},
      mostReportedCrimesOptions:{},
      reportsIn30DaysData :{},
      reportsIn30DaysOptions :{},
      spinner:{
        loading: true,
        size: "200px",
        color: "#9FA8DA"
        },
    }
  },
  created(){
    fetch('http://localhost:8081/dashboard', {
      method: 'GET',
      mode: 'cors'
    })
    .then(response => response.json())
    .then(data => {
      // console.log('Success:', data);
      this.allData = data;
      console.log("from fetch")
      console.log(this.allData)
    }).then(()=>{
      this.fillMostReportedCrimes()
      this.fillReportsIn30Days()
      
    }).then(()=>{
      this.spinner.loading = false;
    })
  },
  mounted () {
    
    if (this.$route.query.id){
      this.loading = true;
    db.collection("User").where
    ('id-number','==',this.$route.query.id).get()
      .then(snapshot => {
        snapshot.forEach(doc => {
          this.user.push(doc.data());
          // console.log(doc.data());
        });
        //Add user info to AddUser method
        this.addUser(this.user[0])
        
        }).then(()=>{
          this.loading = false
           
          })
        .catch(err => {
          console.log('Error getting documents', err);
        });
    }
    },
  methods: {
    open (link) {
      this.$electron.shell.openExternal(link)
    },
    
    //STORE USER IN STATE
    addUser(user) {
      store.addUser(user)
      // store.commit("changeUser", user)
    },
    fillMostReportedCrimes(){
     
      const data_values = Object.values(this.allData["top3crimes"])
      // console.log(`values ${data_values }`)
      const data_keys = Object.keys(this.allData["top3crimes"])
      // console.log(`values ${data_keys }`)
      // console.log(typeof(data_values))
      // console.log(typeof(data_keys))
      let a = {
        
      hoverBackgroundColor: "red",
        hoverBorderWidth: 10,
        labels: data_keys,
        datasets: [
          {
            label: "Data One",
            backgroundColor: "#00D8FF",
            data: data_values 
          }
        ]
      }
      let b = {
         responsive: true,
        maintainAspectRatio: false,
        title:{
          display: true,
          text: "Most Reported Crimes",
          fontSize: 25
      },
      scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
    }
      }
      this.mostReportedCrimesData = a
      this.mostReportedCrimesOptions = b
      // console.log("function")
      // console.log(this.mostReportedCrimesData)
    },
    fillReportsIn30Days(){
      let data = []
      this.allData.crime30days.forEach((e,i)=>{

        data.push({x:e["date-time-reported"], y:e["offence count"] })
      })

      let chartData = {

        datasets: [{
					label: 'Last 30 days',
          backgroundColor: "#2196F3",
          data: data
        }]
        
      }

      let options = {
        title:{
          display: true,
          text: "Crimes in the last 30 days",
          fontSize: 25
      },
        scales:{
          xAxes: [{
            type: 'time',
            distribution: "series"
          }]
        }
      }
      this.reportsIn30DaysData = chartData;
      this.reportsIn30DaysOptions = options;
    }
  }
}
</script>

<style>
#welcome-name {
  margin-left: 60px;
  letter-spacing: 2px;
}

#welcome-user {
  letter-spacing: 1px;
  font-weight: 300px;
  font-size: 36px;
  margin-top: 50px;
}

#notif:hover{
  fill: #7986CB;
}

.dot:hover {
  background-color: #7986CB;
}

#home-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  /* height: 100vh; */
  height: 100%;
  margin-left: 230px
}

#dashboard-content {
  margin-left: 50px;
  margin-right: 20px;
  margin-top: 60px;
}

#dashboard-label {
    font-size: 16px;
    margin-top: 30px;
    letter-spacing: 2px;
    font-weight: 300px;
}

.flex-center {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.flex-center-align {
  display: flex;
  justify-content: center;
 
}

.flex-center p {
  
}

ul.columns{
  columns: 2;
  list-style-type: none;
}
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
  gap: 1px 1px;
  justify-items: center;
  align-items: center;
  
}

.item-a {
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 2;
  /* place-self: stretch; */
}
.item-b {
  grid-column-start: 3;
  grid-column-end: 5;
  grid-row-start: 1;
  grid-row-end: 3;
}
.item-c {
  grid-column-start: 3;
  grid-column-end: 5;
  grid-row-start: 3;
  grid-row-end: 5;
}
.item-d {
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 2;
  grid-row-end: 6;
}

.item-e{

  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 2;
  grid-row-end: 3;
  /* place-self: stretch; */

}

.flex-center p:first-child{
 font-weight: bold;
 margin: 0;
}

.item-a,.item-e h4{
  text-align: center;
}

</style>