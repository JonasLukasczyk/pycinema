<script setup>
import NodeEditor from './components/NodeEditor.vue'
</script>

<template>
  <NodeEditor/>
</template>

<style>
.material-symbols-outlined {
  font-variation-settings:
    'FILL' 0,
    'wght' 400,
    'GRAD' 0,
    'opsz' 24
}

.rotating {
  animation: spin 2s linear infinite;
  display: inline-block; /* Ensure it rotates properly */
  transform-origin: center center;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

</style>
