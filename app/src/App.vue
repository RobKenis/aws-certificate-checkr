<template>
  <div id="app">
    <Regions />
    <CertificatesTable />
  </div>
</template>

<script>
    import Regions from './components/Regions.vue'
    import CertificatesTable from "./components/CertificatesTable";

    export default {
        name: 'App',
        components: {
          CertificatesTable,
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
