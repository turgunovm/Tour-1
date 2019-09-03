<template>
  <div id="app" variant="dark">
      <app-header></app-header>
            <b-container>
                   <router-view></router-view>
            </b-container>
      
  </div>
  
</template>

<script>
import AppHeader from './components/AppHeader'
export default {
  name: 'app',
  components: {
    'app-header':AppHeader
  }
}
</script>

<style>
  #app{
    background-color:black;
  }
</style>
