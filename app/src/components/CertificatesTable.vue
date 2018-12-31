<template>
  <BContainer fluid>
    <BFormGroup
      horizontal
      label="Filter"
      class="mb-0"
    >
      <BInputGroup>
        <BFormInput
          v-model="filter"
          placeholder="Type to Search"
        />
        <BInputGroupAppend>
          <BButton
            :disabled="!filter"
            @click="filter = ''"
          >
            Clear
          </BButton>
        </BInputGroupAppend>
      </BInputGroup>
    </BFormGroup>
    <BTable
      hover
      :items="certificates"
      :fields="fields"
      :filter="filter"
    />
  </BContainer>
</template>

<script>
  import bTable from 'bootstrap-vue/es/components/table/table';
  import bFormGroup from 'bootstrap-vue/es/components/form/form';
  import bFormInput from 'bootstrap-vue/es/components/form-input/form-input';
  import bInputGroup from 'bootstrap-vue/es/components/input-group/input-group';
  import bInputGroupAppend from 'bootstrap-vue/es/components/input-group/input-group-append';
  import bButton from 'bootstrap-vue/es/components/button/button';
  import bContainer from 'bootstrap-vue/es/components/layout/container'

  export default {
        name: 'CertificatesTable',
        components: {
            'BTable': bTable,
            'BFormGroup': bFormGroup,
            'BInputGroup': bInputGroup,
            'BFormInput': bFormInput,
            'BInputGroupAppend': bInputGroupAppend,
            'BButton': bButton,
            'BContainer': bContainer,
        },
        props: {
            certificates: {
                type: Array,
                default: function () {
                    return [];
                },
            }
        },
        data: function () {
            return {
                filter: null,
                fields: [
                    {key: 'CertificateArn', label: 'Certificate ARN', sortable: true},
                    {key: 'DomainName', label: 'Domain Name', sortable: true},
                    {key: 'InUse', label: 'In Use ?', sortable: true},
                    {key: 'InUseBy', label: 'In Use By', sortable: false}
                ]
            }
        }
    }
</script>

<style>

</style>