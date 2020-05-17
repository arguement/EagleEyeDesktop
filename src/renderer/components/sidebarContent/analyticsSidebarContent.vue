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
      options:{},
      chartdata: {},
      storeState: store.state,
      allData: {},
      clusterData:{},
      clusterChartOptions:{}
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

    
  },
  fillDataCluster(){
    // const {"overall_tables":clustersTable} = this.allData;

    // console.log(clustersTable);
    
    // const temp = [ /* Object.keys(clustersTable[0]) */["crimeClusters","Assault","Total"]  ];

    // console.log(temp);
    // console.log(clustersTable.length)
    // clustersTable.length >= 2 &&
    // clustersTable.forEach((val)=>{
    //   // let json_to_list  = Object.values(val);
    //   const {Assault,Total,"Crime_clusters":crimeClusters} = val
    //   let json_to_list = [crimeClusters.toString(),Assault,Total]
    //   temp.push(json_to_list);
    // })
    // console.log(temp)
    // this.clusterData = temp;

    // this.clusterChartOptions= {
    //     chart: {
    //       title: 'Cluster ',
    //       // subtitle: 'Sales, Expenses, and Profit: 2014-2017',
    //       hAxis: {title: 'Assault'},
    //       vAxis: {title: 'Crime_clusters'}
    //     }
    //   }
    const {"overall_tables":clustersTable} = this.allData;
    let store = []
    let clusters = {}

    clustersTable.forEach((el)=>{

      const {"Crime_clusters":numCluster} = el;
      if (numCluster in clusters == false) clusters[numCluster] = [];
    })
    

    clustersTable.forEach((el)=>{
      
      let {"Crime_clusters":numCluster,Assault:x,Total:y} = el;
      clusters[numCluster].push({x,y})

    })

    store = Object.entries(clusters)
   
    let datasets = []
    store.forEach((el)=>{
      let obj = {
        label: ""+el[0],
        data: el[1]
      }
      datasets.push(obj)
    })

    this.clusterData= {
      
      datasets
    }
    console.log(this.clusterData)

    this.clusterChartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      title:{
        display: true,
        text: "Cluster",
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