<template>
  <div class="regions">
    <h1>Regions</h1>
    <div class="regions-list">
      <Region
        v-for="region in regions"
        :key="region"
        :name="region"
      />
    </div>
  </div>
</template>

<script>
    import Region from './Region.vue'

    export default {
        name: 'Regions',
        components: {
            Region
        },
        data: function () {
            return {regions: ["eu-central-1", "eu-west-1", "us-east-1"]}
        }
    }
</script>

<style scoped>
    .regions-list {
        display: inline;
    }
</style>