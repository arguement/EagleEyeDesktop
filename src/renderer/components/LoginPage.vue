<template>
  <div id="wrapper">
    <loginForm></loginForm>
    <loginFormContent></loginFormContent>
  </div>
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

  #wrapper {
    background:
      radial-gradient(
        ellipse at top left,
        rgba(255, 255, 255, 1) 40%,
        rgba(229, 229, 229, .9) 100%
      );
    height: 100vh;
    padding: 60px 80px;
    width: 100vw;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }
</style>
