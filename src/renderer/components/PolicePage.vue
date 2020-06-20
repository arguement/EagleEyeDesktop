<template>
  <div>
    <main>
      <div id="police-page">
        <policeSidebar></policeSidebar>
        <policeSidebarContent></policeSidebarContent>
      </div>
    </main>
  </div>
</template>

<script>
import policeSidebar from './sidebar/policeSidebar'
import policeSidebarContent from './sidebarContent/policeSidebarContent'
  export default {
    name: 'police-page',
    components: { policeSidebar, policeSidebarContent },
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

  #police-page {
    display: flex;
    flex-direction: row;
  }

</style>
