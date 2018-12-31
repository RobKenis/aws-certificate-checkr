<template>
  <div class="main-table">
    <CertificatesTable />
  </div>
</template>

<script>
    import CertificatesTable from "./CertificatesTable";
    export default {
        components: {CertificatesTable}
    }
</script>

<style>
.main-table {
    width: 60%;
    margin-left: 20%;
}
</style>