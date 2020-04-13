7<template>
  <main>
  <div id="analytics-page">
      <mapSidebar></mapSidebar>
      <mapSidebarContent></mapSidebarContent>
  </div>
  </main>
</template>

<script>
import mapSidebar from './sidebar/mapSidebar'
import mapSidebarContent from './sidebarContent/mapSidebarContent'

  export default {
    name: 'analytics-page',
    components: { mapSidebar, mapSidebarContent },
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

#analytics-page {
    display: flex;
    flex-direction: row;
  }
</style>
