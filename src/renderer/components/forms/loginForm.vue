<template>
  <div>
    <router-view></router-view>

<!-- NAVBAR -->
    <nav id="login-nav" class="navbar navbar-expand-lg navbar-light bg-light">
      <li id="logo-stuff" class="navbar-brand">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="18px" height="18px"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 4C7 4 2.73 7.11 1 11.5 2.73 15.89 7 19 12 19s9.27-3.11 11-7.5C21.27 7.11 17 4 12 4zm0 12.5c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
        <h1 id="logo-eye">EAGLE EYE</h1>
      </li>
    </nav>

<!-- LOGIN FORM -->
    <div id="login-form">
      <form class="login">
        <h1 id="welcome">WELCOME</h1>
        <h1 id="login-form-label">Log in to get access to your account. Your activity is also being monitored.</h1>
        <div class="form-group">
          <label class="label" for="exampleInputId1">ID NUMBER <div class="errors">{{ idErrors }}</div> </label>
          <input v-model="input.id" type="id" class="form-control" id="input-id">
        </div>
        <div class="form-group">
          <label class="label" for="exampleInputPassword1">PASSWORD <div class="errors">{{ passwordErrors }}</div> </label>
          <input  v-model="input.password" type="password" class="form-control" id="input-password">
        </div>
        <button v-on:click="login()" type="submit" class="btn btn-primary" id="login-button" >SUBMIT</button>
      </form>
      
<!-- FORGOT PASSWORD LINK -->      
      <router-link id="forgot" to="#">
        <p id="forgot-text">Forgot your ID number or Password?</p>
      </router-link>
      </div>

  </div>
</template>

<script>
import {db} from '../../../../static/js/fire_config'
export default {
  props: {
    userList: {
      type: Array,
      required: true
    },
    idErrors: {
      type: String,
      required: true
    },
    passwordErrors: {
      type: String,
      required: true
    }
  },
  methods: {
    //LOGIN FUNCTION
    login: function () {
      let id = this.input.id
      let password = this.input.password
      for (let index = 0; index < this.userList.length; index++) {
            let userid = this.userList[index]["id-number"]
            let userpassword = this.userList[index]["password"]
            let userrole = this.userList[index]["role"]
            
            //PASSWORD ERRORS
            if (id == "" && password == "") {
                this.passwordErrors = "Invalid"
                this.idErrors = "Invalid"
              }  else
            
            if (id == userid && password == "") {
                this.passwordErrors = "Invalid"
                this.idErrors = ""
              } else

            if (id == "" && password == userpassword) {
                this.passwordErrors = ""
                this.idErrors = "Invalid"
              } else


            if (id != "" && password != "") {
              if (id != userid && password != userpassword) {
                  this.passwordErrors = "Invalid"
                  this.idErrors = "Invalid"
                } else
                if (id == userid && password != userpassword) {
                  this.idErrors = ""
                  this.passwordErrors = ""
                } else
                if (id == userid && password == userpassword) { 
                  if (userrole == "user") {
                    //PAGE REDIRECT
                    this.$router.push({ name: "home-page", query: {id: userid} })
                  } 
                  
                }
            }
      } 
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
      users: [],
      input: {
        id: [],
        password: [],
      }
    }
  },
  created (){
      let user = db.collection("User").get()
        .then(snapshot => {
          snapshot.forEach(doc => {
            this.users.push(doc.data());
            console.log(doc.data());
          });

          this.userList = this.users
          
        })
        .catch(err => {
          console.log('Error getting documents', err);
        });
    }
}
</script>

<style>
.errors {
  color: red;
  margin-left: 10px;
}

#forgot-text {
  margin-top: 10px;
  letter-spacing: 1px;
  font-size: 10px;
  color: black;
}

#forgot {
  text-decoration: none;
}


#welcome {
  text-align: center;
  letter-spacing: 4px;
}

#logo-stuff {
  display: flex;
  flex-direction: row;
}

#login-nav {
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    top: 0;
    right: 0;
    background-color: transparent!important;
    overflow-x: hidden; /* Disable horizontal scroll */
    transition: 0.5s;
    width: 100%;
    height: 70px;
    padding-left: 50px;
    }

#logo-eye {
  font-size: 10px;
  letter-spacing: 1px;
  font-weight: 300;
  margin-top: 1.5px;
  margin-left: 10px;
}

#login-form {
  width: 50%;
}

form {
  width: 400px;
  margin-left: auto;
  margin-right: auto;
}

#login-form-label {
  text-align: center;
  letter-spacing: 1px;
  font-size: 15px;
  font-weight: 400;
  margin-bottom: 40px;
  color: #ABB2B9;
  }

.label {
  font-size: 10px;
  letter-spacing: 1px;
  font-weight: 600;
  color: #85929E;
  display: flex;
  flex-direction: row;
}

#input-password,#input-id {
  border: none;
  border-radius: 4px;
  height: 40px;
  font-size: 12px;
  letter-spacing: 1px;
  font-weight: 500;
  color: #ABB2B9;
  background-color: #F2F3F4 ;
}

#login-button {
  margin-top: 8px;
  height: 45px;
  width: 100%;
  background-color: #7986CB;
  border: none;
  border-radius: 4px;
  color: white;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 2px
}

#login-button:hover {
  margin: 3px 0px;
  background-color: #5C6BC0;
  box-shadow: 21px 27px 54px -30px rgba(0,0,0,0.75);
}
</style>