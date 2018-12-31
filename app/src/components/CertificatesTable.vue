<template>
  <BTable
    hover
    :items="certificates"
    :fields="fields"
  />
</template>

<script>
    import bTable from 'bootstrap-vue/es/components/table/table'

    export default {
        name: 'CertificatesTable',
        components: {
            'BTable': bTable
        },
        props: {
            certificates: {
                type: Array,
                default: function () {
                    return [];
                },
            }
        },
        data: function () {
            return {
                fields: [
                    {key: 'CertificateArn', label: 'Certificate ARN', sortable: true},
                    {key: 'DomainName', label: 'Domain Name', sortable: true},
                    {key: 'InUse', label: 'In Use ?', sortable: true},
                    {key: 'InUseBy', label: 'In Use By', sortable: false}
                ]
            }
        }
    }
</script>

<style>

</style>