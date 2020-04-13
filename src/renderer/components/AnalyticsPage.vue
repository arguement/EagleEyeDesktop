<template>
  <div>
    <main>
      <div id="analytics-page">
      </div>
    </main>
  </div>
</template>

<script>
  export default {
    name: 'analytics-page',
    components: {  },
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
    margin: 0;
    padding: 0;
  }

  body { font-family: 'Source Sans Pro', sans-serif; }

  #analytics-page {
    display: flex;
    flex-direction: row;
  }

</style>
