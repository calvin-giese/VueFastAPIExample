<template>
  <div class="home">
    <ItemComponent/>
  </div>
</template>

<script>
// @ is an alias to /src
import ItemComponent from '@/components/ItemComponent.vue'

export default {
  name: 'ItemView',
  components: {
    ItemComponent
  }
}
</script>
