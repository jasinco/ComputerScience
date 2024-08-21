<script setup lang="ts">
import { onMounted, ref } from 'vue';

const chinese_word_choosing = "電腦,資訊,網路,應用程式,C,C++";
const banner = "臺中高工資訊科";
const banner_mesg = ref("");

const loaded = defineModel()

const banner_eng = ref("opacity-0")

onMounted(() => {
  let keywords = chinese_word_choosing.split(",");
  let id = 0;
  let count = 0;

  const choose = () => {
    let selected = Math.floor(Math.random() * keywords.length);
    let t = keywords[selected];
    keywords.splice(selected, 1);
    return t;
  };

  banner_mesg.value = choose();
  id = window.setInterval(() => {
    if (count > 1) {
      banner_mesg.value = banner;
      setTimeout(() => {
        banner_eng.value = "transition-opacity opcaity-100";
        loaded.value = true;
      }, 800)
      clearInterval(id)
      return
    }
    banner_mesg.value = choose();
    count++;
  }, 800)


})
</script>
<template>
  <div class="w-dvw h-9/10 flex justify-center items-center flex-col">
    <h1 id="banner" class="w-full">
      {{ banner_mesg }}
    </h1>
    <Transition>
      <h2 class="text-3xl select-none font-pixel" :class="banner_eng">
        Computer Science
      </h2>
    </Transition>
  </div>
</template>
<style scoped>
#banner {
  font-size: 5rem;
  user-select: none;
  font-family: cubic-11;
}
</style>
