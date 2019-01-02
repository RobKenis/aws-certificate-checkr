<template>
  <div>
    <span>
      {{ value }}
    </span>
  </div>
</template>

<script>
    export default {
        name: 'CopyableRow',
        props: {
            value: {
                type: String,
                required: true
            }
        },
    }
</script>

<style scoped>
    .container {
        width: 40em;
    }

    .row {
        overflow: hidden;
        white-space: nowrap;
        -ms-text-overflow: ellipsis;
        text-overflow: ellipsis;
        width: 28em;
        height: 1.2em;
    }

    .row:hover {
        overflow: visible;
    }
</style>