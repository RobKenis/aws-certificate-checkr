<template>
  <BContainer fluid>
    <ul id="usages">
      <CopyableRow
        v-for="arn in certificateUsages"
        :key="arn"
        :value="arn"
      />
    </ul>
  </BContainer>
</template>

<script>
  import bContainer from 'bootstrap-vue/es/components/layout/container';
  import CopyableRow from "./CopyableRow";

  export default {
        name: 'CertificateDetails',
        components: {
          CopyableRow,
          'BContainer': bContainer,
        },
        props: {
            certificateUsages: {
                type: Array,
                required: true,
            },
        }
    }
</script>

<style>

</style>