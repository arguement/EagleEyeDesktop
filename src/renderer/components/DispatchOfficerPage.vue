<template>
  <div>
    <main>
      <div id="dispatch-officer-page">
          <reportSidebar></reportSidebar>
          <dispatchofficer></dispatchofficer>
      </div>
    </main>
  </div>
</template>

<script>  
import dispatchofficer from './sidebarContent/dispatchofficer'
import reportSidebar from './sidebar/ReportSidebar'
  export default {
    name: 'dispatch-officer-page',
    components: { dispatchofficer, reportSidebar },
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

  #dispatch-officer-page {
    display: flex;
    flex-direction: row;
  }

</style>
