<template>
  <div>
    <main>
      <div id="analytics-page">
        <analyticsSidebar></analyticsSidebar>
        <keep-alive>
        <analyticsSidebarContent></analyticsSidebarContent>
        </keep-alive>
      </div>
    </main>
  </div>
</template>

<script>
  import analyticsSidebar from './sidebar/analyticsSidebar'
  import analyticsSidebarContent from './sidebarContent/analyticsSidebarContent'
  
  export default {
    name: 'analytics-page',
    components: { analyticsSidebar, analyticsSidebarContent },
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
