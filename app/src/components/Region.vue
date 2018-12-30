<template>
  <BButton
    class="region-button"
    variant="primary"
    @click="loadRegion"
  >
    {{ name }}
  </BButton>
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
            loadRegion: function () {
                console.log("Requesting info for [" + this.name + "]");
            }
        }
    }
</script>

<style scoped>
    .region-button {
        margin: 1em;
    }
</style>