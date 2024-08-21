<script setup lang="ts">
import { ref, watch } from 'vue';
import Banner from './Banner.vue';
import Nav from './Nav.vue';
import Intro from './Intro.vue';
import News from './News.vue';
const loaded = defineModel<boolean>();
let appear = ref("")
watch(loaded, (stat) => {
  if (!stat) {
    appear.value = "opacity-0 translate-y-full"
  }
  if (stat) {
    setTimeout(() => {
      appear.value = "opacity-100 translate-y-0 sticky top-0"
    }, 300)
  }

})
appear.value = "opacity-0 translate-y-full"
</script>

<template>
  <Banner v-model="loaded" />
  <Nav :class="appear" class="transition-transform" v-show="loaded" />
  <Intro v-show="loaded" />
  <News v-show="loaded" />
</template>
