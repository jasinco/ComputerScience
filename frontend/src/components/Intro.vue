<script setup lang="ts">
</script>

<template>
  <div class="w-dvw h-9/10 ">
    <div class="flex flex-row ml-5">
      <h1>
        介紹
      </h1>
      <h1 class="font-pixel pl-5">
        Introduction
      </h1>
    </div>
    <div class="grid grid-cols-4 mt-20">
      <div class="list_item">
        <h2>
          程式設計
        </h2>
        <ul>
          <li>計算思維</li>
          <li>解決問題能力(演算法)</li>
          <li>C, C++, C#, SQL</li>
        </ul>
      </div>
      <div class="list_item">
        <h2>
          電子學
        </h2>
        <ul>
          <li>電子元件特性</li>
          <li>運算放大器 OPA</li>
          <li>運用電子元件能力</li>
        </ul>
      </div>
      <div class="list_item">
        <h2>
          單晶片微處理機(SoC, MCU)
        </h2>
        <ul>
          <li>微處理機架構</li>
          <li>設計小型MCU應用系統的技能</li>
        </ul>
      </div>
      <div class="list_item">
        <h2>
          數位邏輯
        </h2>
        <ul>
          <li>二進制數字系統</li>
          <li>布林代數</li>
          <li>組合邏輯與序向邏輯電路</li>
          <li>FPGA 應用</li>
        </ul>
      </div>
    </div>
  </div>
</template>
<style scoped>
#container {
  grid-template-columns: 1fr 1fr 1fr 1fr;
}

.list_item h2 {
  font-size: 1.3rem;
}
</style>
