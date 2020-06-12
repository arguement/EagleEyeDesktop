<template>
    <div>
        <main> 
            <div>
                <AdduserForm id="gazaform"></AdduserForm>
            </div>
        </main>
    </div>
</template> 
<script>
import AdduserForm from './forms/Adduser'
export default {
    name: 'Adduser-page',
    components: { AdduserForm },
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

  #gazaform {
    display: flex;
    flex-direction: row;
  }

</style>