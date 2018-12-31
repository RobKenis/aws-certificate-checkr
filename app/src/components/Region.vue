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
    import { EventBus } from './event-bus.js';

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
                EventBus.$emit('region-clicked', {region: this.name});
            }
        }
    }
</script>

<style scoped>
    .region-button {
        margin: 1em;
    }
</style>