<template>
  <div>
    <main>
      <div id="home-page">
        <homeSidebar></homeSidebar>
        <homeSidebarContent></homeSidebarContent>
      </div>
    </main>
  </div>
</template>

<script>
  import homeSidebar from './sidebar/homeSidebar'
  import homeSidebarContent from './sidebarContent/homeSidebarContent'

  export default {
    name: 'home-page',
    components: { homeSidebar, homeSidebarContent },
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

  #home-page {
    display: flex;
    flex-direction: row;
  }

</style>
