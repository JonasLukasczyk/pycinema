<script lang="ts" setup>
import { useDialogPluginComponent } from 'quasar';
import { reactive, onMounted, ref, nextTick } from 'vue';

const canvasContainer = ref(null);

const props = defineProps({
  port: Object
})

const iProps = reactive({
  port_str: ''
});

defineEmits([
  ...useDialogPluginComponent.emits
]);

const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } = useDialogPluginComponent();

const init = ()=>{
  for(let image of props.port.value){
    const canvas = document.createElement('canvas');
    canvasContainer._value.appendChild(canvas);

    const pixelData = image.channels.rgba;

    const ctx = canvas.getContext('2d');
    const rows = pixelData.length;
    const cols = pixelData[0].length;

    canvas.width = cols;
    canvas.height = rows;

    const imageData = ctx.createImageData(cols, rows);

    let pixelArray = [];
    for (let row = 0; row < rows; row++) {
      for (let col = 0; col < cols; col++) {
        const rgba = pixelData[row][col];
        pixelArray.push(...rgba);
      }
    }
    imageData.data.set(pixelArray);
    ctx.putImageData(imageData, 0, 0);
  }
};

onMounted(async ()=>{
  setTimeout(init, 100)
});

</script>

<template>
  <q-dialog ref="dialogRef" @hide="onDialogHide">
    <q-card class="q-dialog-plugin bg-grey-9" style="min-width:45em;">
      <q-card-section>
        <q-input bg-color="grey-6" color="white" filled readonly :label='`${props.port.parent}.${props.port.is_input?"inputs":"outputs"}.${props.port.name}`' v-model='props.port.value_str'/>
      </q-card-section>

      <q-card-section>
        <div ref='canvasContainer'></div>
      </q-card-section>
    </q-card>

  </q-dialog>
</template>
