<template>
  <div class="main-table">
    <CertificatesTable :certificates="certificates" />
  </div>
</template>

<script>
    import CertificatesTable from "./CertificatesTable";
    import axios from "axios";
    import { EventBus } from './event-bus.js';

    export default {
        components: {CertificatesTable},
        data: function () {
            return {
                certificates: [],
            }
        },
        created: function(){
          EventBus.$on('region-clicked', event => this.getCertificates(event));
        },
        methods: {
            getCertificates: function (e) {
                console.log("Fetching results for [" + e.region + "]");
                axios
                    .get('https://s3-eu-west-1.amazonaws.com/rob-k-public-s3/certificates.json')
                    .then(response => response.data).then(certs => this.certificates = certs)
            }
        }
    }
</script>

<style>
    .main-table {
        width: 60%;
        margin-left: 20%;
    }
</style>