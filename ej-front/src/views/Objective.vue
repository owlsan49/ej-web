<script setup lang="ts">
import { onBeforeMount, ref } from 'vue';
import { GetObj } from '@/apis/read.ts'
import { BASEURL } from '@/utils/request.js'

let img = ref()
let info = ref()
onBeforeMount(() => {
    GetObj({})
    .then(response => {
        console.log('@', response)
        img.value = response.data.img_path
        info.value = response.data.info
    })
    .catch(error => {
        console.log(error)
    })
})
</script>

<template>
    <p>{{ info }}</p>
    <img :src="`${BASEURL}${img}`" width="600" height="400">
</template>

<style scoped></style>