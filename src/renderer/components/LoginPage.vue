<template>
  <main>
  <div id="login-page">
    <loginForm></loginForm>
  </div>
  </main>
</template>

<script>
  import loginForm from './forms/loginForm'
  import loginFormContent from './formContent/loginFormContent'

  export default {
    name: 'login-page',
    components: { loginForm, loginFormContent },
    methods: {
      open (link) {
        this.$electron.shell.openExternal(link)
      }
    }
  }
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body { font-family: 'Source Sans Pro', sans-serif; }

  #login-page {
    background-color: #E8EAF6;
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }
</style>
