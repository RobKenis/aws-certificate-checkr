<template>
  <div class="regions">
    <h1>Regions</h1>
    <ul class="regions-list">
      <li>
        <Region
          v-for="region in regions"
          :key="region"
          :name="region"
        />
      </li>
    </ul>
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
        width: 40%;
        margin-left: 30%;
    }

    ul {
        list-style-type: none;
    }
</style>