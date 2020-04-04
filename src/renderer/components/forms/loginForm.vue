<template>
  <div id="login-form">
    <router-view></router-view>
    <form>
    <h1 id="login-form-label">Log in to your account.</h1>
  <div class="form-group">
    <label class="label" for="exampleInputEmail1">ID NUMBER</label>
    <input type="email" class="form-control" id="input-email" aria-describedby="emailHelp">
  </div>
  <div class="form-group">
    <label class="label" for="exampleInputPassword1">PASSWORD</label>
    <input type="password" class="form-control" id="input-password">
  </div>
  <router-link
  to="/home"
  >
  <button type="submit" class="btn btn-primary" id="login-button" href="/home">SUBMIT</button>
  </router-link>
</form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      electron: process.versions.electron,
      name: this.$route.name,
      node: process.versions.node,
      path: this.$route.path,
      platform: require('os').platform(),
      vue: require('vue/package.json').version
    }
  }
}
</script>

<style>

#login-form {
  width: 50%;
}

form {
  width: 300px;
  margin-left: auto;
  margin-right: auto;
}

#login-form-label {
font-size: 30px;
font-weight: 400;
margin-bottom: 40px;
}

.label {
  font-size: 10px;
  letter-spacing: 1px;
  font-weight: 600;
  color: #85929E;
}

#input-password,#input-email {
border: none;
border-radius: 4px;
background:#F2F3F4;
height: 40px;
font-size: 12px;
letter-spacing: 1px;
font-weight: 600;
color: #ABB2B9;
}

#login-button {
  margin-top: 8px;
  height: 43px;
  width: 100%;
  background-color: #3F51B5;
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