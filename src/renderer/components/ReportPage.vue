<template>
  <div>
    <main>
        <reportSidebar></reportSidebar>
    </main>
  </div>
</template>

<script>
  import reportsidebar from './sidebar/reportSidebar'

  export default {
    name: 'report-page',
    components: { reportSidebar},
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


</style>
