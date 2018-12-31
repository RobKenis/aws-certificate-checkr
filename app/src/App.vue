<template>
  <div id="app">
    <Regions />
    <Certificates />
  </div>
</template>

<script>
    import Regions from './components/Regions.vue'
    import Certificates from "./components/Certificates";

    export default {
        name: 'App',
        components: {
            Certificates,
            Regions
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
