<template>
  <div id="analytics-sidebar-content">
    <router-view></router-view>
    
    <nav id="page-nav" class="navbar navbar-expand-lg navbar-light bg-light">
        <li class="navbar-brand">
        <h1 id="dashboard-label">ANALYTICS</h1>
      </li>
    <div id="navbar-icons">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
          <svg id="notif" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg>
        </li>
      <li class="nav-item">
        <span class="dot"><div id="user-initials">{{ storeState.user["first-name"].charAt(0) }}{{ storeState.user["surname"].charAt(0)}}</div></span>  
      </li>   
    </ul>
    </div>
</nav>


  <div id= "charts">

    <div id="bar">
      <bar-chart :chart-data="chartdata" :options="options"></bar-chart>
    </div>

    <div id="cluster">

      <scatter-chart :chart-data="clusterData" :options="clusterChartOptions"></scatter-chart>

    </div>

    <div id="crime_in_area">
      <bar-chart :chart-data="crimeLocationStackedBar" :options="options"></bar-chart>
    </div>

    <div id="crime_in_area">
      <bar-chart :chart-data="prioritiesData" :options="optionsPrioritiesData"></bar-chart>
    </div>

  </div>

    

  </div>
</template>

<script>
import {store} from "../../store/store"
import {db} from '../../../../static/js/fire_config'
import BarChart from "../charts/BarChart.js";
import ScatterChart from "../charts/ScatterChart";


export default {
  components: {
      BarChart,
      ScatterChart
    },
  data () {
    return {
      colors: ["#F44336","#9C27B0","#673AB7","#2196F3","#00BCD4","#FFEB3B","#FF5722","#607D8B"],
      options:{},
      chartdata: {},
      storeState: store.state,
      allData: {},
      clusterData:{},
      clusterChartOptions:{},
      crimeLocationStackedBar: {},
      optionsCrimeLocationStackedBar: {},
      priorities: {},
      prioritiesData:{},
      optionsPrioritiesData:{},
      
    }
  },
  created(){
    fetch('http://localhost:8081/CrimeAnalytics?orientCluster=records', {
      method: 'GET',
      mode: 'cors'
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      this.allData = data;
    }).then(()=>{
      this.fillDataOverallCounts()
      this.fillDataCluster()
      this.fillCrimeLocationStackedBar();


          fetch('http://localhost:8081/allPriority', {
          method: 'GET',
          mode: 'cors'
          }).
          then(response => response.json())
          .then(({priorities}) => {
            console.log('Success2:', priorities);
            this.priorities = priorities;
          }).then(()=>{
            this.fillPrioritiesData()
          })
    })
    .catch((error) => {
      console.error('Error:', error);
    });

  },
  methods:{
   fillDataOverallCounts(){
    
    const {over_counts} = this.allData;
    let labs = Object.keys(over_counts);
    this.chartdata = {
      labels: labs,
      datasets: [
        {
          label: 'Overall Crime Counts',
          backgroundColor: '#f87979',
          data: Object.values(over_counts)
        }
      ]
    }
    this.options = {
      responsive: true,
      maintainAspectRatio: false,
      title:{
        display: true,
        text: "Overall Crime Counts",
        fontSize: 25
      }
    }
    console.log(this.scatter)
    
  },
  fillDataCluster(){
   
    
    const x_axis = "Assault"
    const y_axis = "Total"
    let store = Object.entries(this.xyScatter("Assault","Total"))
   
    let datasets = []
    store.forEach((el)=>{
      let col = this.colors.pop()
      let obj = {
        label: ""+el[0],
        data: el[1],
        pointBackgroundColor: col,
        backgroundColor: col
      }
      datasets.push(obj)
    })

    this.clusterData= {
      
      datasets
    }
    
    

    this.clusterChartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      title:{
        display: true,
        text: `Cluster Data ${x_axis} vs ${y_axis}`,
        fontSize: 25
      },
      scales: {
              yAxes: [{
                scaleLabel: {
                  display: true,
                  labelString: y_axis
                }
              }],
              xAxes: [{
                scaleLabel: {
                  display: true,
                  labelString: x_axis
                }
              }]
        }    
    }
  },
  xyScatter(xName,yName){

    const {"overall_tables":clustersTable} = this.allData;
    
    let clusters = {}

    clustersTable.forEach((el)=>{

      const {"Crime_clusters":numCluster} = el;
      if (numCluster in clusters == false) clusters[numCluster] = [];
    })
    

    clustersTable.forEach((el)=>{
      
      let {"Crime_clusters":numCluster,[xName]:x,[yName]:y} = el;
      clusters[numCluster].push({x,y})

    })

    return clusters

  },
  fillCrimeLocationStackedBar(){
    const {"overall_tables":clustersTable,offences,locations} = this.allData;

    const location = {}
    const store = []

    

        for (const off of offences) {
          const temp = []
          clustersTable.forEach((e)=>{
            
            
            const {[off]:offval} = e;
            temp.push(offval);

          })
          store.push(temp)
          
        }


    let datasets = []
    store.forEach((el,i)=>{
      let col = this.colors.pop()
      let obj = {
        label: ""+locations[i],
        data: el,
        pointBackgroundColor: col,
        backgroundColor: col
      }
      datasets.push(obj)
    })    

    this.crimeLocationStackedBar = {
      labels: locations,
      datasets
    }

    this.optionsCrimeLocationStackedBar = {
      title: {
						display: true,
						text: 'Crimes by location'
					},
					tooltips: {
						mode: 'index',
						intersect: false
					},
					responsive: true,
					scales: {
						x: {
							stacked: true,
						},
						y: {
							stacked: true
						}
					}
    }

  },
  fillPrioritiesData(){
    const labs = Object.keys(this.priorities)
    const data = Object.values(this.priorities);

    this.prioritiesData = {
      labels: labs,
      datasets: [
        {
          label: "Priorities",
          backgroundColor: this.colors[5],
          data: data
        }
      ]
    }
    this.optionsPrioritiesData = {
      responsive: true,
      maintainAspectRatio: false,
      title:{
        display: true,
        text: "Priorites",
        fontSize: 25
      }
    }
  }

  }
}
</script>

<style>
#analytics-sidebar-content {
  background-color: #F8F9F9;
  width: 100%;
  height: 100vh;
  margin-left: 230px
}

#charts{
  display: flex;
}

#charts div{
  width: 100%;
  max-width: 600px;
  height: auto;
  
}
</style>