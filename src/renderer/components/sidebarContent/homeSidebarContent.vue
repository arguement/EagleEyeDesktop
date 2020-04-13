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
        <span class="dot"><div id="user-initials">{{ storeState.User["first-name"].charAt(0) }}{{ storeState.User["surname"].charAt(0) }}</div></span>  
      </li>   
    </ul>
    </div>
</nav>
<h1 id="welcome-name">Hello {{ storeState.User["first-name"] }}</h1>


  </div>
</template>

<script>
import {store} from "../../store/store"
import {db} from '../../../../static/js/fire_config'
export default {
  props: {
    userList: {
      type: Array,
      required: true
    }
  },
  methods: {
    open (link) {
      this.$electron.shell.openExternal(link)
    },
    addIndex(Index) {
      store.addIndex(Index)
    },
    addUser(User) {
      store.addUser(User)
      store.commit("changeUser", User)
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
      users: [],
      loaded: true,
      storeState: store.state,
      Index: [],
      User: []
    }
  },
  created () {
    this.Index = this.$route.query.userIndex

    let user = db.collection("User").get()
      .then(snapshot => {
        snapshot.forEach(doc => {
          this.users.push(doc.data());
          console.log(doc.data());
        });
        this.userList = this.users
        
        this.addIndex(this.Index)
        this.User = this.userList[this.Index]
        this.addUser(this.User)
        })
        .catch(err => {
          console.log('Error getting documents', err);
        });
    },
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
  height: 100vh;
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


</style>