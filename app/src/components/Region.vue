<template>
  <div>
    <BButton
      class="region-button"
      variant="primary"
      @click="loadRegion"
    >
      {{ name }}
    </BButton>
  </div>
</template>

<script>
    import bButton from 'bootstrap-vue/es/components/button/button'

    export default {
        name: 'Region',
        components: {
            'BButton': bButton
        },
        props: {
            name: {
                type: String,
                required: true
            }
        },
        methods: {
            loadRegion: function() {
                console.log("Requesting info for [" + this.name + "]");
            }
        }
    }
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css?family=Roboto+Mono');

    .region-button {
        font-family: 'Roboto', sans-serif;
        margin: 1em;
        float: left;
    }
</style>