<template>
    <div>
        <b-button v-on:click="loadRegion" class="region-button" variant="primary">{{name}}</b-button>
    </div>
</template>

<script>
    import bButton from 'bootstrap-vue/es/components/button/button'

    export default {
        name: 'Region',
        props: {
            name: String,
        },
        components: {
            'b-button': bButton
        },
        methods: {
            loadRegion: function () {
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