<script lang="ts" setup>
import { useDialogPluginComponent } from 'quasar';
import { reactive, onMounted } from 'vue';

const iProps = reactive({
  value: ''
});

defineEmits([
  ...useDialogPluginComponent.emits
]);

const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } = useDialogPluginComponent();

// onMounted(()=>iProps.value=props.value);

</script>

<template>
  <q-dialog ref="dialogRef" @hide="onDialogHide" persistent>
    <q-card class="q-dialog-plugin bg-grey-9" style="min-width:45em;">

      <q-card-section>

      </q-card-section>

      <q-card-actions align="right" style="margin:0 1.5em 1.5em;">
        <q-btn color="primary" icon='logout' label="Logout" @click='onDialogOK' class='text-weight-bold' />
        <q-btn color="primary" label="Close" @click='onDialogCancel' class='text-weight-bold'/>
      </q-card-actions>
    </q-card>

  </q-dialog>
</template>
