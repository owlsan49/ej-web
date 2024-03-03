<script setup lang="ts">
import { ref } from 'vue'
// import { RouterView } from 'vue-router';

const activeIndex = ref('1')
const activeRouter = ref(true)
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<template>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" :router=activeRouter>
        <el-menu-item index="/yesor">Yes or?</el-menu-item>
        <el-menu-item index="/obj">Objective!</el-menu-item>
    </el-menu>
    <br/>
    <!-- <RouterView /> -->
</template>

<style scoped></style>