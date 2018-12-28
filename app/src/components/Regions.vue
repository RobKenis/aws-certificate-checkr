<template>
    <div class="regions">
        <h1>Regions</h1>
        <div class="regions-list">
            <Region v-for="region in regions" v-bind:key="region" :name="region"></Region>
        </div>
    </div>
</template>

<script>
    import Region from './Region.vue'

    export default {
        name: 'Regions',
        data: function () {
            return {regions: ["eu-central-1", "eu-west-1", "us-east-1"]}
        },
        components: {
            Region
        }
    }
</script>

<style scoped>
    .regions-list {
        display: inline;
    }
</style>