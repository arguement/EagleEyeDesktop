<template>
  <div id="home-sidebar-content">
    <router-view></router-view>
    
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
        <span class="dot"><div id="user-initials">JD</div></span>  
      </li>   
    </ul>
    </div>
</nav>


<p>  {{ inputId }} </p>
<p>  {{ userList }} </p>
<p>  {{ User }} </p>


  </div>
</template>

<script>
import {db} from '../../../../static/js/fire_config'
export default {
  props: {
    inputId: {
      type: String,
      required: true
    },
    User: {
      type: Array,
      required: true
    },
    userList: {
      type: Array,
      required: true
    }
  },
  methods: {
    open (link) {
      this.$electron.shell.openExternal(link)
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
      users: []
    }
  },
  created (){
    this.inputId = this.$route.params.userId

    let user = db.collection("User").get()
      .then(snapshot => {
        snapshot.forEach(doc => {
          this.users.push(doc.data());
          console.log(doc.data());
        });
        this.userList = this.users
        
        let allUsers = this.userList
        for (let index = 0; index < allUsers.length; index++) {
          let userId = this.userList[index]["id-number"];
          if (this.inputId == userId) {
            this.User = userList[index]
          }
        }
        
        })
        .catch(err => {
          console.log('Error getting documents', err);
        });
    }
}
</script>

<style>
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
  height: 100vh;
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


</style>