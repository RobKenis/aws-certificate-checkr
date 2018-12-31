<template>
  <BTable
    hover
    :items="items"
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
        data: function () {
            return {
                fields: [
                    {key: 'first_name', sortable: true},
                    {key: 'last_name', sortable: true},
                    {key: 'age', sortable: true}
                ],
                items: [
                    {isActive: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald'},
                    {isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw'},
                    {isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson'},
                    {isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney'}
                ]
            }
        }
    }
</script>

<style>

</style>