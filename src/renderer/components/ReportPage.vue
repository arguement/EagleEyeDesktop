<template>
  <div id="blah">
    <main>
      <div id="report-page">
        <reportSidebar></reportSidebar>
        <reportSidebarContent></reportSidebarContent>
      </div>
    </main>
  </div>
</template>

<script>
  import reportSidebar from './sidebar/reportSidebar'
  import reportSidebarContent from './sidebarContent/reportSidebarContent'
  

  export default {
    name: 'report-page',
    components: { reportSidebar, reportSidebarContent },
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

  #report-page {
    display: flex;
    flex-direction: row;
  }


</style>
